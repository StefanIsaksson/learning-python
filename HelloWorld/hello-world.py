import platform

def get_message(user_name):
    return f'Hello {user_name} says Python {platform.python_version()}'

	
def get_border(border_length):
    return '*' * border_length

	
def print_message(message, show_border=True):
    if show_border:
	    border = get_border(len(message))
	    print(border + '\n' + message + '\n' + border)
    else:
        print(message)
    
	
def main():
    user_name = input('What is your name?: ')

    message = get_message(user_name)
    print_message(message=message)


if __name__ == '__main__': main()
