from file_utils import read_list


def main():
    arr = read_list('input.txt')
    print(part1(arr))


def part1(arr: list):
    rucksack_sum = 0
    split_input = []
    common_items = []
    for el in arr:
        split_el = []
        temp1 = ''
        temp2 = ''
        for i in range(len(el) // 2):
            temp1 += el[i]
            temp2 += el[(len(el) // 2) + i]
        split_el.append(temp1)
        split_el.append(temp2)
        split_input.append(split_el)
    # print(split_input)
    for rucksack in split_input:
        common_chars = []
        for char in rucksack[0]:
            if char in common_chars:
                break
            if char in rucksack[0] and char in rucksack[1]:
                common_chars += char
        common_items.extend(common_chars)
    # return common_items
    # return split_input
    for el in common_items:
        if el.islower():
            rucksack_sum += ord(el) - ord('a') + 1
        else:
            rucksack_sum += ord(el) - ord('A') + 27
    return f'the sum of rucksack priorities is {rucksack_sum}'


def part2():
    return 0


if __name__ == '__main__':
    main()
