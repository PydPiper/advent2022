
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