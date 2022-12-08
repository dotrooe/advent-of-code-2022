from utils.file_utils import read_list


def main():
    strategy_input = read_list('input.txt')
    print(calc_strategy(strategy_input))
    print(part2(strategy_input))


def calc_strategy(arr: list):
    score = 0
    for el in arr:
        if el[2] == 'X':
            score += 1
        elif el[2] == 'Y':
            score += 2
        else:
            score += 3
        if el[0] == 'A' and el[2] == 'X' or el[0] == 'B' and el[2] == 'Y' or el[0] == 'C' and el[2] == 'Z':
            # DRAW
            score += 3
        elif el[0] == 'A' and el[2] == 'Y' or el[0] == 'B' and el[2] == 'Z' or el[0] == 'C' and el[2] == 'X':
            # WIN
            score += 6
    return score


def part2(arr: list):
    score = 0
    for el in arr:
        if el[2] == 'Z':
            score += 6
            if el[0] == 'A':
                score += 2
            elif el[0] == 'B':
                score += 3
            else:
                score += 1
        elif el [2] == 'Y':
            score += 3
            if el[0] == 'A':
                score += 1
            elif el[0] == 'B':
                score += 2
            else:
                score += 3
        else:
            if el[0] == 'A':
                score += 3
            elif el[0] == 'B':
                score += 1
            else:
                score += 2
    return score


if __name__ == '__main__':
    main()
