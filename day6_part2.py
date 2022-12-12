from aocd import get_data, submit

data = get_data(day=6, year=2022).splitlines()
data = data[0]

for i in range(len(data)):
   sub = data[i:i+14] 
   if len(set(sub)) == len(sub):
        answer = i + 14 
        break

if __name__ == '__main__':                                                             
    submit(answer, part = 2, day = 6, year = 2022)
