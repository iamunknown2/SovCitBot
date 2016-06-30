import random

snippets = {
    "initial": [
        ["The GOLD FRINGES on the US FLAG in a court", "gold fringe"],
        ["Someone's NAME in ALL CAPITALS don't refer to the SAME PERSON . ", "all caps name"],
        ["Actually , the POLICE have NO RIGHT to ARREST you . "
         "Instead ,they can only DETAIN you. Only SHERIFFS can arrest you . ", "AM I BEING DETAINED"]
    ], "gold fringe": [
        [" indicate the COURT as a COURT within MARITIME LAW . ", "maritime"]
    ], "maritime": [
        ["This means that ANY RULINGS in COURT (I.E ALL OF THEM) are uner MARTIAL LAW , "
         "where the DEFENDANT is GUILTY until PROVEN INNOCENT . THE US IS STILL UNDER MARTIAL LAW . "
         "OPEN YOUR EYES !!!", "end"], ["Therefore , all vehicles are considered as boats or ships . ", "cars"]
    ], "cars": [["The ABANDONED SHIPWRECK ACT protects SHIPWRECKS (I.E CRASHED CARS) "
                 "from TREASURE HUNTERS and SALVAGERS (AKA THE POLICE) . Therefore , CONTEST your CHARGES "
                 "by declaring that they ILLEGALLY pulled you over .", "end"],
                ["INTERNATIONAL MARITIME LAW makes the act of PIRACY (I.E THE POLICE PULLING YOU OVER AND"
                 " FORCING YOU TO PAY) ILLEGAL . CONTEST your CHARGES in COURT by SUING the STATE for COMMITTING"
                 " the act of PIRACY .", "end"]
                ], "all caps name": [
        ["According to ENGLISH EXPERTS , NAMES are not to be written in ALL CAPS . ", "denial"],
        ["Instead, ALL CAPS NAMES refer to a COMPLETELY DIFFERENT and NON-EXISTENT LEGAL ENTITY . ", "denial"]
    ], "denial": [
        ["If they give your name in ALL-CAPS in a COURT CASE, "
         "POINT OUT that the ALL-CAPS NAME DOES NOT REFER to you and you will be FREE TO GO .", "end"]
    ], "AM I BEING DETAINED": [
        ["If you ASK them , ' AM I BEING DETAINED ' , ", "police arrest reaction"],
        ["You should ARGUE in COURT that the POLICE had made an ILLEGAL ARREST , "
         "since the POLICE don't have the RIGHT to make ARRESTS .", "end"]
    ],
    "police arrest reaction": [
        ["they will be FORCED by the LAW to either go get a SHERIFF or GIVE UP .", "end"],
        ["the POLICE'S REPLY can INDICATE their legal ' know-how ' .", "end"]
    ]
}


def next_snippet(key: str = "initial") -> str:
    return random.choice(snippets[key])


def get_quote() -> str:
    snippet = next_snippet()
    quote = snippet[0]
    while snippet[1] is not "end":
        snippet = next_snippet(snippet[1])
        quote += snippet[0]
    return quote


if __name__ == "__main__":
    print(get_quote())
