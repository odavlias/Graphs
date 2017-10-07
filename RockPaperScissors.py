print("Welcome to RockPaperScissors!")
print("")
choice = input("Type start when you are ready: ")

while choice!= "no":
    winner = False
    scoreboard = {}
    scoreboard["p1"] = 0
    scoreboard["p2"] = 0

    while winner==False:
        p1_choice = input("Player 1 choice (rock, paper, scissors): ")
        p2_choice = input("Player 2 choice (rock, paper, scissors): ")
        if p1_choice=="rock" and p2_choice=="rock":
            print("Draw")
        elif p1_choice=="rock" and p2_choice=="paper":
            print("Player 2 gets a point!")
            scoreboard["p2"] += 1
        elif p1_choice=="rock" and p2_choice=="scissors":
            print("Player 1 gets a point!")
            scoreboard["p1"] += 1
        elif p1_choice=="paper" and p2_choice=="rock":
            print("Player 1 gets a point!")
            scoreboard["p1"] += 1
        elif p1_choice=="paper" and p2_choice=="paper":
            print("Draw!")
        elif p1_choice=="paper" and p2_choice=="scissors":
            print("Player 2 gets a point!")
            scoreboard["p2"] += 1
        elif p1_choice=="scissors" and p2_choice=="rock":
            print("Player 2 gets a point!")
            scoreboard["p2"] += 1
        elif p1_choice=="scissors" and p2_choice=="paper":
            print("Player 1 gets a point!")
            scoreboard["p1"] += 1
        elif p1_choice=="scissors" and p2_choice=="scissors":
            print("Draw!")

        if scoreboard["p1"]==3:
            print("Player 1 wins {p1_score} - {p2_score}".format(p1_score= scoreboard["p1"], p2_score= scoreboard["p2"]))
            winner = True
            choice = input("Do you want to play again? (yes/no): ")
        elif scoreboard["p2"]==3:
            print("Player 2 wins {p1_score} - {p2_score}".format(p1_score= scoreboard["p1"], p2_score= scoreboard["p2"]))
            winner = True
            choice = input("Do you want to play again? (yes/no): ")
