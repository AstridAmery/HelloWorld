import random

hand = ["rock", "paper", "scissors"]

player2 = random.choice(hand)
player1 = random.choice(hand)


def rps(p1, p2):
    # your code here
    winner = {"scissors": "paper", "paper": "rock", "rock": "scissors"}  # scissors 'winning hand' value is paper, etc
    if p1 == p2:
        return 'Draw!'
    elif winner[p1] == p2:       # if the Key^ value of player1's hand is equal to player 2's hand, player1 wins.
        return "Player 1 won!"

    return "Player 2 won!"


print(player1, "v", player2)
print(rps(player1, player2))
