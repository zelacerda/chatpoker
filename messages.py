PURPLE = '\033[95m'
BLUE = '\033[94m'
CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
BLACK = '\033[30m'
UNDERLINE = '\033[4m'
FOREWHITE = '\033[107m'

suit_map = {0: "♣",
            1: "♥",
            2: "♠",
            3: "♦"}

val_map = {0: "2", 1: "3", 2: "4", 3: "5", 4: "6",
           5: "7", 6: "8", 7: "9", 8: "10", 9: "J",
           10: "Q", 11: "K", 12: "A"}

PROMPT = f"    {BOLD}{PURPLE}> {ENDC}"

def render_card(v, s):
    t = BOLD
    if s in (1, 3):
        t += FOREWHITE
        t += RED
    else:
        t += FOREWHITE
        t += BLACK
    t += f" {val_map[v]:2}{suit_map[s]}"
    t += " "
    t += ENDC

    return t

def render_hand(hand):
    pos = f"{YELLOW}  1     2     3     4     5{ENDC}"
    borders = 5 * f"{FOREWHITE}     {ENDC} "
    return f"""
    {pos}
    {borders}
    {" ".join([render_card(v, s) for v, s in hand])}
    {borders}
    """

def welcome():
    return f"""
    Hi! Welcome to {BOLD}{YELLOW}Chat Video Poker!{ENDC}
    Press {BOLD}{PURPLE}t{ENDC} whenever you want to see the paytable.
    Or {BOLD}{PURPLE}q{ENDC} to quit and exit the game at any time.
    Press {BOLD}{PURPLE}Enter{ENDC} to start the game. Good luck!
    """

def bet(chips):
    return f"""
    You have {BOLD}{GREEN}{chips} chips{ENDC} to play.
    How many chips do you want to bet this round?
    """

def bet_limit(chips):
    return f"""
    {RED}Hey! you cannot bet more than {chips} chips.{ENDC}"""

def bet_error():
    return f"""
    {RED}Sorry, but you need to enter a valid number.{ENDC}"""

def your_hand(hand):
    rendered_hand = render_hand(hand)
    return f"""
    Your starting hand is:
    {rendered_hand}"""

def change():
    return f"""
    Which cards do you want {BOLD}{YELLOW}to hold{ENDC}? Select its positions without spaces.
    E.g., to hold the cards from positions {YELLOW}1, 3 and 5{ENDC}, press {BOLD}{PURPLE}135 + Enter{ENDC}.
    If you want to change all the cards, just press {BOLD}{PURPLE}Enter{ENDC}.
    """

def change_error():
    return f"""
    {RED}My bad... You must choose only valid card positions.{ENDC}"""

def result(hand, pattern, prize):
    rendered_hand = render_hand(hand)
    if prize == 0:
        prize_msg = "You didn't make any poker hands and lost your bet :("
    else:
        prize_msg = f"You made a {BOLD}{YELLOW}{pattern}{ENDC} and won {BOLD}{GREEN}{prize} chips{ENDC}!"
    return f"""
    All right. This is your final hand:
    {rendered_hand}

    {prize_msg}"""

def new_hand():
    return f"""
    Press {BOLD}{PURPLE}Enter{ENDC} to start a new round.
    """

def end():
    return f"""
    What a pity! You lost all your rich buck :(
    Want to play again? Just press {BOLD}{PURPLE}Enter{ENDC} and I'll lend you some money.
    """

def quit(chips):
    return f"""
    You left the game with {BOLD}{GREEN}{chips} chips{ENDC}.
    See you later!
    """

def table():
    return f"""
    This is the paytable for each chip bet:

    Royal Flush:        {BOLD}{YELLOW}800{ENDC}
    Straight Flush:      {BOLD}{YELLOW}50{ENDC}
    Four of a kind:      {BOLD}{YELLOW}25{ENDC}
    Full House:           {BOLD}{YELLOW}9{ENDC}
    Flush:                {BOLD}{YELLOW}6{ENDC}
    Straight:             {BOLD}{YELLOW}4{ENDC}
    Three of a kind:      {BOLD}{YELLOW}3{ENDC}
    Two Pair:             {BOLD}{YELLOW}2{ENDC}
    Jacks or Better:      {BOLD}{YELLOW}1{ENDC}"""
