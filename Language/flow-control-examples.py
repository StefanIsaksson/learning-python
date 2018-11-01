def while__loop(words):
    index = 0
    while(index < len(words)):
        print(words[index].capitalize())
        index += 1


def for__loop(words):    
    for word in words:
        for letter_index, letter in enumerate(word):
            before_letter = word[:letter_index]
            after_letter = word[letter_index+1:]
            print(letter_index, before_letter + letter.upper() + after_letter)
        print()


def print_even_numbers():
    even_numbers = {x for x in range(10) if x % 2 == 0}
    for x in even_numbers:
        print(x, end=' ')
		
def main():
    words = ['snigel', 'krokodil', 'boll']
    while__loop(words)
    for__loop(words)
    print_even_numbers()

if __name__ == '__main__': main()
