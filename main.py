from drafter import *
from dataclasses import dataclass
from random import randint, shuffle, choice
from bakery import assert_equal
from itertools import combinations

# Use a clean base theme, then apply the custom design below.
set_website_style("none")

set_website_title("DeMare Casino")
set_site_information(
    author="Anthony DeMare",
    description="Simulate Casino Games and Outcomes.",
    sources="",
    planning=Link("Planning PDF","https://docs.google.com/document/d/1Q54cMhI5bBXzKVjJlt7ZRtrfVYuWWjO9/edit#heading=h.5uuq5osg3ivi"),
    links=["https://anthonydemare.github.io/pseudocasino"]
)

#hide_debug_information()
set_website_framed(False)

add_website_css("""
/* Demare Casino visual theme */
* {
    box-sizing: border-box;
}

body {
    min-height: 100vh;
    margin: 0;
    padding: 32px 20px;
    color: #f7f1df;
    text-align: center;
    background:
        radial-gradient(circle at 50% 0%, rgba(36, 104, 77, 0.72), transparent 48%),
        radial-gradient(circle at 10% 90%, rgba(120, 20, 40, 0.25), transparent 40%),
        linear-gradient(145deg, #0c3025, #061b16 68%, #04120f);
    font-family: Georgia, "Times New Roman", serif;
    font-size: 17px;
    line-height: 1.6;
}

body > div,
main {
    width: 100%;
    max-width: 1080px;
    margin: 0 auto;
}

h1, h2, h3 {
    color: #e6c875;
    text-align: center;
    line-height: 1.2;
    text-shadow: 0 2px 12px rgba(0, 0, 0, 0.35);
}

h1 {
    margin: 12px 0 24px;
    font-size: clamp(2rem, 5vw, 3.2rem);
    letter-spacing: 0.07em;
    animation: goldGlow 3s ease-in-out infinite alternate;
}

h2 {
    margin-top: 28px;
    font-size: clamp(1.5rem, 3vw, 2.2rem);
}

@keyframes goldGlow {
    from { text-shadow: 0 2px 10px rgba(0, 0, 0, 0.35); }
    to   { text-shadow: 0 0 22px rgba(240, 216, 143, 0.75), 0 2px 10px rgba(0, 0, 0, 0.35); }
}

@keyframes dealIn {
    from { opacity: 0; transform: translateY(-24px) rotate(-7deg); }
    to   { opacity: 1; transform: translateY(0) rotate(0); }
}

p, label {
    color: #f7f1df;
}

button {
    margin: 8px 8px 8px 0;
    padding: 12px 22px;
    border: 1px solid #f0d88f;
    border-radius: 10px;
    color: #14271f;
    background: linear-gradient(180deg, #f1d994, #c9a94f);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25);
    font-family: inherit;
    font-size: 1rem;
    font-weight: bold;
    cursor: pointer;
    transition: transform 0.15s ease, filter 0.15s ease, box-shadow 0.15s ease;
}

button:hover {
    transform: translateY(-2px);
    filter: brightness(1.08);
    box-shadow: 0 7px 16px rgba(0, 0, 0, 0.32);
}

button:active {
    transform: translateY(0);
}

input, select, textarea {
    max-width: 100%;
    margin: 6px 8px 14px 0;
    padding: 10px 12px;
    border: 1px solid #b99b50;
    border-radius: 8px;
    color: #f7f1df;
    background: #102d23;
    font: inherit;
}

input:focus, select:focus, textarea:focus {
    outline: 2px solid #e6c875;
    outline-offset: 2px;
}

img {
    width: min(150px, 26vw) !important;
    height: auto;
    margin: 8px;
    border: 2px solid #d8bd72;
    border-radius: 9px;
    background: #fff;
    box-shadow: 0 6px 16px rgba(0, 0, 0, 0.35);
    vertical-align: middle;
    animation: dealIn 0.45s ease-out both;
    transition: transform 0.2s ease;
}

img:hover {
    transform: translateY(-6px) scale(1.04);
}

a {
    color: #f0d88f;
}

hr {
    border: 0;
    border-top: 1px solid rgba(230, 200, 117, 0.45);
    margin: 24px 0;
}

@media (max-width: 600px) {
    body {
        padding: 20px 12px;
        font-size: 16px;
    }

    button {
        width: 100%;
        margin: 6px 0;
    }

    img {
        width: min(125px, 28vw) !important;
        margin: 5px;
    }
}
""")

@dataclass
class Card:
    '''The number is the actual number value of the card
    the suit is the suit of the card
    '''
    number: int
    suit: str

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

@dataclass
class Player:
    '''name: the name of the player
    cards: the cards the player holds
    hand_rank: the rank of the hand (flush, straight, etc.)
    result: whether the player won or lost
    is_human: "is it the person playing the game?"
    chips: chips the player currently has (bots keep theirs between hands)
    bet: chips put in during the CURRENT betting round
    contributed: chips put in during the WHOLE hand (used for side pots)
    folded: did they fold this hand?
    all_in: did they push every chip into the middle?
    acted: have they acted since the last raise? (betting engine uses this)
    aggro: 0-100, how aggressive/bluffy a bot is
    '''
    name: str
    cards: list[Card]
    hand_rank: str
    result: str
    is_human: bool = False
    chips: int = 0
    bet: int = 0
    contributed: int = 0
    folded: bool = False
    all_in: bool = False
    acted: bool = False
    aggro: int = 50

@dataclass
class State:
    game_type: str #type of game played
    player_name: str #name of player
    players: list[Player] #list of players playing
    community_cards: list[Card] #list of cards on table
    dealer_cards: list[Card] #list of cards dealer has (blackjack)
    deck: list[Card] #cards left in deck
    player_count: int #number of players
    current_round: str #what round we are on
    message: str #the message portrayed on screen
    game_over: bool #is the game completed?
    roulette_number: int #number on roulette
    roulette_bet: str #betted number on roulette
    bet_type: str #type of roulette bet (red,number,odd?)
    community_stage: int #how many cards on the table for Texas Hold'em
    chips: int #YOUR bankroll, shared by every game
    bet: int #your wager in blackjack
    pot: int #chips in the middle (poker)
    current_bet: int #amount everyone must match this betting round
    min_raise: int #smallest legal raise
    turn: int #index of whose turn it is (poker)
    raises: int #raises so far this round (capped so bots can't argue forever)
    stage_index: int #which betting round we are in
    hand_log: list[str] #what the bots did this hand
    achievements: list[str] #unlocked achievements
    hands_played: int
    hands_won: int
    biggest_win: int
    net_profit: int #lifetime profit/loss
    begs: int #how many times you have asked for free chips
    last_net: int #profit/loss of the most recent round
    toast: str #one-time pop-up text (achievements)

STARTING_CHIPS = 1000
ANTE = 10
MAX_RAISES = 4
POKER_GAMES = ["Texas Hold'em", "Three-Card Poker", "Five-Card Poker"]
HAND_SIZE = {"Texas Hold'em": 2, "Three-Card Poker": 3, "Five-Card Poker": 5}

#(name, aggression) - up to five bots for a six player table
BOT_PROFILES = [
    ("Lucky Larry", 40),
    ("Sketchy Sue", 80),
    ("Grandma Pearl", 25),
    ("Count Inthuchipps", 60),
    ("Dealer Dave", 50)
]

ACHIEVEMENTS = {
    "Beginner's Luck": "Win your first hand.",
    "High Roller Moment": "Win 500+ chips in a single round.",
    "Whale Watching": "Reach 5,000 chips.",
    "Rock Bottom": "Hit zero chips. It happens to the best of us.",
    "Professional Beggar": "Ask for free chips 5 times.",
    "Regular": "Play 25 rounds.",
    "Cardsharp": "Win a poker hand with a Full House or better.",
    "Lucky Seven": "Hit the slots jackpot.",
    "Zero Hero": "Win a straight-up bet on roulette's green 0."
}

WIN_QUIPS = [
    "The house is crying in the break room.",
    "Somewhere, a security camera just sighed.",
    "Chips acquired. Ego inflated.",
    "Skill? Luck? Witchcraft? We may never know.",
    "Don't spend it all in one place. Spend it in a different place of ours."
]
LOSE_QUIPS = [
    "On the bright side, the chips were fake anyway.",
    "The house sends its thoughts and prayers. Mostly prayers.",
    "That was less 'gambling' and more 'donating'.",
    "Statistically, you were due. Statistically, you are still due.",
    "Your chips have gone to a better place. The house's pocket."
]
PUSH_QUIPS = [
    "A tie! Nobody wins, nobody loses, everybody is slightly disappointed.",
    "You get your bet back. The thrill of victory is on backorder."
]
RAISE_QUIPS = [
    "{} raises to {}. Their poker face is doing a LOT of work.",
    "{} bumps it to {}. Confident, or just dramatic?",
    "{} pushes the bet to {} and stares at you menacingly.",
    "{} raises to {} with a suspiciously steady hand."
]
CALL_QUIPS = [
    "{} calls.",
    "{} calls, whistling casually.",
    "{} calls and adjusts their tie."
]
CHECK_QUIPS = [
    "{} checks.",
    "{} taps the table. Check.",
    "{} checks, doing absolutely nothing suspicious."
]
FOLD_QUIPS = [
    "{} folds and pretends that was the plan.",
    "{} folds. Cowardice, or wisdom? Yes.",
    "{} tosses their cards in with a dramatic sigh."
]
BEG_LINES = [
    "The pit boss slides you a tray of chips with a sympathetic nod.",
    "A mysterious benefactor leaves chips on your seat.",
    "You find chips in your couch cushions. Technically a miracle.",
    "Grandma Pearl slips you some chips and tells you not to tell your mother.",
    "The casino 'accidentally' mis-stacked a tray in your direction."
]
BEG_LINES_LATER = [
    "Again?! Fine. The pit boss is no longer making eye contact.",
    "Here. Take it. We're calling this a 'loyalty program'.",
    "The house has started a file on you. It's labeled 'Charity Case'."
]

def rank_title(chips: int) -> str:
    '''Give the player a title based on their bankroll.'''
    if chips <= 0:
        return "Professional Window Shopper"
    if chips < 200:
        return "Couch Cushion Archaeologist"
    if chips < 600:
        return "Penny Gambler"
    if chips < 1500:
        return "Regular"
    if chips < 5000:
        return "High Roller"
    if chips < 20000:
        return "Whale"
    return "Casino Owner (the IRS has questions)"

def card_to_image(card: Card) -> str:
    '''converts a card to an image link
    this image link can be added to drafter
    '''
    return card_images[format_card(Card(card.number, card.suit.lower()))]

def show_cards(cards: list[Card]) -> list:
    '''Turn a list of cards into a list of Images.'''
    return [Image(card_to_image(card), width=200) for card in cards]

def new_deck() -> list[Card]:
    '''Return a freshly shuffled 52-card deck.'''
    deck = [
        Card(number, suit)
        for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]
        for number in range(2, 15)
    ]
    shuffle(deck)
    return deck

def unlock(state: State, name: str):
    '''Unlock an achievement (once) and queue a pop-up message.'''
    if name not in state.achievements:
        state.achievements.append(name)
        text = "🏆 Achievement unlocked: " + name + " - " + ACHIEVEMENTS[name]
        if state.toast != "":
            state.toast = state.toast + "   |   " + text
        else:
            state.toast = text

def record(state: State, net: int):
    '''Update lifetime stats after any finished round.
    net is profit (positive) or loss (negative).
    '''
    state.last_net = net
    state.hands_played += 1
    state.net_profit += net
    if net > 0:
        state.hands_won += 1
        if net > state.biggest_win:
            state.biggest_win = net
        if state.hands_won == 1:
            unlock(state, "Beginner's Luck")
        if net >= 500:
            unlock(state, "High Roller Moment")
    if state.chips <= 0:
        unlock(state, "Rock Bottom")
    if state.chips >= 5000:
        unlock(state, "Whale Watching")
    if state.hands_played >= 25:
        unlock(state, "Regular")

def outcome_line(net: int) -> str:
    '''A joke that fits how the round went.'''
    if net > 0:
        return choice(WIN_QUIPS)
    if net < 0:
        return choice(LOSE_QUIPS)
    return choice(PUSH_QUIPS)

def net_text(net: int) -> str:
    '''Format profit/loss for display.'''
    if net > 0:
        return "💚 You won " + format(net, ",") + " chips!"
    if net < 0:
        return "💔 You lost " + format(-net, ",") + " chips."
    return "😐 You broke even."

def chip_bar(state: State) -> list:
    '''The status bar shown at the top of every page.'''
    items = [Text(
        f"💰 Chips: {state.chips:,}   |   🎖️ Rank: {rank_title(state.chips)}"
        f"   |   📈 Net: {state.net_profit:+,}"
    )]
    if state.toast != "":
        items.append(Text(state.toast))
        state.toast = ""
    items.append("\n")
    return items

def bet_options(chips: int) -> list[str]:
    '''Build the list of bets the player can afford.'''
    options = [str(a) for a in [10, 25, 50, 100, 250, 500, 1000, 5000] if a <= chips]
    if chips > 0:
        options.append("ALL IN (" + str(chips) + ")")
    return options

def default_bet(options: list[str]) -> str:
    '''Pick a sensible preselected bet.'''
    if len(options) > 2:
        return options[1]
    return options[0]

def parse_bet(text: str, chips: int) -> int:
    '''Turn a bet menu choice back into a number (never more than chips).'''
    if text.startswith("ALL IN"):
        return chips
    try:
        amount = int(text)
    except ValueError:
        amount = 10
    return max(0, min(amount, chips))

def bet_picker(state: State) -> list:
    '''A bet dropdown named bet_amount.'''
    options = bet_options(state.chips)
    return ["Your bet:", SelectBox("bet_amount", options, default_bet(options)), "\n"]

@route
def broke_page(state: State) -> Page:
    '''Shown when the player cannot afford to play.'''
    return Page(state, chip_bar(state) + [
        Header("OUT OF CHIPS"),
        "The dealer looks at your empty hands.\n",
        "The security guard looks at your empty hands.\n",
        "Even the slot machine looks at your empty hands.\n\n",
        "Good news: begging is legal here.\n",
        Button("🎁 Beg the House for Chips", "free_chips"),
        Button("Return to Casino", "index")
    ])

@route
def free_chips(state: State) -> Page:
    '''Give the player a handful of free chips, with commentary.'''
    state.begs += 1
    amount = randint(100, 400)
    state.chips += amount
    if state.begs >= 5:
        unlock(state, "Professional Beggar")
    if state.begs <= 3:
        line = choice(BEG_LINES)
    else:
        line = choice(BEG_LINES_LATER)
    if state.chips - amount >= 2000:
        line = "You have " + format(state.chips - amount, ",") + " chips and you're asking for MORE? Bold. Take them."
    return Page(state, chip_bar(state) + [
        Header("🎁 FREE CHIPS"),
        line + "\n",
        "You received " + str(amount) + " chips. (Times begged: " + str(state.begs) + ")\n",
        Button("Back to the Casino", "index")
    ])

@route
def stats(state: State) -> Page:
    '''Show lifetime stats and achievements.'''
    if state.hands_played > 0:
        win_rate = round(100 * state.hands_won / state.hands_played)
    else:
        win_rate = 0
    content = chip_bar(state) + [
        Header("📊 YOUR PERMANENT RECORD"),
        "Player: " + state.player_name + "\n",
        "Rounds played: " + str(state.hands_played) + "\n",
        "Rounds won: " + str(state.hands_won) + " (" + str(win_rate) + "%)\n",
        "Biggest single win: " + format(state.biggest_win, ",") + " chips\n",
        "Lifetime profit: " + f"{state.net_profit:+,}" + " chips\n",
        "Times begged: " + str(state.begs) + "\n",
        Header("Achievements"),
    ]
    for name in ACHIEVEMENTS:
        if name in state.achievements:
            content.append("✅ " + name + " - " + ACHIEVEMENTS[name] + "\n")
        else:
            content.append("🔒 " + name + " - " + ACHIEVEMENTS[name] + "\n")
    content.extend(["\n", Button("Return to Casino", "index")])
    return Page(state, content)

# ----------------------------------------------------------------------
# HAND EVALUATION (blackjack and poker)
# ----------------------------------------------------------------------

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

assert_equal(parse_bet("ALL IN (250)", 250), 250)
assert_equal(parse_bet("500", 100), 100)
assert_equal(bet_options(60), ["10", "25", "50", "ALL IN (60)"])

# ----------------------------------------------------------------------
# HOME PAGE AND SETUP
# ----------------------------------------------------------------------

@route
def index(state: State) -> Page:
    '''Display the casino home page.'''
    return Page(state, chip_bar(state) + [
        Header("WELCOME TO THE DEMARE CASINO\n"),
        "Where the chips are fake, the stakes are imaginary,\n",
        "and the disappointment is 100% real.\n\n",
        "Choose a game to play.\n",
        Button("Texas Hold'em", "setup_texas"),
        Button("Blackjack", "setup_blackjack"),
        Button("Three-Card Poker", "setup_three_card"),
        Button("Five-Card Poker", "setup_five_card"),
        Button("Roulette", "setup_roulette"),
        Button("🎰 Slot Machine", "setup_slots"),
        "\n",
        Button("🎁 Free Chips (Pity Edition)", "free_chips"),
        Button("📊 Stats & Achievements", "stats")
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
def setup_slots(state: State) -> Page:
    '''Set up the slot machine.'''
    state.game_type = "Slots"
    return setup(state)

@route
def setup(state: State) -> Page:
    '''Display the setup page for the selected game.'''
    content = chip_bar(state) + [
        "Let's set this thing up for you.\n",
        "Selected game: " + state.game_type,
        "\n",
        "Enter your name:",
        TextBox("player_name", state.player_name),
        "\n"
    ]

    #not all games are multiplayer, so filter what's needed
    if state.game_type in POKER_GAMES:
        content.extend([ #up to six players, default 2
            "Choose the number of players (the others are bots with... personalities):",
            SelectBox("player_count", ["2","3","4","5","6"],"3"),
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
    #poker with nobody to play against is just sitting quietly
    if state.game_type in POKER_GAMES and player_count < 2:
        player_count = 2
    #changes the necessary aspects of State
    state.player_count = player_count
    state.players = []
    state.community_cards = []
    state.deck = []
    state.current_round = "Starting"
    state.game_over = False
    state.message = "Game setup complete."

    content = chip_bar(state) + [
        "You know what time it is??? GAME TIME!!!\n",
        "*insert cool music and awesome colors...*\n",
        "Player: " + state.player_name,
        "\n",
        "Selected game: " + state.game_type,
        "\n"
    ]
    if state.game_type in POKER_GAMES:
        content.extend(["Number of players: " + str(state.player_count), "\n"])
    content.extend([
        state.message,
        "\n",
        Button("Continue", "play_game"),
        Button("Return to Casino", "index")
    ])
    return Page(state, content)

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
    elif state.game_type == "Slots":
        return slots(state)
    return Page(state, [ #just in case something went wrong
        state.game_type,
        "This game has not been implemented yet.",
        Button("Return to Casino", "index")
    ])

# ----------------------------------------------------------------------
# POKER ENGINE (shared by Texas Hold'em, Three-Card and Five-Card Poker)
# Real betting: ante, check, call, raise, fold, all-in, side pots, and
# bots that think (a little) about their cards.
# ----------------------------------------------------------------------

def poker_stages(state: State) -> list[str]:
    '''Names of the betting rounds for the current game.'''
    if state.game_type == "Texas Hold'em":
        return ["Pre-Flop", "Flop", "Turn", "River"]
    return ["Betting Round"]

def poker_score(state: State, player: Player) -> tuple[tuple[int, ...], str]:
    '''Final score and rank for a player's hand.'''
    if state.game_type == "Texas Hold'em":
        return best_texas_hand(player.cards, state.community_cards)
    if state.game_type == "Three-Card Poker":
        return evaluate_three_card_hand(player.cards)
    return evaluate_hand(player.cards)

HAND_TABLE = [0.15, 0.45, 0.60, 0.72, 0.80, 0.85, 0.92, 0.97, 0.99, 1.0]
THREE_TABLE = [0.25, 0.60, 0.80, 0.75, 0.90, 0.98]

def hand_strength(state: State, player: Player) -> float:
    '''How good does a bot THINK its hand is? 0.0 (trash) to 1.0 (unbeatable).'''
    if state.game_type == "Texas Hold'em":
        if state.community_stage < 3: #pre-flop: judge the two hole cards
            low, high = sorted(card.number for card in player.cards)
            strength = 0.2 + (low + high) / 28 * 0.25
            if low == high:
                strength += 0.3 + low / 14 * 0.2
            if player.cards[0].suit == player.cards[1].suit:
                strength += 0.05
            return min(strength, 1.0)
        visible = state.community_cards[:state.community_stage]
        score, rank = best_texas_hand(player.cards, visible)
        return HAND_TABLE[score[0]]
    if state.game_type == "Three-Card Poker":
        score, rank = evaluate_three_card_hand(player.cards)
        strength = THREE_TABLE[score[0]]
        if score[0] == 0:
            strength += 0.1 * (max(c.number for c in player.cards) - 2) / 12
        return strength
    score, rank = evaluate_hand(player.cards)
    return HAND_TABLE[score[0]]

def log(state: State, text: str):
    '''Add a line to the table talk.'''
    state.hand_log.append(text)

def put_in(state: State, player: Player, amount: int):
    '''Move chips from a player into the pot (never more than they have).'''
    amount = max(0, min(amount, player.chips))
    player.chips -= amount
    player.bet += amount
    player.contributed += amount
    state.pot += amount
    if player.chips == 0:
        player.all_in = True

def raise_to(state: State, player: Player, target: int):
    '''Raise so the player's bet this round equals target.
    A real raise makes everybody else get another turn.
    '''
    target = min(target, player.bet + player.chips)
    put_in(state, player, target - player.bet)
    if player.bet > state.current_bet:
        state.current_bet = player.bet
        state.raises += 1
        for other in state.players:
            if other is not player and not other.folded and not other.all_in:
                other.acted = False
    player.acted = True

def next_actor(state: State):
    '''Find who must act next, or None if the betting round is done.'''
    live = [p for p in state.players if not p.folded and not p.all_in]
    if len(live) == 0:
        return None
    if len(live) == 1 and live[0].bet >= state.current_bet:
        return None #nobody left to bet against
    count = len(state.players)
    for step in range(count):
        index = (state.turn + step) % count
        player = state.players[index]
        if (not player.folded and not player.all_in
                and (not player.acted or player.bet < state.current_bet)):
            state.turn = index
            return player
    return None

def bot_act(state: State, bot: Player):
    '''Let a bot decide what to do.'''
    to_call = state.current_bet - bot.bet
    bluffing = randint(1, 100) <= bot.aggro // 5
    confidence = hand_strength(state, bot)
    if bluffing:
        confidence += 0.3
    confidence += randint(-8, 8) / 100 + (bot.aggro - 50) / 500
    can_raise = state.raises < MAX_RAISES and bot.chips > to_call
    extra = max(state.min_raise, (state.pot // 4) // 10 * 10)
    if confidence > 0.92:
        extra *= 2

    if to_call == 0:
        if can_raise and confidence > 0.62:
            raise_to(state, bot, state.current_bet + extra)
            log(state, choice(RAISE_QUIPS).format(bot.name, bot.bet))
        else:
            bot.acted = True
            log(state, choice(CHECK_QUIPS).format(bot.name))
        return

    need = 0.2 + 0.5 * to_call / (state.pot + to_call)
    if confidence < need:
        bot.folded = True
        bot.acted = True
        log(state, choice(FOLD_QUIPS).format(bot.name))
    elif can_raise and confidence > 0.78:
        raise_to(state, bot, state.current_bet + extra)
        if bot.all_in:
            log(state, bot.name + " goes ALL IN. Dramatic music plays.")
        else:
            log(state, choice(RAISE_QUIPS).format(bot.name, bot.bet))
    else:
        put_in(state, bot, to_call)
        bot.acted = True
        if bot.all_in:
            log(state, bot.name + " calls and is now ALL IN. Gulp.")
        else:
            log(state, choice(CALL_QUIPS).format(bot.name))

def advance_betting(state: State) -> Page:
    '''Run the betting round until it is the human's turn or the round ends.'''
    while True:
        alive = [p for p in state.players if not p.folded]
        if len(alive) == 1:
            return showdown(state)
        actor = next_actor(state)
        if actor is None:
            return end_of_betting_round(state)
        if actor.is_human:
            return poker_page(state)
        bot_act(state, actor)
        state.turn = (state.turn + 1) % len(state.players)

def end_of_betting_round(state: State) -> Page:
    '''Collect bets, reveal community cards, start the next round.'''
    for player in state.players:
        player.bet = 0
        player.acted = False
    state.current_bet = 0
    state.raises = 0
    state.turn = 0
    state.stage_index += 1
    stages = poker_stages(state)
    if state.stage_index >= len(stages):
        return showdown(state)
    state.current_round = stages[state.stage_index]
    if state.game_type == "Texas Hold'em":
        state.community_stage = [0, 3, 4, 5][state.stage_index]
        names = {"Flop": "The flop", "Turn": "The turn", "River": "The river"}
        state.message = names[state.current_round] + " has been revealed!"
        log(state, "--- " + state.message + " ---")
    return advance_betting(state)

def split_pots(players: list[Player], scores: dict) -> list[int]:
    '''Work out who wins what, including side pots for all-ins.'''
    payouts = [0] * len(players)
    levels = sorted(set(p.contributed for p in players if p.contributed > 0))
    previous = 0
    for level in levels:
        layer = sum(
            min(p.contributed, level) - min(p.contributed, previous)
            for p in players)
        eligible = [
            i for i, p in enumerate(players)
            if not p.folded and p.contributed >= level]
        if not eligible: #only folded players reached this level: refund
            eligible = [
                i for i, p in enumerate(players) if p.contributed >= level]
        scored = [i for i in eligible if i in scores]
        if scored:
            top = max(scores[i] for i in scored)
            winners = [i for i in scored if scores[i] == top]
        else:
            winners = eligible
        share = layer // len(winners)
        for i in winners:
            payouts[i] += share
        payouts[winners[0]] += layer - share * len(winners)
        previous = level
    return payouts

def showdown(state: State) -> Page:
    '''Compare hands, pay the winners, update stats.'''
    state.game_over = True
    state.current_round = "Showdown"
    if state.game_type == "Texas Hold'em":
        state.community_stage = 5
    players = state.players
    alive = [i for i, p in enumerate(players) if not p.folded]
    for player in players:
        if player.folded:
            player.hand_rank = "Folded"
    if len(alive) == 1:
        payouts = [0] * len(players)
        payouts[alive[0]] = state.pot
        players[alive[0]].hand_rank = "Everyone else folded"
    else:
        scores = {}
        for i in alive:
            score, rank = poker_score(state, players[i])
            scores[i] = score
            players[i].hand_rank = rank
        payouts = split_pots(players, scores)

    winners = []
    for i, player in enumerate(players):
        player.chips += payouts[i]
        if player.folded:
            player.result = "Folded"
        elif payouts[i] > 0:
            player.result = "Winner"
            winners.append(i)
        else:
            player.result = "Lost"

    if len(winners) == 1:
        top = players[winners[0]]
        state.message = f"{top.name} wins {payouts[winners[0]]:,} chips! ({top.hand_rank})"
    elif len(winners) > 1:
        state.message = "The pot is split between " + ", ".join(players[i].name for i in winners) + "!"
    else:
        state.message = "Somehow nobody won. Call the manager."

    human = players[0]
    state.chips = human.chips
    net = payouts[0] - human.contributed
    if (payouts[0] > 0 and not human.folded and human.hand_rank in
            ["Full House", "Four of a Kind", "Straight Flush", "Royal Flush"]):
        unlock(state, "Cardsharp")
    record(state, net)
    return poker_results(state)

def raise_options(state: State, player: Player) -> list[str]:
    '''Raise sizes the human can afford.'''
    to_call = state.current_bet - player.bet
    return ["+" + str(a) for a in [20, 50, 100, 250, 500] if player.chips >= to_call + a]

def start_poker_hand(state: State) -> Page:
    '''Ante up, deal cards, and start betting.'''
    if state.chips < ANTE:
        return broke_page(state)
    state.deck = new_deck()
    size = HAND_SIZE[state.game_type]
    old = state.players
    #keep the same bots (and their chips) from hand to hand
    if len(old) == state.player_count and len(old) > 1 and old[0].is_human:
        players = old
    else:
        players = [Player(state.player_name, [], "", "", True, state.chips)]
        for i in range(1, state.player_count):
            name, aggro = BOT_PROFILES[i - 1]
            players.append(Player(name, [], "", "", False, 500, aggro=aggro))
    state.players = players
    state.hand_log = []
    state.pot = 0
    state.current_bet = 0
    state.min_raise = 20
    state.raises = 0
    state.turn = 0
    state.stage_index = 0
    state.community_stage = 0
    state.game_over = False
    state.current_round = poker_stages(state)[0]
    for i, player in enumerate(players):
        player.cards = [state.deck.pop() for _ in range(size)]
        player.hand_rank = ""
        player.result = ""
        player.bet = 0
        player.contributed = 0
        player.folded = False
        player.all_in = False
        player.acted = False
        if i == 0:
            player.chips = state.chips
        elif player.chips < ANTE:
            player.chips = 500
            log(state, player.name + " found chips in their sock. They're back in!")
        put_in(state, player, ANTE)
        player.bet = 0 #antes are not part of the round's bet
    state.community_cards = []
    if state.game_type == "Texas Hold'em":
        state.community_cards = [state.deck.pop() for _ in range(5)]
    state.chips = players[0].chips
    state.message = "Everyone antes " + str(ANTE) + " chips. (The casino calls it a 'cover charge'.)"
    return advance_betting(state)

def poker_page(state: State) -> Page:
    '''The table: your cards, the bets, and your options.'''
    human = state.players[0]
    to_call = state.current_bet - human.bet
    stage = poker_stages(state)[state.stage_index]
    content = chip_bar(state) + [
        Header(state.game_type),
        Text(f"{stage}   |   🪙 Pot: {state.pot:,}   |   Bet to match: {state.current_bet}"),
        Text(state.message),
        "\n"
    ]
    for player in state.players:
        if player.folded:
            status = "folded 🏳️"
        elif player.all_in:
            status = "ALL IN 🔥"
        else:
            status = "bet " + str(player.bet) + " this round"
        content.append(f"{player.name}: 💰 {player.chips:,} ({status})\n")
        if player.is_human:
            content.extend(show_cards(player.cards))
            content.append("\n")
        elif not player.folded:
            content.append("🂠 " * len(player.cards) + "\n")

    if state.game_type == "Texas Hold'em":
        content.append(Header("Community Cards"))
        if state.community_stage == 0:
            content.append(Text("No community cards revealed yet."))
        else:
            content.extend(show_cards(state.community_cards[:state.community_stage]))
        content.append("\n")

    #a helpful hint about your current hand
    if state.game_type == "Texas Hold'em":
        if state.community_stage >= 3:
            score, rank = best_texas_hand(human.cards, state.community_cards[:state.community_stage])
            content.append(Text("Your best hand so far: " + rank))
    else:
        score, rank = poker_score(state, human)
        content.append(Text("Your hand: " + rank))

    if len(state.hand_log) > 0:
        content.append(Header("Table Talk"))
        for line in state.hand_log[-6:]:
            content.append(line + "\n")

    content.append(Header("Your Move"))
    if to_call == 0:
        content.append(Button("Check", "poker_check"))
    else:
        content.append(Text(f"It costs {min(to_call, human.chips)} to stay in."))
        content.append(Button("Call " + str(min(to_call, human.chips)), "poker_call"))
    options = raise_options(state, human)
    if len(options) > 0 and state.raises < MAX_RAISES:
        content.extend(["\n", "Raise by:", SelectBox("raise_by", options, options[0]), Button("Raise!", "poker_raise")])
    elif state.raises >= MAX_RAISES:
        content.append(Text("Raise limit reached. Everyone has calmed down."))
    content.extend([
        "\n",
        Button("ALL IN (" + str(human.chips) + ")", "poker_all_in"),
        Button("Fold", "poker_fold")
    ])
    return Page(state, content)

def human_done(state: State):
    '''Bookkeeping after the human acts.'''
    state.turn = 1 % len(state.players)
    state.chips = state.players[0].chips

@route
def poker_check(state: State) -> Page:
    '''Human checks.'''
    if state.game_over:
        return poker_results(state)
    human = state.players[0]
    human.acted = True
    log(state, human.name + " checks.")
    human_done(state)
    return advance_betting(state)

@route
def poker_call(state: State) -> Page:
    '''Human calls the current bet.'''
    if state.game_over:
        return poker_results(state)
    human = state.players[0]
    put_in(state, human, state.current_bet - human.bet)
    human.acted = True
    if human.all_in:
        log(state, human.name + " calls and is ALL IN!")
    else:
        log(state, human.name + " calls.")
    human_done(state)
    return advance_betting(state)

@route
def poker_raise(state: State, raise_by: str) -> Page:
    '''Human raises.'''
    if state.game_over:
        return poker_results(state)
    human = state.players[0]
    try:
        amount = int(raise_by.replace("+", ""))
    except ValueError:
        amount = state.min_raise
    raise_to(state, human, state.current_bet + amount)
    log(state, human.name + " raises to " + str(human.bet) + ". Bold!")
    human_done(state)
    return advance_betting(state)

@route
def poker_all_in(state: State) -> Page:
    '''Human shoves everything into the middle.'''
    if state.game_over:
        return poker_results(state)
    human = state.players[0]
    raise_to(state, human, human.bet + human.chips)
    human.acted = True
    log(state, human.name + " goes ALL IN. Everyone stares.")
    human_done(state)
    return advance_betting(state)

@route
def poker_fold(state: State) -> Page:
    '''Human folds.'''
    if state.game_over:
        return poker_results(state)
    human = state.players[0]
    human.folded = True
    human.acted = True
    log(state, human.name + " folds. The bots will finish without you.")
    human_done(state)
    return advance_betting(state)

def poker_results(state: State) -> Page:
    '''Show every hand, who won, and how much it hurt.'''
    content = chip_bar(state) + [
        Header(state.game_type + " Results"),
        Text(state.message),
        Text(f"🪙 Total pot: {state.pot:,}"),
        "\n"
    ]
    if state.game_type == "Texas Hold'em":
        content.append(Header("Community Cards"))
        content.extend(show_cards(state.community_cards))
        content.append("\n")
    for player in state.players:
        content.append(Header(player.name))
        content.extend(show_cards(player.cards))
        content.append("\n")
        content.append("Hand: " + player.hand_rank + "   |   Result: " + player.result + "\n")
    content.extend(["\n", net_text(state.last_net), "\n", outcome_line(state.last_net), "\n\n"])
    if state.chips >= ANTE:
        content.append(Button("Deal New Hand", "play_game"))
    else:
        content.append(Button("🎁 Beg for Chips", "free_chips"))
    content.append(Button("Return to Casino", "index"))
    return Page(state, content)

#the three poker entry points all use the same engine
@route
def five_card_poker(state: State) -> Page:
    '''Deal five cards to each player and start betting.'''
    return start_poker_hand(state)

@route
def three_card_poker(state: State) -> Page:
    '''Deal three cards to each player and start betting.'''
    return start_poker_hand(state)

@route
def texas_holdem(state: State) -> Page:
    '''Deal two private cards to each player and start betting.'''
    return start_poker_hand(state)

# ----------------------------------------------------------------------
# BLACKJACK (bets, 3:2 blackjack payout, double down)
# ----------------------------------------------------------------------

@route
def blackjack(state: State) -> Page:
    '''Betting page for a new Blackjack round.'''
    if state.chips <= 0:
        return broke_page(state)
    state.game_over = False
    return Page(state, chip_bar(state) + [
        Header("Blackjack"),
        "Beat the dealer without going over 21.\n",
        "Blackjack pays 3:2. The dealer stands on 17. Math is on the house's side, but hope is free.\n\n"
    ] + bet_picker(state) + [
        Button("Deal Me In", "deal_blackjack"),
        Button("Return to Casino", "index")
    ])

@route
def deal_blackjack(state: State, bet_amount: str) -> Page:
    '''Take the bet and deal two cards to the player and dealer.'''
    bet = parse_bet(bet_amount, state.chips)
    if bet <= 0:
        return broke_page(state)
    state.chips -= bet
    state.bet = bet
    state.deck = new_deck()
    player_cards = [state.deck.pop(), state.deck.pop()]
    state.dealer_cards = [state.deck.pop(), state.deck.pop()]
    state.players = [
        Player(state.player_name, player_cards, "", "", True)
    ]
    state.current_round = "Blackjack"
    state.game_over = False
    state.message = ""
    if bet >= 500:
        state.message = "That's a big bet. Your palms are sweaty. "
    player_natural = hand_value(player_cards) == 21
    dealer_natural = hand_value(state.dealer_cards) == 21
    if player_natural and dealer_natural:
        finish_blackjack(state, "push", "Double blackjack! Very rare, very awkward.")
    elif player_natural:
        finish_blackjack(state, "blackjack", "BLACKJACK! Pays 3 to 2!")
    elif dealer_natural:
        finish_blackjack(state, "lose", "The dealer has blackjack. Ouch.")
    return blackjack_page(state)

def finish_blackjack(state: State, outcome: str, message: str):
    '''Pay out (or collect) and end the round.
    outcome is one of: win, lose, push, blackjack
    '''
    bet = state.bet
    player = state.players[0]
    state.game_over = True
    if outcome == "blackjack":
        winnings = bet * 3 // 2
        state.chips += bet + winnings
        net = winnings
        player.result = "Blackjack"
    elif outcome == "win":
        state.chips += bet * 2
        net = bet
        player.result = "Winner"
    elif outcome == "push":
        state.chips += bet
        net = 0
        player.result = "Push"
    else:
        net = -bet
        if player.result != "Bust":
            player.result = "Lost"
    state.message = message
    record(state, net)

@route
def blackjack_page(state: State) -> Page:
    '''Display the current Blackjack hand and available actions.'''
    player = state.players[0]
    content = chip_bar(state) + [
        Header("Blackjack"),
        Text(f"{player.name}'s hand:   (💵 Bet: {state.bet:,})"),
        "\n"]
    content.extend(show_cards(player.cards))
    content.extend(["\n", Text(f"Your total: {hand_value(player.cards)}"), "\n"])

    if state.game_over:
        content.append("\n")
        content.append(Text("Dealer's hand:"))
        content.append("\n")
        content.extend(show_cards(state.dealer_cards))
        content.append("\n")
        content.append(Text(f"Dealer total: {hand_value(state.dealer_cards)}"))
        content.append("\n")
        content.append(Text(state.message))
        content.append(Text(net_text(state.last_net)))
        content.append(Text(outcome_line(state.last_net)))
        content.append("\n")
        if state.chips > 0:
            content.append(Button("Play Again", "blackjack"))
        else:
            content.append(Button("🎁 Beg for Chips", "free_chips"))
        content.append(Button("Return to Casino", "index"))
    else:
        content.append("\n")
        content.append(Text("Dealer's visible card:"))
        content.append("\n")
        content.extend(show_cards([state.dealer_cards[0]]))
        content.append("\n")
        content.append(Text("Dealer's second card is hidden. (It's plotting.)"))
        content.append("\n")
        if hand_value(player.cards) == 21:
            content.append(Button("Stand", "blackjack_stand"))
        else:
            content.append(Button("Hit", "blackjack_hit"))
            content.append(Button("Stand", "blackjack_stand"))
            if len(player.cards) == 2 and state.chips >= state.bet:
                content.append(Button("Double Down (" + str(state.bet) + " more)", "blackjack_double"))
    return Page(state, content)

@route
def blackjack_hit(state: State) -> Page:
    '''Give the player one card and check for a bust.'''
    if not state.game_over:
        state.players[0].cards.append(state.deck.pop())
        if hand_value(state.players[0].cards) > 21:
            state.players[0].result = "Bust"
            finish_blackjack(state, "lose", "You busted! The dealer wins. Greed is a hard teacher.")
    return blackjack_page(state)

def dealer_plays_and_settle(state: State):
    '''The dealer draws to 17 and the winner is decided.'''
    player_total = hand_value(state.players[0].cards)
    while hand_value(state.dealer_cards) < 17:
        state.dealer_cards.append(state.deck.pop())
    dealer_total = hand_value(state.dealer_cards)
    if dealer_total > 21:
        finish_blackjack(state, "win", "The dealer busted. You win!")
    elif player_total > dealer_total:
        finish_blackjack(state, "win", "Your total is higher. You win!")
    elif player_total == dealer_total:
        finish_blackjack(state, "push", "It's a tie! Push.")
    else:
        finish_blackjack(state, "lose", "The dealer wins!")

@route
def blackjack_stand(state: State) -> Page:
    '''Finish the player's turn and let the dealer draw.'''
    if not state.game_over:
        dealer_plays_and_settle(state)
    return blackjack_page(state)

@route
def blackjack_double(state: State) -> Page:
    '''Double the bet, take exactly one card, then stand.'''
    player = state.players[0]
    if (not state.game_over and len(player.cards) == 2
            and state.chips >= state.bet):
        state.chips -= state.bet
        state.bet *= 2
        player.cards.append(state.deck.pop())
        if hand_value(player.cards) > 21:
            player.result = "Bust"
            finish_blackjack(state, "lose", "You doubled down... and busted. Bold. Very bold.")
        else:
            dealer_plays_and_settle(state)
    return blackjack_page(state)

# ----------------------------------------------------------------------
# ROULETTE (number 35:1, dozens 2:1, everything else 1:1)
# ----------------------------------------------------------------------

RED_NUMBERS = [
    1, 3, 5, 7, 9, 12, 14, 16, 18,
    19, 21, 23, 25, 27, 30, 32, 34, 36
]
ROULETTE_BETS = [
    "Number", "Red", "Black", "Odd", "Even",
    "Low (1-18)", "High (19-36)",
    "1st Dozen (1-12)", "2nd Dozen (13-24)", "3rd Dozen (25-36)"
]

def roulette_result(bet_type: str, pick: str, number: int) -> tuple[bool, int]:
    '''Return (did the bet win, payout multiplier).'''
    if bet_type == "Number":
        return int(pick) == number, 35
    dozens = ["1st Dozen (1-12)", "2nd Dozen (13-24)", "3rd Dozen (25-36)"]
    if bet_type in dozens:
        low = dozens.index(bet_type) * 12 + 1
        return low <= number <= low + 11, 2
    if number == 0: #zero beats every outside bet
        return False, 1
    if bet_type == "Red":
        return number in RED_NUMBERS, 1
    if bet_type == "Black":
        return number not in RED_NUMBERS, 1
    if bet_type == "Odd":
        return number % 2 == 1, 1
    if bet_type == "Even":
        return number % 2 == 0, 1
    if bet_type == "Low (1-18)":
        return number <= 18, 1
    return number >= 19, 1

@route
def roulette(state: State) -> Page:
    '''Display the roulette betting page.'''
    if state.chips <= 0:
        return broke_page(state)
    return Page(state, chip_bar(state) + [
        Header("ROULETTE"),
        "Welcome, " + state.player_name + "! The wheel is thirsty.\n\n",
        "Choose your type of bet:",
        SelectBox("bet_type", ROULETTE_BETS, "Number"),
        "\n",
        "Choose a number if you selected Number (35 to 1!):",
        SelectBox(
            "roulette_bet",
            [str(number) for number in range(37)],
            state.roulette_bet
        ),
        "\n"
    ] + bet_picker(state) + [
        Button("Spin the Wheel", "spin_roulette"),
        Button("Return to Casino", "index")
    ])

@route
def spin_roulette(
    state: State, bet_type: str, roulette_bet: str, bet_amount: str
) -> Page:
    '''Spin the wheel and evaluate the selected bet.'''
    bet = parse_bet(bet_amount, state.chips)
    if bet <= 0:
        return broke_page(state)
    state.chips -= bet
    state.roulette_bet = roulette_bet
    state.bet_type = bet_type
    state.roulette_number = randint(0, 36)
    state.current_round = "Roulette"
    state.game_over = True
    number = state.roulette_number
    won, multiplier = roulette_result(bet_type, roulette_bet, number)
    if won:
        state.chips += bet * (multiplier + 1)
        net = bet * multiplier
        state.message = "Your bet won! YIPPEE :)"
        if bet_type == "Number" and number == 0:
            unlock(state, "Zero Hero")
    else:
        net = -bet
        state.message = "Your bet lost :("
    record(state, net)
    if number == 0:
        color = "Green"
    elif number in RED_NUMBERS:
        color = "Red"
    else:
        color = "Black"
    content = chip_bar(state) + [
        Header("ROULETTE RESULTS"),
        "Bet type: " + bet_type + "   |   Wager: " + format(bet, ",") + " chips",
        "\n"]
    if bet_type == "Number":
        content.append("Your number selection: " + roulette_bet + "\n")
    content.extend([
        "\nWinning number: " + str(number) + " (" + color + ")\n",
        Image(roulette_images[number]),
        "\n\n",
        state.message,
        "\n",
        net_text(net),
        "\n",
        outcome_line(net),
        "\n\n"
    ])
    if state.chips > 0:
        content.append(Button("Play Again", "roulette"))
    else:
        content.append(Button("🎁 Beg for Chips", "free_chips"))
    content.append(Button("Return to Casino", "index"))
    return Page(state, content)

# ----------------------------------------------------------------------
# SLOT MACHINE (new!)
# ----------------------------------------------------------------------

#more cherries than sevens, so jackpots are rare (like in real life)
SLOT_SYMBOLS = (
    ["🍒"] * 6 + ["🍋"] * 5 + ["🔔"] * 4 + ["⭐"] * 3 + ["💎"] * 2 + ["7️⃣"]
)
SLOT_PAYS = {"🍒": 5, "🍋": 8, "🔔": 15, "⭐": 30, "💎": 75, "7️⃣": 250}

@route
def slots(state: State) -> Page:
    '''Slot machine betting page.'''
    if state.chips <= 0:
        return broke_page(state)
    return Page(state, chip_bar(state) + [
        Header("🎰 LUCKY LEMON SLOTS 🎰"),
        "Three matching symbols win. Two cherries pay double.\n",
        "Three 7️⃣ pays 250x. The odds of that are... let's not talk about the odds.\n\n"
    ] + bet_picker(state) + [
        Button("PULL THE LEVER", "spin_slots"),
        Button("Return to Casino", "index")
    ])

@route
def spin_slots(state: State, bet_amount: str) -> Page:
    '''Spin three reels and pay out.'''
    bet = parse_bet(bet_amount, state.chips)
    if bet <= 0:
        return broke_page(state)
    state.chips -= bet
    reels = [choice(SLOT_SYMBOLS) for _ in range(3)]
    if reels[0] == reels[1] == reels[2]:
        multiplier = SLOT_PAYS[reels[0]]
    elif reels.count("🍒") == 2:
        multiplier = 2
    else:
        multiplier = 0
    payout = bet * multiplier
    state.chips += payout
    net = payout - bet
    if reels == ["7️⃣", "7️⃣", "7️⃣"]:
        unlock(state, "Lucky Seven")
        message = "JACKPOT!!! Sirens! Confetti! A man in a suit is walking over!"
    elif multiplier >= 15:
        message = "BIG WIN! The machine coughs up chips like it owes you money."
    elif multiplier > 0:
        message = "A winner! The machine is annoyed but pays up."
    else:
        message = choice([
            "Nothing. The machine hums smugly.",
            "So close! (It was not close.)",
            "The lemon giveth, and the lemon taketh away.",
            "The machine says: 'thank you for your donation.'"
        ])
    record(state, net)
    content = chip_bar(state) + [
        Header("🎰 " + "  |  ".join(reels) + " 🎰"),
        message,
        "\n",
        net_text(net),
        "\n\n"
    ]
    if state.chips > 0:
        content.extend(bet_picker(state))
        content.append(Button("Spin Again", "spin_slots"))
    else:
        content.append(Button("🎁 Beg for Chips", "free_chips"))
    content.append(Button("Return to Casino", "index"))
    return Page(state, content)

start_server(State(
    game_type="",
    player_name="",
    players=[],
    community_cards=[],
    dealer_cards=[],
    deck=[],
    player_count=2,
    current_round="Menu",
    message="Welcome to the casino!",
    game_over=False,
    roulette_number=0,
    roulette_bet="0",
    bet_type="Number",
    community_stage=0,
    chips=STARTING_CHIPS,
    bet=0,
    pot=0,
    current_bet=0,
    min_raise=20,
    turn=0,
    raises=0,
    stage_index=0,
    hand_log=[],
    achievements=[],
    hands_played=0,
    hands_won=0,
    biggest_win=0,
    net_profit=0,
    begs=0,
    last_net=0,
    toast=""
))


