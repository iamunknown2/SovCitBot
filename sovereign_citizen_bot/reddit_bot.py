import os
import traceback
from time import sleep

import praw

from config import user_agent, username, password, subreddit_list, delay_between_polls
from quote_generator import get_quote


def check_config():
    if not os.path.isfile("./config.py"):
        print("You must create a config file")
        exit(1)


def login():
    print("Logging in as /u/" + username + " with user agent " + user_agent)
    r = praw.Reddit(user_agent=user_agent)
    r.login(username=username, password=password)
    return r


def main():
    already_replied = set()
    check_config()
    r = login()
    while True:
        try:
            print("Looking for new mail")
            for comment in r.get_unread():
                print("Id: " + comment.id + "\nSubreddit: " + str(comment.subreddit) + "\nBody: " + comment.body)

                if ("/u/" + username).lower() not in comment.body.lower():
                    comment.mark_as_read()
                    print("Comment is not a username mention")
                    continue

                if str(comment.subreddit) not in subreddit_list:
                    comment.mark_as_read()
                    print("Comment is not in subreddit list")
                    continue

                for reply in comment.replies:
                    if reply.author is username:
                        already_replied.add(reply.id)
                        print("Already replied: " + reply)
                        break

                if comment.id not in already_replied:
                    quote = get_quote()
                    print("Commenting with quote '" + quote + "'")
                    comment.reply(quote)
                    comment.mark_as_read()
            print("Sleeping...")
            sleep(delay_between_polls)

        # Stop if someone manually interrupts
        except KeyboardInterrupt:
            print("Keyboard interrupt received. Shutting down")
            exit(0)

        # Praw handles the API Rate limits for us, we just have to sleep and try again
        except praw.errors.RateLimitExceeded:
            print("Rate limit exceeded")
            sleep(delay_between_polls)
            continue

        # Catch all exceptions so in case of a simple error the next loop will be successful
        except Exception as e:
            print(traceback.format_exc())
            print("Error: ", e)
            print("Waiting " + delay_between_polls + " seconds before trying again")
            sleep(delay_between_polls)
            continue


if __name__ == "__main__":
    main()
