from aocd import get_data, submit 

data = get_data(day=2, year=2022).splitlines()

score = 0
for i in data:
    lst = i.split(' ')

    # you lose
    if lst[1] == "X":
        # they rock
        if lst[0] == "A":
            # you scissor 
            score += 3
        # they paper
        elif lst[0] == "B":
            # you rock 
            score += 1
        # they scissor
        elif lst[0] == "C":
            # you paper
            score += 2
    # you tie
    elif lst[1] == "Y":
        score += 3 
        # they rock
        if lst[0] == "A":
            score += 1
        # they paper 
        elif lst[0] == "B":
            score += 2
        # they scissor 
        elif lst[0] == "C":
            score += 3
    # you win
    elif lst[1] == "Z":
            score += 6 
            # they rock
            if lst[0] == "A":
                # you paper
                score += 2
            # they paper 
            elif lst[0] == "B":
                # you scissor 
                score += 3
            # they scissor 
            elif lst[0] == "C":
                # you rock 
                score += 1


if __name__ == '__main__':                                                             
    submit(score, part = 2, day = 2, year = 2022)
    
