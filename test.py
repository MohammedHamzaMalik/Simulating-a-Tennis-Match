# test.py

from tennis import Player, Match

nadal = Player("Rafael Nadal")
djokovic = Player("Novak Djokovic")

test_match = Match(nadal, djokovic)

test_match.simulate_match()
test_match.play_match()
