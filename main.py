

N = input("Enter a number: ")
deck = set()
score_list = list()
for i in range(int(N)):
    deck.add(str(i+1))
for i in range(int(N)):
    score_list.append(int(deck.pop()))
    print("Player " + str(i+1) + " draw " + str(score_list[i]))
print("Player " + str(score_list.index(max(score_list))+1) + " is the winner with " + str(max(score_list)) + " points")




