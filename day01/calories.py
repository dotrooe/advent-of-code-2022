from utils.file_utils import read_list


def main():
    puzzle_input = read_list('input.txt')
    int_puzzle_input = []
    for el in puzzle_input:
        if el == '':
            int_puzzle_input.append('next')
        else:
            int_puzzle_input.append(int(el))
    print(int_puzzle_input)
    # for el in puzzle_input:
    #     print(el)
    calories = count_calories(int_puzzle_input)
    result_1 = max(calories)
    print(result_1)
    top_3 = part2(calories)
    print(top_3)


def count_calories(arr: list):
    calories_count = []
    current_calories_count = 0
    for el in arr:
        if el != 'next':
            current_calories_count += el
        elif el == 'next':
            calories_count.append(current_calories_count)
            current_calories_count = 0
    calories_count.append(current_calories_count)
    return calories_count


def part2(arr: list):
    highest_calories_count = 0
    second_highest_cal = 0
    third_highest_cal = 0
    for el in arr:
        if el < third_highest_cal:
            continue
        if el > highest_calories_count:
            second_highest_cal = highest_calories_count
            highest_calories_count = el
        if highest_calories_count > el > second_highest_cal:
            third_highest_cal = second_highest_cal
            second_highest_cal = el
        if second_highest_cal > el > third_highest_cal:
            third_highest_cal = el
    return highest_calories_count + second_highest_cal + third_highest_cal


if __name__ == '__main__':
    main()
