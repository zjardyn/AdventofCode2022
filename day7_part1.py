from aocd import get_data, submit

data = get_data(day=7, year=2022).splitlines()

# point to same object, one changes so does the other
cwd = root = {}

# root[1] = 2
# print(cwd)

# keep track, everytime we go into dir we push old dir onto stack so that when we do 
# cd .. we can pop and go back up one level
stack = []

for line in data:
    line = line.strip()
    # its a command
    if line[0] == "$":
        # either cd or ls
        if line[2] == "c":
            dir = line[5:]
            if dir == "/":
                # go back up to root and clear stack
                cwd = root
                stack = []
            elif dir == "..":
                # removes last element of the stack
                cwd = stack.pop()
            # otherwise go into the dir
            else:
                if dir not in cwd:
                    cwd[dir] = {}
                # push cwd onto stack
                stack.append(cwd)
                cwd = cwd[dir]
