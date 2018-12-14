def main():

    frequency_changes = get_frequency_changes()

    repeating_frequency = find_first_repeating_frequency(frequency_changes)

    print(f'First repeating frequency was {repeating_frequency[0]} after {repeating_frequency[1]} changes were applied')


def get_frequency_changes():
    frequency_changes = []

    with open("input.txt", "r") as file:
        for line in file:
            change = int(line.rstrip('\n'))
            frequency_changes.append(change)

    return frequency_changes


def find_first_repeating_frequency(frequency_changes):
    tries = 0
    current = 0;
    history = {0: 1}
    while True:
        for change in frequency_changes:
            tries += 1
            current += change
            if current in history:
                history[current] = history[current] + 1
                return current, tries
            else:
                history[current] = 0

    print(f'Final frequency {current}')


if __name__ == '__main__':
    main();
