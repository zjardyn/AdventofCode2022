from aocd import get_data, submit

data = get_data(day=3, year=2022).splitlines()

groups = [data[i:i+3] for i in range(0, len(data), 3)]

sum = 0
for i in groups:
    common = list(set.intersection(*map(set, i)))[0]
    if common.isupper():
        sum += ord(common) - 38 
    else:
        sum += ord(common) - 96

if __name__ == '__main__':                                                             
    submit(sum, part = 2, day = 3, year = 2022)
