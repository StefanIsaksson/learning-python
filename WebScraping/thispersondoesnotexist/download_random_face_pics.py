import urllib.request
import time
import cv2

def main():
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    urllib.request.install_opener(opener)

    for index_number in range(217,301):
        url = f'https://thispersondoesnotexist.com/image'

        urllib.request.urlretrieve(url, f'big_{index_number}.png')

        img = cv2.imread(f'big_{index_number}.png', cv2.IMREAD_UNCHANGED)
        resized = cv2.resize(img, (200, 210), interpolation = cv2.INTER_AREA)
        cv2.imwrite(f'{index_number}.png', resized)

        time.sleep(10)

if __name__ == '__main__':
    main();
