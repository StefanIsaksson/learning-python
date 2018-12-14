def main():

    box_id_list= get_box_id_list()

    checksum = calculate_checksum(box_id_list)

    print(f'Checksum for list Box IDs is {checksum}')


def get_box_id_list():
    box_id_list = []

    with open("input.txt", "r") as file:
        for line in file:
            box_id = line.rstrip('\n')
            box_id_list.append(box_id)

    return box_id_list


def calculate_checksum(box_id_list):
    two_same_letters = 0
    three_same_letters = 0

    for box_id in box_id_list:
        char_frequency = get_char_frequency(box_id)

        if 2 in char_frequency.values():
            two_same_letters += 1

        if 3 in char_frequency.values():
            three_same_letters += 1

    return two_same_letters * three_same_letters


def get_char_frequency(box_id):
    char_frequency = {}
    for char in box_id:
        if char in char_frequency:
            char_frequency[char] = char_frequency[char] + 1
        else:
            char_frequency[char] = 1
    return char_frequency


if __name__ == '__main__':
    main();
