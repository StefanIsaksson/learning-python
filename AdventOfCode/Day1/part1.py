def main():
    current = 0;

    with open("input.txt", "r") as file:
        for line in file:
            change = int(line.rstrip('\n'))
            print(f'Current frequency {current}, change of {change}; resulting frequency {current + change}.')
            current += change

    print(f'Final frequency {current}')


if __name__ == '__main__':
    main();
