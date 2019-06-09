import urllib.request
import time

def main():
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    urllib.request.install_opener(opener)

    for index_number in range(0,5):
        zero_padded_index_number = str(index_number).zfill(3)
        url = f'https://thispersondoesnotexist.com/image'

        urllib.request.urlretrieve(url, f'{zero_padded_index_number}.png')
        time.sleep(5)


if __name__ == '__main__':
    main();
