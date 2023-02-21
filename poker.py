import sys
import random

import messages as msg
import check as chk


def get_deck():
    """
    A deck is a list made of 54 tuples, in the form of (v, s),
    with v representing value (from 0 to 12) and s the suit (from 0 to 3).
    """
    return [(v, s) for s in range(4) for v in range(13)]


class Deck:
    """
    Implements the Deck object. The stack can be shuffled
    and it's possible to pick cards from the stack.
    """
    def __init__(self, shuffle=True):
        self.stack = get_deck()
        if shuffle:
            self.shuffle()

    def shuffle(self):
        random.shuffle(self.stack)

    def pick(self, n):
        result = []
        for _ in range(n):
            result.append(self.stack.pop())
        return result


class Hand:
    """
    Implements the Hand object. It's possible to change cards
    picking another ones from the deck stack.
    """
    def __init__(self, deck, init_hand=5):
        self.deck = deck
        self.hand = self.deck.pick(init_hand)

    def change(self, cards_pos):
        new_cards = self.deck.pick(len(cards_pos))
        for i, p in enumerate(cards_pos):
            self.hand[p] = new_cards[i]


class Game:
    """
    Implements the Game object.
    """
    def __init__(self, chips=1000):
        self.default_chips = chips
        self.chips = self.default_chips
        self.bet = 0
        self.state = "start"
        self.loop()

    def eval_prompt(self):
        i = input(msg.PROMPT)
        if i == "t": # Show pay table
            print(msg.table())
            return False
        elif i == "q": # Quit game
            self.quit()
        elif self.state in ["start", "result"]:
            return True
        elif self.state == "bet":
            try:
                v = int(i)
                return v
            except ValueError:
                print(msg.bet_error())
                return False
        elif self.state == "change":
            f = [e for e in i if e in "12345"]         # Valid positions
            if f == list(i) and len(i) == len(set(i)): # Only unique pos
                return i
            else:
                print(msg.change_error())
                return False
        return i

    def start(self):
        print(msg.welcome())
        r = self.eval_prompt()
        if r:
            self.state = "bet"

    def do_bet(self):
        print(msg.bet(self.chips))
        v = self.eval_prompt()
        if type(v) is int:
            if v <= 0:
                print(msg.bet_error())
            elif v > self.chips:
                print(msg.bet_limit(self.chips))
            else:
                self.bet = v
                self.chips -= self.bet
                self.deck = Deck()
                self.hand = Hand(self.deck)
                self.state = "change"

    def change(self):
        print(msg.your_hand(self.hand.hand))
        print(msg.change())
        r = self.eval_prompt()
        if r or r == "":
            to_change = [n for n in range(5) if str(n + 1) not in r]
            self.hand.change(to_change)
            self.state = "result"

    def result(self):
        pattern, prize = chk.get_prize(self.hand.hand)
        self.chips += self.bet * prize
        print(msg.result(self.hand.hand, pattern, self.bet * prize))
        self.bet = 0
        if self.chips == 0: # Loose game
            print(msg.end())
            _ = self.eval_prompt()
            self.chips = self.default_chips
        else:
            print(msg.new_hand())
            self.bet = 0
            _ = self.eval_prompt()
        self.state = "bet"

    def quit(self):
        print(msg.quit(self.chips + self.bet))
        sys.exit()

    def loop(self):
        while True:
            if self.state == "start":
                self.start()
            elif self.state == "bet":
                self.do_bet()
            elif self.state == "change":
                self.change()
            elif self.state == "result":
                self.result()

if __name__ == "__main__":
    Game()
