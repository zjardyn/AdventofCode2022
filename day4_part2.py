from aocd import get_data, submit

data = get_data(day=4, year=2022).splitlines()

def range1(start, end):
    return range(start, end + 1)

sum = 0
for i in data:
    pairs = i.split(",")
    pair_one = pairs[0].split("-")
    pair_two = pairs[1].split("-")
    if pair_one[0] == pair_one[1]:
        pair_one_seq = set([int(pair_one[0])])
    else:
        pair_one_seq = set(range1(int(pair_one[0]), int(pair_one[1])))
    
    if pair_two[0] == pair_two[1]:
        pair_two_seq = set([int(pair_two[0])])
    else:
        pair_two_seq = set(range1(int(pair_two[0]), int(pair_two[1])))
    
    inter = pair_one_seq.intersection(pair_two_seq)
    if inter:
        sum += 1

if __name__ == '__main__':                                                             
    submit(sum, part = 2, day = 4, year = 2022)


