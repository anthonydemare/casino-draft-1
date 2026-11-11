from drafter import *
from dataclasses import dataclass
from random import randint, shuffle, choice
from bakery import assert_equal
from itertools import combinations

set_website_title("DeMare Casino")
set_site_information(
    author="Anthony DeMare",
    description="Simulate Casino Games and Outcomes.",
    sources="",
    planning="ADeMare-Casino-Plan.pdf",
    links=["https://anthonydemare.github.io/casino-draft-1"]
)
#hide_debug_information()
set_website_framed(False)

'''
make other stuff look good with images and whatnot
'''

@dataclass
class Card:
    '''The number is the actual number value of the card
    the suit is the suit of the card
    '''
    number: int
    suit: str
    
'''
alternative pngs
card_images = {
    "ace_spades" : "https://www.dcode.fr/tools/playing-cards/images/pique_a.png",
    "two_spades" : "https://www.dcode.fr/tools/playing-cards/images/pique_2.png",
    "three_spades" : "https://www.dcode.fr/tools/playing-cards/images/pique_3.png",
    "four_spades" : "https://www.dcode.fr/tools/playing-cards/images/pique_4.png",
    "five_spades" : "https://www.dcode.fr/tools/playing-cards/images/pique_5.png",
    "six_spades" : "https://www.dcode.fr/tools/playing-cards/images/pique_6.png",
    "seven_spades" : "https://www.dcode.fr/tools/playing-cards/images/pique_7.png",
    "eight_spades" : "https://www.dcode.fr/tools/playing-cards/images/pique_8.png",
    "nine_spades" : "https://www.dcode.fr/tools/playing-cards/images/pique_9.png",
    "ten_spades" : "https://www.dcode.fr/tools/playing-cards/images/pique_10.png",
    "jack_spades" : "https://www.dcode.fr/tools/playing-cards/images/pique_v.png",
    "queen_spades" : "https://www.dcode.fr/tools/playing-cards/images/pique_d.png",
    "king_spades" : "https://www.dcode.fr/tools/playing-cards/images/pique_r.png",
    "ace_hearts" : "https://www.dcode.fr/tools/playing-cards/images/coeur_a.png",
    "two_hearts" : "https://www.dcode.fr/tools/playing-cards/images/coeur_2.png",
    "three_hearts" : "https://www.dcode.fr/tools/playing-cards/images/coeur_3.png",
    "four_hearts" : "https://www.dcode.fr/tools/playing-cards/images/coeur_4.png",
    "five_hearts" : "https://www.dcode.fr/tools/playing-cards/images/coeur_5.png",
    "six_hearts" : "https://www.dcode.fr/tools/playing-cards/images/coeur_6.png",
    "seven_hearts" : "https://www.dcode.fr/tools/playing-cards/images/coeur_7.png",
    "eight_hearts" : "https://www.dcode.fr/tools/playing-cards/images/coeur_8.png",
    "nine_hearts" : "https://www.dcode.fr/tools/playing-cards/images/coeur_9.png",
    "ten_hearts" : "https://www.dcode.fr/tools/playing-cards/images/coeur_10.png",
    "jack_hearts" : "https://www.dcode.fr/tools/playing-cards/images/coeur_v.png",
    "queen_hearts" : "https://www.dcode.fr/tools/playing-cards/images/coeur_d.png",
    "king_hearts" : "https://www.dcode.fr/tools/playing-cards/images/coeur_r.png",
    "ace_clubs" : "https://www.dcode.fr/tools/playing-cards/images/trefle_a.png",
    "two_clubs" : "https://www.dcode.fr/tools/playing-cards/images/trefle_2.png",
    "three_clubs" : "https://www.dcode.fr/tools/playing-cards/images/trefle_3.png",
    "four_clubs" : "https://www.dcode.fr/tools/playing-cards/images/trefle_4.png",
    "five_clubs" : "https://www.dcode.fr/tools/playing-cards/images/trefle_5.png",
    "six_clubs" : "https://www.dcode.fr/tools/playing-cards/images/trefle_6.png",
    "seven_clubs" : "https://www.dcode.fr/tools/playing-cards/images/trefle_7.png",
    "eight_clubs" : "https://www.dcode.fr/tools/playing-cards/images/trefle_8.png",
    "nine_clubs" : "https://www.dcode.fr/tools/playing-cards/images/trefle_9.png",
    "ten_clubs" : "https://www.dcode.fr/tools/playing-cards/images/trefle_10.png",
    "jack_clubs" : "https://www.dcode.fr/tools/playing-cards/images/trefle_v.png",
    "queen_clubs" : "https://www.dcode.fr/tools/playing-cards/images/trefle_d.png",
    "king_clubs" : "https://www.dcode.fr/tools/playing-cards/images/trefle_r.png",
    "ace_diamonds" : "https://www.dcode.fr/tools/playing-cards/images/carreau_a.png",
    "two_diamonds" : "https://www.dcode.fr/tools/playing-cards/images/carreau_2.png",
    "three_diamonds" : "https://www.dcode.fr/tools/playing-cards/images/carreau_3.png",
    "four_diamonds" : "https://www.dcode.fr/tools/playing-cards/images/carreau_4.png",
    "five_diamonds" : "https://www.dcode.fr/tools/playing-cards/images/carreau_5.png",
    "six_diamonds" : "https://www.dcode.fr/tools/playing-cards/images/carreau_6.png",
    "seven_diamonds" : "https://www.dcode.fr/tools/playing-cards/images/carreau_7.png",
    "eight_diamonds" : "https://www.dcode.fr/tools/playing-cards/images/carreau_8.png",
    "nine_diamonds" : "https://www.dcode.fr/tools/playing-cards/images/carreau_9.png",
    "ten_diamonds" : "https://www.dcode.fr/tools/playing-cards/images/carreau_10.png",
    "jack_diamonds" : "https://www.dcode.fr/tools/playing-cards/images/carreau_v.png",
    "queen_diamonds" : "https://www.dcode.fr/tools/playing-cards/images/carreau_d.png",
    "king_diamonds" : "https://www.dcode.fr/tools/playing-cards/images/carreau_r.png",
    }
'''

card_images = {
    "ace_spades" : "https://i.postimg.cc/BLqV64YH/ace-of-spades.png",
    "two_spades" : "https://i.postimg.cc/ZBTMR47v/2-of-spades.png",
    "three_spades" : "https://i.postimg.cc/sQVNXs6W/3-of-spades.png",
    "four_spades" : "https://i.postimg.cc/7GxW6wsG/4-of-spades.png",
    "five_spades" : "https://i.postimg.cc/PptRxT3L/5-of-spades.png",
    "six_spades" : "https://i.postimg.cc/9RWnMC8z/6-of-spades.png",
    "seven_spades" : "https://i.postimg.cc/34KcRYSN/7-of-spades.png",
    "eight_spades" : "https://i.postimg.cc/R6MDF4sF/8-of-spades.png",
    "nine_spades" : "https://i.postimg.cc/8FdYNjHM/9-of-spades.png",
    "ten_spades" : "https://i.postimg.cc/MMWFTqPG/10-of-spades.png",
    "jack_spades" : "https://i.postimg.cc/1g1dkppx/jack-of-spades2.png",
    "queen_spades" : "https://i.postimg.cc/1g1dkpDY/queen-of-spades2.png",
    "king_spades" : "https://i.postimg.cc/Y4BP51QP/king-of-spades2.png",
    "ace_hearts" : "https://i.postimg.cc/KK7WxRN8/ace-of-hearts.png",
    "two_hearts" : "https://i.postimg.cc/xkGZncRV/2-of-hearts.png",
    "three_hearts" : "https://i.postimg.cc/sBPLsvcR/3-of-hearts.png",
    "four_hearts" : "https://i.postimg.cc/3yjqYdBT/4-of-hearts.png",
    "five_hearts" : "https://i.postimg.cc/mc3nBtwR/5-of-hearts.png",
    "six_hearts" : "https://i.postimg.cc/PLb7TP4T/6-of-hearts.png",
    "seven_hearts" : "https://i.postimg.cc/p9QSRpZP/7-of-hearts.png",
    "eight_hearts" : "https://i.postimg.cc/WDmyThnN/8-of-hearts.png",
    "nine_hearts" : "https://i.postimg.cc/PLb7TP4f/9-of-hearts.png",
    "ten_hearts" : "https://i.postimg.cc/3yjqYdBJ/10-of-hearts.png",
    "jack_hearts" : "https://i.postimg.cc/qtHFP88d/jack-of-hearts2.png",
    "queen_hearts" : "https://i.postimg.cc/SXbPBWcD/queen-of-hearts2.png",
    "king_hearts" : "https://i.postimg.cc/XZ6PRw9T/king-of-hearts2.png",
    "ace_clubs" : "https://i.postimg.cc/Z9PQ4Cc3/ace-of-clubs.png",
    "two_clubs" : "https://i.postimg.cc/Tyjsfp9P/2-of-clubs.png",
    "three_clubs" : "https://i.postimg.cc/yJhGskPW/3-of-clubs.png",
    "four_clubs" : "https://i.postimg.cc/gwy7mnDn/4-of-clubs.png",
    "five_clubs" : "https://i.postimg.cc/DWQNn8gW/5-of-clubs.png",
    "six_clubs" : "https://i.postimg.cc/PLb7TP4p/6-of-clubs.png",
    "seven_clubs" : "https://i.postimg.cc/06G4PbfJ/7-of-clubs.png",
    "eight_clubs" : "https://i.postimg.cc/v17Kbczx/8-of-clubs.png",
    "nine_clubs" : "https://i.postimg.cc/v17Kbczn/9-of-clubs.png",
    "ten_clubs" : "https://i.postimg.cc/d7RfwLBy/10-of-clubs.png",
    "jack_clubs" : "https://i.postimg.cc/zLYQsnn5/jack-of-clubs2.png",
    "queen_clubs" : "https://i.postimg.cc/SXbPBWc3/queen-of-clubs2.png",
    "king_clubs" : "https://i.postimg.cc/mcWnvQQf/king-of-clubs2.png",
    "ace_diamonds" : "https://i.postimg.cc/HJ0NdV2D/ace-of-diamonds.png",
    "two_diamonds" : "https://i.postimg.cc/hJ8Ycf0k/2-of-diamonds.png",
    "three_diamonds" : "https://i.postimg.cc/qtcF4zGS/3-of-diamonds.png",
    "four_diamonds" : "https://i.postimg.cc/B85z4XgW/4-of-diamonds.png",
    "five_diamonds" : "https://i.postimg.cc/d7RfwL9g/5-of-diamonds.png",
    "six_diamonds" : "https://i.postimg.cc/SXLPkJGw/6-of-diamonds.png",
    "seven_diamonds" : "https://i.postimg.cc/jW61tLh9/7-of-diamonds.png",
    "eight_diamonds" : "https://i.postimg.cc/CZp23jjw/8-of-diamonds.png",
    "nine_diamonds" : "https://i.postimg.cc/LqFWczz2/9-of-diamonds.png",
    "ten_diamonds" : "https://i.postimg.cc/67xPkddX/10-of-diamonds.png",
    "jack_diamonds" : "https://i.postimg.cc/HJ1NqQQm/jack-of-diamonds2.png",
    "queen_diamonds" : "https://i.postimg.cc/nsfWyvqS/queen-of-diamonds2.png",
    "king_diamonds" : "https://i.postimg.cc/yJCGMF0M/king-of-diamonds2.png"
    }

def card_to_image(card: Card) -> str:
    '''converts a card to an image link
    this image link can be added to drafter
    '''
    card_index = ""
    card_index = card_index + "_" + card.suit
    if card.number == 2:
        card_index = "two" + card_index
    if card.number == 3:
        card_index = "three" + card_index
    if card.number == 4:
        card_index = "four" + card_index
    if card.number == 5:
        card_index = "five" + card_index
    if card.number == 6:
        card_index = "six" + card_index
    if card.number == 7:
        card_index = "seven" + card_index
    if card.number == 8:
        card_index = "eight" + card_index
    if card.number == 9:
        card_index = "nine" + card_index
    if card.number == 10:
        card_index = "ten" + card_index
    if card.number == 11:
        card_index = "jack" + card_index
    if card.number == 12:
        card_index = "queen" + card_index
    if card.number == 13:
        card_index = "king" + card_index
    if card.number == 14:
        card_index = "ace" + card_index
    link = {card_images[card_index]}
    return link

@dataclass
class Player:
    '''the name is a string representing the name of the player
    cards is a list of cards the player has
    hand_rank is the rank of the hand they have (flush, straight, etc.)
    result is whether the player won or lost
    chips is the amount of chips the player currently has
    bet is the current bet that the player is placing
    folded is whether the player has folded in the current game
    all_in is whther the player has gone all in in the current game
    is_human is just "is it the person playing the game?"
    '''
    name: str
    cards: list[Card]
    hand_rank: str
    result: str
    is_human: bool = False
    
@dataclass
class State:
    game_type: str #type of game played
    player_name: str #name of player
    players: list[Player] #list of players playing
    community_cards: list[Card] #list of cards on table
    dealer_cards: list[Card] #list of cards dealer has (blackjack)
    deck: list[Card] #cards left in deck
    player_count: int #number of players
    current_round: str #what round number we are on
    message: str #the message portrayed on screen
    game_over: bool #is the game completed?
    roulette_number: int #number on roulette
    roulette_bet: str #betted number on roulette
    bet_type: str #type of roulette bet (red,number,odd?)
    community_stage: int #how many cards on the table for Texas Hold'em

def card_value(card: Card) -> int:
    '''Return a card's value in Blackjack.
    Aces are 11 (or 1, defined later)
    Face cards are ten
    '''
    if card.number == 14:
        return 11
    elif card.number >= 11:
        return 10
    else:
        return card.number

def hand_value(cards: list[Card]) -> int:
    '''Calculate a Blackjack hand's value
    treats aces as 1 when needed
    '''
    total = 0
    aces = 0 #number of aces 
    for card in cards: #finds total aces
        total += card_value(card)
        if card.number == 14:
            aces += 1
    while total > 21 and aces > 0: #uses an ace to reduce total
        total -= 10 #reduces score
        aces -= 1 #"uses" and ace
    return total

def evaluate_three_card_hand(cards: list[Card]) -> tuple[tuple[int, ...], str]:
    '''Rank a three-card poker hand and return its score
    ex output: ((4,10), "three of a kind)
    '''
    numbers = [card.number for card in cards]
    #^^ rank of cards in a list ^^
    counts = {}
    for number in numbers: #tracks how many times each number appears
        counts[number] = counts.get(number, 0) + 1
        #retrieves count, and if no count gets 0, +1 increases
    groups = sorted(
        counts,
        key=lambda number: (counts[number], number),
        reverse=True)
    '''the code above is lambda calculus (got bored and learned it)
    essentially it's math for programmers
    the "key" section redefines the sorting function
    lambda is like a placeholder
    number: (counts... defines the sorted objects
    python sorts by the first object, being frequency
    finally, "reverse=True" sorts in descending order
    so counts = {5:1,10:2} would become [10,5]
    the "groups" definition sorts by frequency
    '''
    flush = all(
        card.suit == cards[0].suit
        for card in cards)
        #checks for flushes
    unique_numbers = sorted(set(numbers))
    '''"set" removes duplicates, sorted sorts what's left
    '''
    straight_high = 0
    #checks for a straight
    if len(unique_numbers) == 3:
        if unique_numbers[2] - unique_numbers[0] == 2:
            straight_high = unique_numbers[2]
        elif unique_numbers == [2, 3, 14]:
            straight_high = 3
        elif unique_numbers == [12, 13, 14]:
            straight_high = 14
    '''above checks for straights
    with "straight_high" storing the current highest value
    The three possibilities are ace low, ace high, or other
    basically, checks if the highest and lowest are two apart
    or aces, because they wanna be difficult...
    straight_high remains 0 if no straights
    '''
    if flush and straight_high:
        return (5, straight_high), "Straight Flush"
    if counts[groups[0]] == 3:
        return (4, groups[0]), "Three of a Kind"
    if straight_high:
        return (3, straight_high), "Straight"
    if flush:
        return ((2,) + tuple(sorted(numbers, reverse=True)),"Flush")
    '''above just returns the type by categorization
    for flush, it also returns the cards since:
        ties are settled by highest card
    turns out "+" can connect tuples :)
    '''
    if counts[groups[0]] == 2: #checks if most frequent is pair
        pair = groups[0]
        kicker = next(n for n in numbers if n != pair)
        #kicker is just the tie breaker
        #ex: 2,2,10 vs 2,2,3 goes to first player
        return (1, pair, kicker), "One Pair"
    #all that's left is high card, below
    return ((0,) + tuple(sorted(numbers, reverse=True)),"High Card")

def best_texas_hand(
    player_cards: list[Card],
    community_cards: list[Card]
) -> tuple[int, str]:
    '''Find the best five-card poker hand from seven available cards.'''
    all_cards = player_cards + community_cards #defines all cards
    best_score = None
    best_rank = ""

    for hand in combinations(all_cards, 5):
        '''the combination function is so good!
        this creates all five card combinations
        then it determines the score andd rank
        uses a helper function
        finally, redefines functions
        '''
        score, rank = evaluate_hand(list(hand))
        if best_score is None or score > best_score:
            best_score = score
            best_rank = rank

    return best_score, best_rank

#start defining routes here
@route
def index(state: State) -> Page:
    '''Display the casino home page.'''
    return Page(state, [
        Header("WELCOME TO THE DEMARE CASINO\n"),
        "Choose a game to play.\n",
        Button("Texas Hold'em", "setup_texas"),
        Button("Blackjack", "setup_blackjack"),
        Button("Three-Card Poker", "setup_three_card"),
        Button("Five-Card Poker", "setup_five_card"),
        Button("Roulette", "setup_roulette")
    ])

'''the routes below change state.game_type
then it returns the setup function with the game_type
'''
@route
def setup_texas(state: State) -> Page:
    '''Set up a Texas Hold'em game.'''
    state.game_type = "Texas Hold'em"
    return setup(state)

@route
def setup_blackjack(state: State) -> Page:
    '''Set up a blackjack game.'''
    state.game_type = "Blackjack"
    return setup(state)

@route
def setup_three_card(state: State) -> Page:
    '''Set up a three-card poker game.'''
    state.game_type = "Three-Card Poker"
    return setup(state)

@route
def setup_five_card(state: State) -> Page:
    '''Set up a five-card poker game.'''
    state.game_type = "Five-Card Poker"
    return setup(state)

@route
def setup_roulette(state: State) -> Page:
    '''Set up a roulette game.'''
    state.game_type = "Roulette"
    return setup(state)

@route
def setup(state: State) -> Page:
    '''Display the setup page for the selected game.'''
    content = [
        "Let's set this thing up for you.\n",
        "Selected game: " + state.game_type,
        "\n",
        "Enter your name:",
        TextBox("player_name"),
        "\n"
    ]

    #not all games are multiplayer, so filter what's needed
    if state.game_type in [
        "Texas Hold'em",
        "Three-Card Poker",
        "Five-Card Poker"
    ]:
        content.extend([ #up to six players, default 2
            "Choose the number of players:",
            SelectBox("player_count", ["1","2","3","4","5","6"],"2"),
            "\n"
        ])
    '''below added after dropdown
    even if it isn't there
    (since you need to start the game at some point...)
    '''
    content.extend([
        Button("Start Game", "start_game"),
        Button("Return to Casino", "index")
    ])

    return Page(state, content)

@route
def start_game(
    state: State,
    player_name: str,
    player_count: int = 1
) -> Page:
    '''Save the setup choices and prepare the selected game.'''
    state.player_name = player_name.strip()
    if state.player_name == "":
        state.player_name = "Player"
    if player_count < 1:
        player_count = 1
    elif player_count > 6:
        player_count = 6
    #changes the necessary aspects of State
    state.player_count = player_count
    state.players = []
    state.community_cards = []
    state.deck = []
    state.current_round = "Starting"
    state.game_over = False
    state.message = "Game setup complete."

    return Page(state, [
        "You know what time it is??? GAME TIME!!!\n",
        "*insert cool music and awesome colors...*\n",
        "Player: " + state.player_name,
        "\n",
        "Selected game: " + state.game_type,
        "\n",
        "Number of players: " + str(state.player_count),
        "\n",
        state.message,
        "\n",
        Button("Continue", "play_game"),
        Button("Return to Casino", "index")
    ])

@route
def play_game(state: State) -> Page:
    '''Direct the player to the selected game.'''
    if state.game_type == "Roulette":
        return roulette(state)
    elif state.game_type == "Five-Card Poker":
        return five_card_poker(state)
    elif state.game_type == "Three-Card Poker":
        return three_card_poker(state)
    elif state.game_type == "Blackjack":
        return blackjack(state)
    elif state.game_type == "Texas Hold'em":
        return texas_holdem(state)
    return Page(state, [ #just in case something went wrong
        state.game_type,
        "This game has not been implemented yet.",
        Button("Return to Casino", "index")
    ])

def format_card(card: Card) -> str:
    '''Convert a card into readable text.'''
    number_names = {
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "jack",
        12: "queen",
        13: "king",
        14: "ace"
        }
    if card.number in number_names:
        number = number_names[card.number]
    else:
        number = str(card.number)
    return number + "_" + card.suit

def evaluate_hand(cards: list[Card]) -> tuple[tuple[int, ...], str]:
    '''Returns a poker hand's score and readable ranking.'''
    numbers = [card.number for card in cards]
    counts = {}
    for number in numbers: #counts the number of each rank
        counts[number] = counts.get(number, 0) + 1
    groups = sorted(#sorts by descending order of amount
        counts,
        key=lambda number:(counts[number], number),
        reverse=True)
    '''this does the exact same stuff as the other one
    for three card hands, just check that
    it does add two pair, 4 of a kind, and others
    '''
    flush = all(card.suit == cards[0].suit for card in cards)
    unique_numbers = sorted(set(numbers))
    if 14 in unique_numbers:
        unique_numbers.insert(0, 1)
    straight_high = 0
    for i in range(len(unique_numbers) - 4):
        sequence = unique_numbers[i:i + 5]
        if sequence[-1] - sequence[0] == 4:
            straight_high = sequence[-1]
    if flush and straight_high == 14:
        return (9,), "Royal Flush"
    if flush and straight_high:
        return (8, straight_high), "Straight Flush"
    if counts[groups[0]] == 4:
        return ((7, groups[0], groups[1]),"Four of a Kind")
    if counts[groups[0]] == 3 and counts[groups[1]] == 2:
        return ((6, groups[0], groups[1]),"Full House")
    if flush:
        return ((5,) + tuple(sorted(numbers, reverse=True)),"Flush")
    if straight_high:
        return (4, straight_high), "Straight"
    if counts[groups[0]] == 3:
        kickers = sorted(
            [n for n in numbers if n != groups[0]],
            reverse=True
        )
        return ((3, groups[0]) + tuple(kickers),"Three of a Kind")
    pairs = sorted(
        [n for n in counts if counts[n] == 2],
        reverse=True)
    if len(pairs) == 2:
        kicker = max(n for n in numbers if n not in pairs)
        return ((2, pairs[0], pairs[1], kicker),"Two Pair")
    if len(pairs) == 1:
        kickers = sorted(
            [n for n in numbers if n != pairs[0]],
            reverse=True)
        return ((1, pairs[0]) + tuple(kickers),"One Pair")
    return ((0,) + tuple(sorted(numbers, reverse=True)),"High Card")

#testing functions
assert_equal(
    evaluate_hand([
        Card(10, "Hearts"),
        Card(11, "Hearts"),
        Card(12, "Hearts"),
        Card(13, "Hearts"),
        Card(14, "Hearts")
    ])[1],
    "Royal Flush")

assert_equal(
    evaluate_hand([
        Card(8, "Hearts"),
        Card(8, "Clubs"),
        Card(8, "Spades"),
        Card(5, "Diamonds"),
        Card(2, "Hearts")
    ])[1],
    "Three of a Kind")

assert_equal(
    evaluate_hand([
        Card(2, "Hearts"),
        Card(4, "Clubs"),
        Card(7, "Spades"),
        Card(9, "Diamonds"),
        Card(13, "Hearts")
    ])[1],
    "High Card")

assert_equal(
    evaluate_three_card_hand([
        Card(10, "Hearts"),
        Card(11, "Hearts"),
        Card(12, "Hearts")
    ])[1],
    "Straight Flush")

assert_equal(
    evaluate_three_card_hand([
        Card(7, "Hearts"),
        Card(7, "Clubs"),
        Card(7, "Spades")
    ])[1],
    "Three of a Kind")

assert_equal(
    evaluate_three_card_hand([
        Card(2, "Hearts"),
        Card(3, "Clubs"),
        Card(4, "Spades")
    ])[1],
    "Straight")

#defining the routes for various things
@route
def five_card_poker(state: State) -> Page:
    '''Deal cards, evaluate hands, and display the winner.'''
    #Create a standard 52-card deck using four suits and values 2-14.
    #Values 11-14 represent Jack, Queen, King, and Ace.
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    state.deck = []
    for suit in suits:
        for number in range(2, 15):
            state.deck.append(Card(number, suit))

    #Randomize the order of the cards before dealing.
    shuffle(state.deck)
    #Clear the previous players before starting a new hand.
    state.players = []
    
    #Deal five cards to each player.
    for i in range(state.player_count):
        #Use the entered name for the first player.
        #Give all other players a default name.
        if i == 0:
            name = state.player_name
        else:
            name = "Player " + str(i + 1)
        #Create an empty hand for the current player.
        cards = []
        #Remove five cards from the deck and add them to the player's hand.
        for j in range(5):
            cards.append(state.deck.pop())
        #Create the player with their name, cards, and empty result information.
        state.players.append(Player(name, cards, "", ""))
    #Store each player's hand evaluation and numerical score.
    evaluations = []
    for player in state.players:
        #Evaluate the player's hand to determine its score and ranking.
        score, ranking = evaluate_hand(player.cards)
        #Save the hand's ranking in the player's information.
        player.hand_rank = ranking
        #Store the player and their score together.
        evaluations.append((player, score))

    #Find the highest score among all players.
    best_score = max(entry[1] for entry in evaluations)
    #Collect the names of every player with the highest score.
    #This allows multiple players to win in the event of a tie.
    winners = [
        entry[0].name
        for entry in evaluations
        if entry[1] == best_score
    ]

    #Assign each player a result based on whether they won.
    for player in state.players:
        if player.name in winners:
            player.result = "Winner"
        else:
            player.result = "Lost"

    #Update the game state to indicate the current game and its completion.
    state.current_round = "Five-Card Poker"
    state.game_over = True

    #Create the appropriate message depending on the number of winners.
    if len(winners) == 1:
        state.message = winners[0] + " wins!"
    else:
        state.message = "Tie between " + ", ".join(winners) + "!"

    #Create a list containing the text and information displayed on the results page.
    content = [
        "FIVE-CARD POKER RESULTS\n",
        state.message,
        "\n"
    ]

    #Display each player's name, cards, hand ranking, and result.
    for player in state.players:

        #Display the player's name above their hand.
        content.append(player.name + "'s hand:\n")

        #Format and display each card in the player's hand.
        for card in player.cards:
            content.append(Image(card_images[format_card(Card(card.number,card.suit.lower()))],width=200))
        content.append("\n")
        #Display the ranking of the player's hand.
        content.append("Hand ranking: " + player.hand_rank + "\n")

        #Display whether the player won or lost.
        content.append("Result: " + player.result + "\n\n")

    #Add buttons allowing the user to deal another hand or return to the casino.
    content.extend([
        Button("Deal New Hand", "five_card_poker"),
        Button("Return to Casino", "index")
    ])

    #Return the completed results page.
    return Page(state, content)

@route
def three_card_poker(state: State) -> Page:
    '''Deal three cards to each player and compare hands.'''
    #Create a standard 52-card deck using four suits and values 2-14.
    #Values 11-14 represent Jack, Queen, King, and Ace.
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    state.deck = []

    for suit in suits:
        for number in range(2, 15):
            state.deck.append(Card(number, suit))
    #Randomize the order of the cards before dealing.
    shuffle(state.deck)
    #Clear the previous players before starting a new hand.
    state.players = []
    #Deal three cards to each player.
    for i in range(state.player_count):
        #Use the entered name for the first player.
        #Give all other players a default name.
        if i == 0:
            name = state.player_name
        else:
            name = "Player " + str(i + 1)
        #Create an empty hand for the current player.
        cards = []
        #Remove three cards from the deck and add them to the player's hand.
        for j in range(3):
            cards.append(state.deck.pop())
        #Create the player with their name, cards, and empty result information.
        state.players.append(Player(name, cards, "", ""))
    #Store each player's hand evaluation and numerical score.
    evaluations = []
    for player in state.players:
        #Evaluate the player's three-card hand to determine its score and ranking.
        score, ranking = evaluate_three_card_hand(
            player.cards
        )
        #Save the hand's ranking in the player's information.
        player.hand_rank = ranking
        #Store the player and their score together.
        evaluations.append((player, score))
    #Find the highest score among all players.
    best_score = max(entry[1] for entry in evaluations)
    #Collect the names of every player with the highest score.
    #This allows multiple players to win in the event of a tie.
    winners = [
        entry[0].name
        for entry in evaluations
        if entry[1] == best_score
    ]
    #Assign each player a result based on whether they won.
    for player in state.players:
        if player.name in winners:
            player.result = "Winner"
        else:
            player.result = "Lost"
    #Update the game state to indicate the current game and its completion.
    state.current_round = "Three-Card Poker"
    state.game_over = True
    #Create the appropriate message depending on the number of winners.
    if len(winners) == 1:
        state.message = winners[0] + " wins!"
    else:
        state.message = "Tie between " + ", ".join(winners) + "!"
    #Create a list containing the text and information displayed on the results page.
    content = [
        "THREE-CARD POKER RESULTS\n",
        state.message,
        "\n"
    ]
    #Display each player's name, cards, hand ranking, and result.
    for player in state.players:
        #Display the player's name above their hand.
        content.append(player.name + "'s hand:\n")
        #Format and display each card in the player's hand.
        for card in player.cards:
            content.append(Image(card_images[format_card(Card(card.number,card.suit.lower()))],width=200))
        content.append("\n")
        #Display the ranking of the player's hand.
        content.append("Hand ranking: " + player.hand_rank)
        content.append("\n")
        #Display whether the player won or lost.
        content.append("Result: " + player.result)
        content.append("\n\n")
    #Add buttons allowing the user to deal another hand or return to the casino.
    content.extend([
        Button("Deal New Hand", "three_card_poker"),
        Button("Return to Casino", "index")
    ])
    #Return the completed results page.
    return Page(state, content)

@route
def blackjack(state: State) -> Page:
    '''Start a Blackjack round and deal two cards to the player and dealer.'''
    #Create a standard 52-card deck using four suits and values 2-14.
    state.deck = [
        Card(number, suit)
        for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]
        for number in range(2, 15)
    ]
    #Randomize the order of the cards.
    shuffle(state.deck)
    #Deal two cards to the player and two cards to the dealer.
    player_cards = [state.deck.pop(), state.deck.pop()]
    state.dealer_cards = [state.deck.pop(), state.deck.pop()]
    #Create the player using the entered name and their two cards.
    state.players = [
        Player(state.player_name, player_cards, "", "")
    ]
    #Set the current game and indicate that the round is still active.
    state.current_round = "Blackjack"
    state.game_over = False
    #Clear any previous messages from the last round.
    state.message = ""
    #Display the Blackjack game page.
    return blackjack_page(state)

@route
def blackjack_page(state: State) -> Page:
    '''Display the current Blackjack hand and available actions.'''
    #Retrieve the player from the list of players.
    player = state.players[0]
    #Display the player's name, cards, and current hand total.
    content = [
        Header("Blackjack"),
        Text(f"{player.name}'s hand:"),
        "\n"]
    
    for card in player.cards:
        content.append(Image(card_images[format_card(Card(card.number,card.suit.lower()))],width=200))
        
    content.extend(["\n",
    Text(f"Your total: {hand_value(player.cards)}"),
    "\n"
    ])
    
    #If the game is over, display the dealer's complete hand and final results.
    if state.game_over:
        content.append("\n\n")
        content.append(Text("Dealer's hand:"))
        content.append("\n")
        #Display all of the dealer's cards.
        for card in state.dealer_cards:
            content.append(Image(card_images[format_card(Card(card.number,card.suit.lower()))],width=200))
        content.append("\n")
        #Display the dealer's final hand total.
        content.append(Text(f"Dealer total: {hand_value(state.dealer_cards)}"))
        content.append("\n")
        #Display the final result message.
        content.append(Text(state.message))
        content.append("\n")
        #Add buttons to start another round or return to the casino.
        content.append(Button("Play Again", blackjack))
        content.append(Button("Return to Casino", index))
    else:
        #If the game is still active, only show the dealer's first card.
        content.append("\n\n")
        content.append(Text("Dealer's visible card:"))
        content.append("\n")
        content.append(Image(card_images[format_card(Card(state.dealer_cards[0].number,state.dealer_cards[0].suit.lower()))],width=200))
        content.append("\n")
        #Indicate that the dealer's second card is hidden.
        content.append(Text("Dealer's second card is hidden."))
        content.append("\n")
        #If the player's total is already 21, only allow them to stand.
        if hand_value(player.cards) == 21:
            content.append(Button("Stand", blackjack_stand))
        else:
            #Allow the player to draw another card or end their turn.
            content.append(Button("Hit", blackjack_hit))
            content.append(Button("Stand", blackjack_stand))
        #Allow the player to leave the game and return to the casino.
        content.append(Button("Return to Casino", index))
    #Return the completed Blackjack page.
    return Page(state, content)

@route
def blackjack_hit(state: State) -> Page:
    '''Give the player one card and check for a bust.'''
    #Only allow the player to draw another card while the game is active.
    if not state.game_over:
        #Draw one card from the deck and add it to the player's hand.
        state.players[0].cards.append(state.deck.pop())
        #Check whether the player's total exceeds 21.
        if hand_value(state.players[0].cards) > 21:
            #Mark the player's result as a bust.
            state.players[0].result = "Bust"
            #Display the bust message and end the round.
            state.message = "You busted! The dealer wins."
            state.game_over = True
    #Refresh the page to display the updated hand and game status.
    return blackjack_page(state)

@route
def blackjack_stand(state: State) -> Page:
    '''Finish the player's turn and let the dealer draw.'''
    #Retrieve the player and calculate their final hand total.
    player = state.players[0]
    player_total = hand_value(player.cards)
    #The dealer must continue drawing cards while their total is below 17.
    while hand_value(state.dealer_cards) < 17:
        state.dealer_cards.append(state.deck.pop())
    #Calculate the dealer's final hand total after drawing.
    dealer_total = hand_value(state.dealer_cards)
    #Compare the player's and dealer's totals to determine the winner.
    if dealer_total > 21:
        #The dealer busted, so the player wins.
        player.result = "Winner"
        state.message = "The dealer busted. You win!"
    elif player_total > dealer_total:
        #The player's total is higher, so the player wins.
        player.result = "Winner"
        state.message = "Your total is higher. You win!"
    elif player_total == dealer_total:
        #Both totals are equal, resulting in a tie.
        player.result = "Push"
        state.message = "It's a tie!"
    else:
        #The dealer's total is higher, so the player loses.
        player.result = "Lost"
        state.message = "The dealer wins!"
    #Mark the round as finished.
    state.game_over = True
    #Refresh the page to display both hands and the final result.
    return blackjack_page(state)

@route
def texas_holdem(state: State) -> Page:
    '''Deal private cards and prepare the five community cards.'''
    state.deck = [
        Card(number, suit)
        for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]
        for number in range(2, 15)
    ]
    shuffle(state.deck)
    state.players = []
    #Deal two private cards to each player.
    for number in range(state.player_count):
        if number == 0:
            player_name = state.player_name
        else:
            player_name = f"Opponent {number}"

        player = Player(player_name, [], "", "")
        player.cards = [
            state.deck.pop(),
            state.deck.pop()
        ]
        state.players.append(player)
    #Prepare the five community cards.
    state.community_cards = [
        state.deck.pop() for _ in range(5)
    ]
    state.community_stage = 0
    state.current_round = "Pre-Flop"
    state.game_over = False
    state.message = "Your cards have been dealt!"
    return texas_holdem_page(state)

@route
def texas_holdem_page(state: State) -> Page:
    '''Display private cards and revealed community cards.'''
    content = [
        Header("Texas Hold'em"),
        Text(state.message),
        Header("Players")
    ]
    #Display each player's private cards.
    for player in state.players:
        content.append(player.name)
        if player == state.players[0]:
            content.append(":\n")
            for card in player.cards:
                content.append(Image(card_images[format_card(Card(card.number,card.suit.lower()))],width=200))
        content.append("\n")
    content.append(Header("Community Cards"))
    if state.community_stage == 0:
        content.append(Text("No community cards revealed yet."))
    else:
        visible_cards = state.community_cards[:state.community_stage]
        for card in visible_cards:
            content.append(Image(card_images[format_card(Card(card.number,card.suit.lower()))],width=200))
    content.append("\n")
    #Allow the player to reveal the next community cards.
    if not state.game_over:
        content.append(
            Button("Reveal Next Cards", reveal_community_cards)
        )
    content.append(Button("Return to Casino", index))
    return Page(state, content)

@route
def reveal_community_cards(state: State) -> Page:
    '''Reveal the flop, turn, and river.'''
    if state.community_stage == 0:
        state.community_stage = 3
        state.current_round = "Flop"
        state.message = "The flop has been revealed!"
    elif state.community_stage == 3:
        state.community_stage = 4
        state.current_round = "Turn"
        state.message = "The turn has been revealed!"
    elif state.community_stage == 4:
        state.community_stage = 5
        state.current_round = "River"
        state.message = "The river has been revealed!"
    if state.community_stage == 5:
        return finish_texas_holdem(state)
    return texas_holdem_page(state)

@route
def roulette(state: State) -> Page:
    '''Display the roulette betting page.'''
    #Display the roulette title and welcome message.
    return Page(state, [
        "ROULETTE\n",
        "Welcome, " + state.player_name + "!\n\n",
        #Ask the player to select a type of bet.
        "Choose your type of bet:",
        SelectBox(
            "bet_type",
            ["Number", "Red", "Black", "Odd", "Even"],
            "Number"
        ),
        "\n",
        #Allow the player to select a number from 0 to 36.
        "Choose a number if you selected Number:",
        SelectBox(
            "roulette_bet",
            [str(number) for number in range(37)],
            state.roulette_bet
        ),
        "\n",
        #Add buttons to spin the wheel or return to the casino.
        Button("Spin the Wheel", "spin_roulette"),
        Button("Return to Casino", "index")
    ])

roulette_images = {
    0 : "https://i.postimg.cc/PLtWGjHR/image.png",
    1 : "https://i.postimg.cc/kVnQrmCh/1.png",
    2 : "https://i.postimg.cc/McW7kSw-3/2.png",
    3 : "https://i.postimg.cc/94Wd3h28/3.png",
    4 : "https://i.postimg.cc/HJpwGgmS/4.png",
    5 : "https://i.postimg.cc/679rsXKM/5.png",
    6 : "https://i.postimg.cc/5HxBcVJg/6.png",
    7 : "https://i.postimg.cc/679rsXKY/7.png",
    8 : "https://i.postimg.cc/WdmGf4BK/8.png",
    9 : "https://i.postimg.cc/ZWP8DqGQ/9.png",
    10 : "https://i.postimg.cc/TyRV86x9/10.png",
    11 : "https://i.postimg.cc/Nyg6hctk/11.png",
    12 : "https://i.postimg.cc/K17PsY69/12.png",
    13 : "https://i.postimg.cc/zywCPfs2/13.png",
    14 : "https://i.postimg.cc/68Vr1Qkj/14.png",
    15 : "https://i.postimg.cc/fV7cgbGr/15.png",
    16 : "https://i.postimg.cc/VJ9qHNx4/16.png",
    17 : "https://i.postimg.cc/xXGvFdw5/17.png",
    18 : "https://i.postimg.cc/cv7R5Jpm/18.png",
    19 : "https://i.postimg.cc/gxyVB0CH/19.png",
    20 : "https://i.postimg.cc/87dRnC2h/20.png",
    21 : "https://i.postimg.cc/0zGYHNTd/21.png",
    22 : "https://i.postimg.cc/RW17b0k1/22.png",
    23 : "https://i.postimg.cc/3kjXbwsX/23.png",
    24 : "https://i.postimg.cc/7513QLF2/24.png",
    25 : "https://i.postimg.cc/tsd3mgK6/25.png",
    26 : "https://i.postimg.cc/DSQrYz91/26.png",
    27 : "https://i.postimg.cc/G4PFSpWY/27.png",
    28 : "https://i.postimg.cc/7513QLFT/28.png",
    29 : "https://i.postimg.cc/0zGYHNT6/29.png",
    30 : "https://i.postimg.cc/87dRnC27/30.png",
    31 : "https://i.postimg.cc/mP3Y6rvz/31.png",
    32 : "https://i.postimg.cc/tsd3mgKT/32.png",
    33 : "https://i.postimg.cc/nXK4wLyC/33.png",
    34 : "https://i.postimg.cc/cv7R5JpJ/34.png",
    35 : "https://i.postimg.cc/cv7R5JpC/35.png",
    36 : "https://i.postimg.cc/0z1GfSBD/36.png"
}

@route
def spin_roulette(
    state: State, bet_type: str, roulette_bet: str
) -> Page:
    '''Spin the wheel and evaluate the selected bet.'''
    #Save the player's selected number.
    state.roulette_bet = roulette_bet
    #Generate a random winning number between 0 and 36.
    state.roulette_number = randint(0, 36)
    #Update the game state to indicate that roulette has finished.
    state.current_round = "Roulette"
    state.game_over = True
    #Store the randomly generated winning number.
    number = state.roulette_number
    #Create a list containing all red numbers on the roulette wheel.
    red_numbers = [
        1, 3, 5, 7, 9, 12, 14, 16, 18,
        19, 21, 23, 25, 27, 30, 32, 34, 36
    ]
    #Check whether the player's selected bet matches the winning number.
    if bet_type == "Number":
        won = int(roulette_bet) == number
    #Check whether the winning number is red.
    elif bet_type == "Red":
        won = number in red_numbers
    #Check whether the winning number is black.
    #Zero does not count as black.
    elif bet_type == "Black":
        won = number != 0 and number not in red_numbers
    #Check whether the winning number is odd.
    #Zero does not count as odd.
    elif bet_type == "Odd":
        won = number != 0 and number % 2 == 1
    #Check whether the winning number is even.
    #Zero does not count as even.
    else:
        won = number != 0 and number % 2 == 0
    #Create a message based on whether the player's bet was correct.
    if won:
        state.message = "Your bet won! YIPPEE :)"
    else:
        state.message = "Your bet lost :("
    content = [
        "ROULETTE RESULTS\n",
        "Bet type: " + bet_type,
        "\n"]
    if bet_type == "Number" or bet_type == "Odd" or bet_type == "Even":
        content.append(
            "Your number selection: " + roulette_bet
            )
    content.extend([
        "\nWinning number:\n",
        Image(roulette_images[number]),
        "\n\n",
        state.message,
        "\n",
        #Add buttons to play another round or return to the casino.
        Button("Play Again", "roulette"),
        Button("Return to Casino", "index")
    ])
    #Display the betting selection, winning number, and final result.
    return Page(state, content)

@route
def finish_texas_holdem(state: State) -> Page:
    '''Evaluate all players' hands and announce the winner or tie.'''
    #Make sure all five community cards have been revealed.
    if state.community_stage < 5:
        state.message = "Reveal all five community cards first!"
        return texas_holdem_page(state)
    #Initialize the highest hand score and list of winners.
    best_score = None
    winners = []
    #Evaluate each player's best possible hand.
    for player in state.players:
        score, rank = best_texas_hand(
            player.cards,
            state.community_cards
        )
        #Save the player's best hand ranking.
        player.hand_rank = rank
        #Check whether this player has the highest score.
        if best_score is None or score > best_score:
            best_score = score
            winners = [player]
        #Account for ties.
        elif score == best_score:
            winners.append(player)
    #Announce the winner or winners.
    if len(winners) == 1:
        state.message = (
            f"{winners[0].name} wins with {winners[0].hand_rank}!"
        )
    else:
        winner_names = ", ".join(
            player.name for player in winners
        )
        state.message = f"It's a tie between {winner_names}!"
    #Mark the game as finished.
    state.game_over = True
    state.current_round = "Finished"
    #Display the final results.
    return texas_holdem_results(state)

@route
def texas_holdem_results(state: State) -> Page:
    '''Display each player's hand ranking and the round result.'''
    #Display the results title, winner message, and all five community cards.
    content = [
        Header("Texas Hold'em Results"),
        Text(state.message),
        Header("Community Cards"),
        "\n"]
    for card in state.community_cards:
        content.append(Image(card_images[format_card(Card(card.number,card.suit.lower()))],width=200))
    #Display each player's name, private cards, and best hand ranking.
    for player in state.players:
        #Display the player's name as a section heading.
        content.append(Header(player.name))
        content.append("\n")
        #Display the player's two private cards.
        for card in player.cards:
            content.append(Image(card_images[format_card(Card(card.number,card.suit.lower()))],width=200))
        content.append("\n")
        #Display the ranking of the player's best possible hand.
        content.append(Text(f"Best hand: {player.hand_rank}"))
    #Add buttons to start another game or return to the casino.
    content.append("\n")
    content.append(Button("Play Again", texas_holdem))
    content.append(Button("Return to Casino", index))
    #Return the completed results page.
    return Page(state, content)

start_server(State(
    "",
    "",
    [],
    [],
    [],
    [],
    2,
    "Menu",
    "Welcome to the casino!",
    False,
    0,
    "0",
    "Number",
    0
))
