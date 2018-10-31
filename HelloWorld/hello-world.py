import platform

def get_message():
    return f'Hello from Python {platform.python_version()}'

	
def get_border(border_length):
    return '*' * border_length

	
def print_message(message, show_border=True):
    if show_border:
	    border = get_border(len(message))
	    print(border + '\n' + message + '\n' + border)
    else:
        print(message)
    
	
def main():
    message = get_message()
    print_message(message=message)


if __name__ == '__main__': main()
