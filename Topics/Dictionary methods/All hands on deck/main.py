deck = {str(card): card for card in range(2, 11)}
deck.update(Jack=11, Queen=12, King=13, Ace=14)
player_cards = [deck[input()] for _ in range(6)]

print(sum(player_cards) / len(player_cards))
