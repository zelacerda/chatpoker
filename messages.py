# ANSI color codes constants
P = "\033[95m"  # Purple
G = "\033[92m"  # Green
Y = "\033[93m"  # Yellow
R = "\033[91m"  # Red
K = "\033[30m"  # Black
W = "\033[107m" # White (foreground)
B = "\033[1m"   # Bold
D = "\033[0m"   # Restore to default
BP = B + P
BG = B + G
BY = B + Y
BR = B + R

SUITS = ["♣", "♥", "♠", "♦"]
VALS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

PROMPT = f" {BP}>{D} "

def render_card(v, s):
    """Renders the card central line with number and suit"""
    l = B + W
    if s in (1, 3): # Red suit
        l += R
    else:           # Black suit
        l += K
    l += f" {VALS[v]:2}{SUITS[s]} {D}"
    return l

def render_hand(hand):
    """Renders the hand of cards"""
    white_line = 5 * f" {W}     {D} " # White top and bottom cards lines
    card_line = "  ".join([render_card(v, s) for v, s in hand])
    t = (f"\n {Y}   1      2      3      4      5{D}\n"
         f" {white_line}\n"
         f"  {card_line}\n"
         f" {white_line}\n")
    return t

def welcome():
    t = (f"\n Hi! Welcome to {BY}chatpoker{D}!\n"
         f" Press {BP}t{D} whenever you want to see the pay table.\n"
         f" Or {BP}q{D} to quit and exit the game at any time.\n"
         f" Press {BP}Enter{D} to start the game. Good luck!\n")
    return t

def bet(chips):
    t = (f"\n You have {BG}{chips} chips{D} to play.\n"
         f" How many chips do you want to bet this round?\n")
    return t

def bet_limit(chips):
    t = f"\n {R}Hey! You cannot bet more than {BR}{chips} chips{D}{R}.{D}"
    return t

def bet_error():
    t = f"\n {R}Sorry, but you need to enter a valid number.{D}"
    return t

def your_hand(hand):
    t = (f"\n Your {BY}starting hand{D} is:\n"
         f" {render_hand(hand)}")
    return t

def change():
    t = (f" Which cards do you want {BY}to hold{D}?"
         f" Type its positions without spaces.\n"
         f" E.g. To hold cards at {Y}2{D}, {Y}3{D} and {Y}5{D}"
         f" positions, type {BP}235 + Enter{D}.\n"
         f" If you want to change all your cards, just press {BP}Enter{D}.\n")
    return t

def change_error():
    t = f"\n {R}Nope... You must choose valid card positions.{D}"
    return t

def result(hand, pattern, prize):
    if prize == 0:
        msg = f"You didn't make a poker hand. Sorry, {BG}no bucks{D} for you."
    else:
        msg = f"You made a {BY}{pattern}{D} and won {BG}{prize} chips{D}!"
    t = (f"\n All right. This is your {BY}final hand{D}:\n"
         f" {render_hand(hand)}\n"
         f" {msg}")
    return t

def new_hand():
    t = f"\n Press {BP}Enter{D} to start a new round.\n"
    return t

def end():
    t = (f"\n What a pity! You lost all your bucks :(\n"
         f" Want to play again? Just press {BP}Enter{D}"
         f" and I'll lend you some money.\n")
    return t

def quit(chips):
    t = (f"\n You left the game with {BG}{chips} chips{D}.\n"
         f" See you later!\n")
    return t

def table():
    t = (f"\n This is the {BY}pay table{D} for each chip bet:\n\n"
         f"  Royal Flush:        {BG}800{D}\n"
         f"  Straight Flush:      {BG}50{D}\n"
         f"  Four of a kind:      {BG}25{D}\n"
         f"  Full House:           {BG}9{D}\n"
         f"  Flush:                {BG}6{D}\n"
         f"  Straight:             {BG}4{D}\n"
         f"  Three of a kind:      {BG}3{D}\n"
         f"  Two Pair:             {BG}2{D}\n"
         f"  Jacks or Better:      {BG}1{D}")
    return t
