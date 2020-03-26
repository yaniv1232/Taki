
N = 0
while int(N) not in range(2, 7):
    N = input("Enter a number between 2 to 6: ")
deck = set()
scores = list()
for i in range(40):
    deck.add(str(i+1))
for i in range(int(N)):
    card_text = deck.pop()
    card_number = int(card_text)
    scores.append(card_number)
    curr_player_index = str(i+1)
    curr_player_score = str(scores[i])
    print(f"Player {curr_player_index} draw {curr_player_score}")
winner_index = str(scores.index(max(scores)) + 1)
winner_score = str(max(scores))
print(f"Player {winner_index} is the winner with {winner_score} points")



