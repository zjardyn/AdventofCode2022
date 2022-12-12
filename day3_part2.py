from aocd import get_data, submit

data = get_data(day=3, year=2022).splitlines()

# split data into nested list; groups of 3 
groups = [data[i:i+3] for i in range(0, len(data), 3)]

sum = 0
for i in groups:
    # more general way to find the intersection among multiple sets
    # have to cast to list and index the character?
    common = list(set.intersection(*map(set, i)))[0]
    # here is the better way 
    if common.isupper():
        sum += ord(common) - ord('A') + 27 
    else:
        sum += ord(common) - ord('a') + 1 

if __name__ == '__main__':                                                             
    submit(sum, part = 2, day = 3, year = 2022)
