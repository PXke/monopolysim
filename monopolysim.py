# coding=utf-8

import random

# Lots of information come from: http://monopoly.wikia.com/wiki/Main_Page

class Actions:
    """
    Enum listing all actions linked to cards and special cases.
    """
    def __init__(self):
        pass

    @staticmethod
    def draw_chance_card(game, player):
        """Draw a chance card and apply its effects."""
        card = game.chance_deck.draw()
        card.action(game, player)

    @staticmethod
    def draw_community_card(game, player):
        """Draw a community card and apply its effects."""
        card = game.chance_deck.draw()
        card.action(game, player)

    @staticmethod
    def go_to_jail(game, player):
        """Set the player in jail"""
        player.position = 10
        player.jailed = True
        game.board.spaces[10].used += 1

    @staticmethod
    def dummy(game, player):
        """Useless action to avoid to code some others."""
        pass

    @staticmethod
    def advance_to_go(game, player):
        """Move the player to go space."""
        player.position = 0
        game.board.spaces[0].used += 1

    @staticmethod
    def advance_to_illinois_ave(game, player):
        """Move the player to illinois avenue"""
        player.position = 24
        game.board.spaces[24].used += 1

    @staticmethod
    def advance_to_charles_place(game, player):
        """Move the player to charles place"""
        player.position = 11
        game.board.spaces[11].used += 1

    @staticmethod
    def advance_to_nearest_utility(game, player):
        """Move the player to the nearest utility"""
        # Electric company is at 12
        # Water works is at 28
        if player.position < 12 or player.position >= 28:
            player.position = 12
        else:
            player.position = 28
        game.board.spaces[player.position].used += 1

    @staticmethod
    def advance_to_nearest_railroad(game, player):
        """Move the player to the railroad"""
        # Railroad are at 5, 15, 25, 35
        if player.position < 5 or player.position >= 35:
            player.position = 5
        elif player.position >= 5 or player.position < 15:
            player.position = 15
        elif player.position >= 15 or player.position < 25:
            player.position = 25
        elif player.position >= 25 or player.position < 35:
            player.position = 35
        game.board.spaces[player.position].used += 1

    @staticmethod
    def go_back_three_spaces(game, player):
        """Move the player 3 spaces back"""
        player.position -= 3
        game.board.spaces[player.position].used += 1

    @staticmethod
    def take_a_trip_to_reading_railroad(game, player):
        """Move the player to reading railroad"""
        player.position = 5
        game.board.spaces[player.position].used += 1

    @staticmethod
    def take_a_walk_on_the_boardwalk(game, player):
        """Move the player to broadwalk"""
        player.position = 39
        game.board.spaces[player.position].used += 1


# keys are spaces and values are actions to call.
actions_space = {30: Actions.go_to_jail, 7: Actions.draw_chance_card, 22: Actions.draw_chance_card,
                 36: Actions.draw_chance_card, 2: Actions.draw_community_card,
                 33: Actions.draw_community_card}


# Chance actions in order of chance cards texts
chance_actions = [
    Actions.advance_to_go,
    Actions.advance_to_illinois_ave,
    Actions.advance_to_charles_place,
    Actions.advance_to_nearest_utility,
    Actions.advance_to_nearest_railroad,
    Actions.advance_to_nearest_railroad,
    Actions.dummy,
    Actions.dummy,
    Actions.go_back_three_spaces,
    Actions.go_to_jail,
    Actions.dummy,
    Actions.dummy,
    Actions.take_a_trip_to_reading_railroad,
    Actions.take_a_walk_on_the_boardwalk,
    Actions.dummy,
    Actions.dummy
]

# Chance cards texts
chance_texts = [
    "Advance to Go (Collect $200) (Mr. M hops on both feet.)",
    "Advance to Illinois Ave. - If you pass Go, collect $200 {Second sentence omitted.} (Mr. M has tied a cloth bundle onto his cane to make a bindle, carried over his right shoulder, and is smoking a cigar)",
    "Advance to St. Charles Place – If you pass Go, collect $200 (Mr. M hurries along, hauling a little boy by the hand)",
    "Advance token to nearest Utility. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total ten times the amount thrown. (Mr. M trudges along with a huge battleship token on his back)",
    "Advance token to the nearest Railroad and pay owner twice the rental to which he/she {he} is otherwise entitled. If Railroad is unowned, you may buy it from the Bank. (There are two of these.) (At lower left, Mr. M carries a large flatiron token with two hands; at upper right a railroad crossing is seen)",
    "Advance token to the nearest Railroad and pay owner twice the rental to which he/she {he} is otherwise entitled. If Railroad is unowned, you may buy it from the Bank. (There are two of these.) (At lower left, Mr. M carries a large flatiron token with two hands; at upper right a railroad crossing is seen)",
    "Bank pays you dividend of $50 (With his feet up on a telephone-bearing desk, Mr. M leans back in an overstuffed chair, blowing cigar smoke rings)",
    "Get out of Jail Free – This card may be kept until needed, or traded/sold {This card may be kept until needed or sold - Get Out of Jail Free}{The first sentence is much smaller than the second} (Mr. M, in close-fitting one-piece prison stripes, is literally kicked out)",
    "Go Back 3 Spaces (Mr. M is hauled back by a cane hooked around his neck) {Presumably an allusion to amateur nights at theaters}",
    "Go to Jail – Go directly to Jail – Do not pass Go, do not collect $200 (A truncheon-carrying policeman in a dark-colored uniform hauls a surprised Mr M along by the feet)",
    """"Make general repairs on all your property – For each house pay $25 – For each hotel $100 (Consulting a "How to Fix It" brochure, a hammer-wielding Mr. M sits astride a house not much larger than he is; it buckles under his weight)""",
    "Pay poor tax of $15 (His trouser pockets pulled out to show them empty, Mr. M spreads his hands) (The video game version replaces this with Speeding fine $15, reportedly also in the UK version.)",
    "Take a trip to Reading Railroad {Take a ride on the Reading} – If you pass Go, collect $200 (Mr. M rides astride the TOOTing engine of a train)",
    "Take a walk on the Boardwalk – Advance token to Boardwalk. {Board Walk in both sentences} (Mr. M, a smallish dog hung over one arm, with the other pushes a squalling baby in a small pram; behind them, birds fly in the sky above a low fence)",
    "You have been elected Chairman of the Board – Pay each player $50 (A newsboy shouts an Extra with Mr. M's headshot on its front page)",
    """Your building {and} loan matures – Collect $150 {Up until the 1980s a "building and loan" was a financial institution.} (Mr. M joyfully embraces an apparent wife)""",
]

# Community cards texts
community_texts = [
    """Advance to Go (Collect $200) <Mr. M strides in 7-league boots>""",
    """Bank error in your favor – Collect $200 <Mr. M falls back in astonishment as an arm presents a sheaf of cash out of a bank teller's window>""",
    """Doctor's fees {fee} – Pay $50 <Mr. M angrily brandishes crutches as he stomps with a leg cast>""",
    """From sale of stock you get $50 {$45} <Mr. M, happily entangled in the tape of a stock ticker, waves cash (with no $ sign this time)>""",
    """Get Out of Jail Free {Get out of Jail, Free} – This card may be kept until needed or sold <A winged Mr. M flutters out of a bird cage>""",
    """Go to Jail – Go directly to jail – Do not pass Go – Do not collect $200 <A truncheon-wielding policeman in a light-colored uniform lifts a surprised Mr M by the collar>""",
    """Grand Opera Night {Opening} – Collect $50 from every player for opening night seats <A wall sign near steps reads "Opera Tonite - 8 PM Sharp"; Mr. M leans against it checking his pocket watch in annoyance>""",
    """Holiday {Xmas} Fund matures - Receive {Collect} $100 <Mr. M carries along a giant Xmas sock containing a sheaf of cash>""",
    """Income tax refund – Collect $20 <Mr M faints back against a man displaying the Refund paper>""",
    """Life insurance matures – Collect $100 <Below an I N S sign stands a bent Mr M, his long beard brushing the floor>""",
    """Pay hospital fees of $100 {Pay hospital $100} <A bored nurse holds out her hand for payment while Mr. M holds 2 swaddled infants, one in each arm>""",
    """Pay school fees {tax} of $150 <A bespectacled schoolboy unhappily receives a head pat and a dime ((Rockefeller style) from Mr. M.>""",
    """Receive $25 consultancy fee {Receive for services $25} <As Justice of the Peace, a stern Mr. M holds out his hand for fee from an embarrassed groom whose bride hold a bouquet behind him>""",
    """You are assessed for street repairs – $40 per house – $115 per hotel <Mr. M., supported by his near-ubiquitous cane in his left hand, holds a pick and shovel over his right shoulder>""",
    """You have won second prize in a beauty contest – Collect $10 <Mr. M preens with a sash and large bouquet>""",
    """You inherit $100 <Mr M. holds his head as unseen people's hands offer brochures titled "Buy Yacht", "World Tour", and "Rolls Royce"> """,
]

# Chance actions in order of chance cards texts
community_actions = [
    Actions.advance_to_go,
    Actions.dummy,
    Actions.dummy,
    Actions.dummy,
    Actions.dummy,
    Actions.go_to_jail,
    Actions.dummy,
    Actions.dummy,
    Actions.dummy,
    Actions.dummy,
    Actions.dummy,
    Actions.dummy,
    Actions.dummy,
    Actions.dummy,
    Actions.dummy,
    Actions.dummy,
]


class Board:
    """Represents the board."""
    def __init__(self, nb_turn=1):
        self.spaces = []
        for i in range(0, 40):
            new_space = Space(i)
            if i in actions_space:
                new_space.action = actions_space[i]
            new_space.nb_turn = nb_turn

            self.spaces.append(new_space)

    def __str__(self):
        return "\n".join(map(lambda x: str(x), self.spaces))


class Card:
    """Represents a card"""
    def __init__(self, text="", action=None):
        self.text = text
        self.action = action

    def __str__(self):
        return "Card: {}".format(self.text)


class Deck:
    """Represents a card deck"""
    def __init__(self):
        self.cards = []

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        card = self.cards.pop()
        self.cards.insert(0, card)
        return card


class Space:
    """Represents a space"""
    def __init__(self, index):
        self.index = index
        self.used = 0
        self.action = None
        self.nb_turn = 0

    @property
    def frequency(self):
        """This is wrongly implemented"""
        #FIXME can be used more than nb of turns due to chance card.
        return self.used / float(self.nb_turn)

    def __str__(self):
        return "Space:  used->{used} frequency->{frequency} index->{index} ".format(used=self.used,
                                                                                    index=self.index,
                                                                                    frequency=self.frequency)

    def __repr__(self):
        return "Space:  used->{used} frequency->{frequency} index->{index} ".format(used=self.used,
                                                                                    index=self.index,
                                                                                    frequency=self.frequency)


class Dice:
    """Represents Dice"""
    def __init__(self):
        pass

    def roll(self):
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        return d1 + d2, (d1, d2)


class Player:
    """Really simplified player."""
    def __init__(self):
        self.position = 0
        self.jailed = False


class Game:
    """Main class representing a game"""
    def __init__(self, player_count=1, nb_turns=1000):
        self.player_count = player_count
        self.board = Board(nb_turns)
        self.dices = Dice()
        self.players = [Player()] * self.player_count
        self.nb_turns = nb_turns
        self.turns_elapsed = 0
        self.chance_deck = Deck()
        for i, text in enumerate(chance_texts):
            self.chance_deck.cards.append(Card(text, chance_actions[i]))
        self.chance_deck.shuffle()
        self.community_deck = Deck()
        for i, text in enumerate(community_texts):
            self.community_deck.cards.append(Card(text, community_actions[i]))
        self.community_deck.shuffle()

    def simulate(self):
        """Launch the simulation"""
        for i in range(0, self.nb_turns):
            for player in self.players:
                sum, res = self.dices.roll()
                if player.jailed:
                    if res[0] == res[1]:
                        player.jailed = False
                        sum, res = self.dices.roll()
                    else:
                        continue
                player.position += sum
                if player.position > 39:
                    player.position -= 40
                current_player_space = self.board.spaces[player.position]
                current_player_space.used += 1
                if current_player_space.action:
                    current_player_space.action(self, player)

            self.turns_elapsed += 1


if __name__ == "__main__":
    """Execute the game and shows spaces information."""
    game = Game(6, 1000000)
    game.simulate()

    total = 0
    # Fix the frenquency problem for spaces by recomputing total number of move.
    for space in game.board.spaces:
        total += space.used

    for space in game.board.spaces:
        space.nb_turn = total

    print(game.board)

