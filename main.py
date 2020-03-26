
p1_scr = 0
p2_scr = 0
deck = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10'}
while len(deck) > 0:
    player1 = deck.pop()
    player2 = deck.pop()
    p1_scr += int(player1)
    p2_scr += int(player2)
    print("Player 1 draw " + player1)
    print("Player 2 draw " + player2)

print("Player 1 score: " + str(p1_scr))
print("Player 2 score: " + str(p2_scr))
if p1_scr > p2_scr:
    print("Player 1 won")
elif p2_scr > p1_scr:
    print("Player 2 won")
else:
    print("It's a draw")



