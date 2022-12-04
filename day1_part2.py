## Part 2 ## 
import day1_part1 as day1

food = day1.food_sums( )
sort_food = sorted(food, reverse = True)
top_three = sort_food[0:3]
answer = sum(top_three)

if __name__ == '__main__':
    print(answer)
    # day1.submit(answer)
