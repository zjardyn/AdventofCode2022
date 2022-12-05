from aocd import get_data, submit 

data = get_data(day=2, year=2022).splitlines()

# First column is :
# A for rock, B for paper, C for scissors

# Second column is what you play in response
# X for rock, Y for paper, Z for scissors 

# score:
# 1 for rock, 2 for paper, 3 for scissors
# plus the outcome of the round: 0 for loss, 3 if draw, 6 if you win
score = 0
for i in data:
    lst = i.split(" ")
    # you roc
    if lst[1] == "X":
        # rock
        score += 1
        # they roc
        if lst[0] == "A":
            # draw
            score += 3
        # they paper
        elif lst[0] == "B":
            # loss 
            continue 
        # they scissors
        elif lst[0] == "C":
            # win
            score += 6
    # you paper
    elif  lst[1] == "Y":
            # paper
            score += 2
            # they rock
            if lst[0] == "A":
                # win
                score += 6
            # they paper
            elif lst[0] == "B":
                # draw 
                score += 3
            # they scissors
            elif lst[0] == "C":
                # lose
                continue
    # you scissors         
    elif  lst[1] == "Z":
            # scissors 
            score += 3
            # they rock
            if lst[0] == "A":
                #  loss
                continue 
            # they paper
            elif lst[0] == "B":
                # win 
                score += 6
            # they scissors
            elif lst[0] == "C":
                # draw
                score += 3

if __name__ == '__main__':                                                             
    # print(score)
    submit(score, day = 2, year = 2022)
