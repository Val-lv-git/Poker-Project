from poker.cards import create_deck, parse_card

deck = create_deck()
print(len(deck))  
print(deck)      
print(parse_card("Ah"))