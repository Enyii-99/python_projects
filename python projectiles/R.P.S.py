import random

def play():
    user = input("what's your choice?? 'r' for Rock, 'p' for Paper, 's' for Scissors: ")
    computer = random.choice(["r", "p", "s"])

    if user == computer:
        return "It's a tie!"
    
    if is_win(user, computer):
        return "You won!"
    
    return "You lost!"
    
def is_win(player, opponent):
    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") or (player == "p" and opponent == "r"):
        return True  


print(play())      