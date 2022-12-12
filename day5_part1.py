from aocd import get_data, submit

data = get_data(day=5, year=2022).splitlines()

def move_containers(To, From, Amount):
    for i in range(Amount):
        containers[To - 1].insert(0, containers[From - 1].pop(0))

# create nested list the size of the stack of containers
# _ is a general purpose throwaway variable
containers = [[] for _ in range(9)]

# populate the stacks of containers
for i in data[0:8]:
    containers[0].append(i[0:3])
    containers[1].append(i[4:7])
    containers[2].append(i[8:11])
    containers[3].append(i[12:15])
    containers[4].append(i[16:19])
    containers[5].append(i[20:23])
    containers[6].append(i[24:27])
    containers[7].append(i[28:31])
    containers[8].append(i[32:35])

# remove empty values
containers = [[v for v in i if v != '   '] for i in containers]

# move them around!
for i in data[10:]:
    i = i.split(' ')
    Amount_i = int(i[1])
    From_i = int(i[3])
    To_i = int(i[5])
    move_containers(To_i, From_i, Amount_i)

# find the first container on the stac
first_on_stack = [i[0] for i in containers]

# parse into answer
first_on_stack = [i.removeprefix('[')  for i in first_on_stack]
first_on_stack = [i.removesuffix(']') for i in first_on_stack]
first_on_stack = ''.join(first_on_stack)
print(first_on_stack)


if __name__ == '__main__':                                                             
    submit(first_on_stack, part = 1, day = 5, year = 2022)


