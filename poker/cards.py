RANKS = "23456789TJQKA"  
COLORS = "shdc" # s = spades, h = hearts, d = diamonds, c = clubs

def parse_card(text):
    rank = RANKS.index(text[0])
    color = COLORS.index(text[1])
    return rank + 2, color

def create_deck():
    deck = []
    for i in RANKS:
        for j in COLORS:
            deck.append(i+j)
    return deck
