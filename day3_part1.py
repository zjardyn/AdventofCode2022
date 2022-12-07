from aocd import get_data, submit

data = get_data(day=3, year=2022).splitlines()

sum = 0
for rucksack in data: 
    compartment_split = len(rucksack)//2
    first_compartment, second_compartment = rucksack[:compartment_split], rucksack[compartment_split:]
    common_item = ''.join(set(first_compartment).intersection(second_compartment))
    if common_item.isupper():
        sum += ord(common_item) - 38 
        # print(ord(common_item) - 38)
        # print(common_item)
    else:
        sum += ord(common_item) - 96
        # print(ord(common_item) - 96)
        # print(common_item)
   
if __name__ == '__main__':                                                             
    submit(sum, part = 1, day = 3, year = 2022)
 
