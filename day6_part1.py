from aocd import get_data, submit

data = get_data(day=6, year=2022).splitlines()
data = data[0]

for i in range(len(data)):
    # make sure we don't index too far
    if i == len(data) - 3:
        break
    else:
       sub = data[i:i+4] 
    if len(set(sub)) == len(sub):
        answer = i + 4
        break

if __name__ == '__main__':                                                             
    submit(answer, part = 1, day = 6, year = 2022)
