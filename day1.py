'''
--- Day 1: Calorie Counting ---
Santa's reindeer typically eat regular reindeer food, but they need a lot of magical energy to deliver presents on Christmas. For that, their favorite snack is a special type of star fruit that only grows deep in the jungle. The Elves have brought you on their annual expedition to the grove where the fruit grows.

To supply enough magical energy, the expedition needs to retrieve a minimum of fifty stars by December 25th. Although the Elves assure you that the grove has plenty of fruit, you decide to grab any fruit you see along the way, just in case.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

The jungle must be too overgrown and difficult to navigate in vehicles or access from the air; the Elves' expedition traditionally goes on foot. As your boats approach land, the Elves begin taking inventory of their supplies. One important consideration is food - in particular, the number of Calories each Elf is carrying (your puzzle input).

The Elves take turns writing down the number of Calories contained by the various meals, snacks, rations, etc. that they've brought with them, one item per line. Each Elf separates their own inventory from the previous Elf's inventory (if any) by a blank line.

For example, suppose the Elves finish writing their items' Calories and end up with the following list:

1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
This list represents the Calories of the food carried by five Elves:

The first Elf is carrying food with 1000, 2000, and 3000 Calories, a total of 6000 Calories.
The second Elf is carrying one food item with 4000 Calories.
The third Elf is carrying food with 5000 and 6000 Calories, a total of 11000 Calories.
The fourth Elf is carrying food with 7000, 8000, and 9000 Calories, a total of 24000 Calories.
The fifth Elf is carrying one food item with 10000 Calories.
In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: they'd like to know how many Calories are being carried by the Elf carrying the most Calories. In the example above, this is 24000 (carried by the fourth Elf).

Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?

Your puzzle answer was 71924.

--- Part Two ---
By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying the most Calories of food might eventually run out of snacks.

To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the top three Elves carrying the most Calories. That way, even if one of those Elves runs out of snacks, they still have two backups.

In the example above, the top three Elves are the fourth Elf (with 24000 Calories), then the third Elf (with 11000 Calories), then the fifth Elf (with 10000 Calories). The sum of the Calories carried by these three elves is 45000.

Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?

Your puzzle answer was 210406.
'''


def part1():
    calories_max = 0
    calories_temp = 0
    with open('day1.data', 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                calories_temp += float(line)
            else:
                calories_max = calories_temp if calories_temp > calories_max else calories_max
                calories_temp = 0
        # this check must be done when the data does not have a new line at the end
        calories_max = calories_temp if calories_temp > calories_max else calories_max
        calories_temp = 0
    print(f'Max Calories is {calories_max}')

def part2(top_n_cals:int=3) -> None:
    calories = [0 for _ in range(top_n_cals)]
    calories_temp = 0
    with open('day1.data', 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                calories_temp += float(line)
            else:
                # instersion sort (similar to heap where min is always on top)
                for i in range(top_n_cals):
                    #  0 1 2 3 4 5
                    # [1,2,3,4,5,6]
                    # 5.5 so i == 5
                    # [2,3,4,5,5.5,6]

                    #  0 1 2 3 4 5
                    # [1,2,3,4,5,6]
                    # 1.5 so i == 1
                    # [1.5,2,3,4,5,5.5,6]

                    # [1,2,3,4,5,6]
                    # 0.5
                    # [1.5,2,3,4,5,5.5,6]
                    if calories[0] > calories_temp:
                        break
                    elif i != top_n_cals and calories_temp < calories[i]:
                        # splice the list: cut the min off the front, add new temp, add trailing larger cals
                        calories = calories[1:i] + [calories_temp] + calories[i:]
                        break
                    # [1,2,3,4,5,6]
                    # 6.5
                    elif calories_temp > calories[i] and i == top_n_cals-1:
                        # pops off the min cal
                        calories.pop(0)
                        # append the new max cal
                        calories.append(calories_temp)
                        break

                calories_temp = 0
    print(f'Max Calories is {sum(calories)} and the top cals are {calories}')


if __name__ == '__main__':
    part1()
    part2()