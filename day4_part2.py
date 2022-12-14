from aocd import get_data, submit

data = get_data(day=4, year=2022).splitlines()

# range with 1-based indexing
def range1(start, end):
    return range(start, end + 1)

sum = 0
for i in data:
    pairs = i.split(",")
    pair_one = pairs[0].split("-")
    pair_two = pairs[1].split("-")
    # if they are just one element long i.e 87-87
    if pair_one[0] == pair_one[1]:
        # have to make iterable by wrapping with []
        pair_one_seq = set([int(pair_one[0])])
    else:
        pair_one_seq = set(range1(int(pair_one[0]), int(pair_one[1])))
    
    if pair_two[0] == pair_two[1]:
        pair_two_seq = set([int(pair_two[0])])
    else:
        pair_two_seq = set(range1(int(pair_two[0]), int(pair_two[1])))
    # find intersection between the sets 
    inter = pair_one_seq.intersection(pair_two_seq)
    # if there is a common element increment a counter
    if inter:
        sum += 1

if __name__ == '__main__':                                                             
    submit(sum, part = 2, day = 4, year = 2022)


