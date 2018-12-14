def main():

    box_id_list= get_box_id_list()

    common_letters = find_common_letters_for_two_box_id_which_differ_with_only_one_char(box_id_list)

    print(f'Common letters are {common_letters}')


def get_box_id_list():
    box_id_list = []

    with open("input.txt", "r") as file:
        for line in file:
            box_id = line.rstrip('\n')
            box_id_list.append(box_id)

    return box_id_list


def find_common_letters_for_two_box_id_which_differ_with_only_one_char(box_id_list):
    length_of_box_id = len(box_id_list[0])

    for char_position in range(length_of_box_id):
        box_id_list_with_a_deleted_char = get_box_id_list_with_a_deleted_char(box_id_list, char_position)

        try:
            first_repeating_box_id = find_first_repeating_box_id(box_id_list_with_a_deleted_char)
            return first_repeating_box_id
        except ValueError as err:
            print(f'No repeating box_id found by deleting char at positin {char_position}')


def get_box_id_list_with_a_deleted_char(box_id_list, char_position):
    box_id_list_with_a_deleted_char = []
    for box_id in box_id_list:
        reduced_box_id = box_id[:char_position] + box_id[char_position+1:]
        box_id_list_with_a_deleted_char.append(reduced_box_id)
        print(f'Original {box_id}, removing char at position {char_position} and reduced {reduced_box_id}')

    return box_id_list_with_a_deleted_char


def find_first_repeating_box_id(box_id_list):
    box_id_frequency = {}
    for box_id in box_id_list:
        if box_id in box_id_frequency:
            return box_id
        else:
            box_id_frequency[box_id] = 1

    raise ValueError('No repeating box_id found!')


if __name__ == '__main__':
    main();
