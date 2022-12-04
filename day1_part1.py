# module to load and submit
from aocd import lines, submit

# input of question
food = lines

## Part One ##

def food_sums():

    # find the number of breaks, which will be the number of elves + 1
    breaks = 0
    for i in food:
        if i == '':
            breaks += 1
    # create a list of empty lists equal to the number of elves         
    lst = [[] for _ in list(range(breaks + 1))]

    # append calories to empty list, each time there is a break, go to next empty list
    counter = 0
    for i in food:
        if i == '':
            counter += 1
            continue
        lst[counter].append(i)

    # cast to int
    lstint = [list(map(int, i)) for i in lst]

    # Sum each sublist and find the max 
    sums = []
    for i in lstint:
        sums.append(sum(i))

    return sums


if __name__ == '__main__':
  answer =  max(food_sums())
  print(answer)
  # submit(answer)
