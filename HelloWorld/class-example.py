class Animal:


    def __init__(self, animal_name='No Name'):
        self.animal_name = animal_name


    def speak(self):
        print(f'{self.animal_name} makes animal sounds!')


    def walk(self):
        print(f'{self.animal_name} walks like an animal')


class Horse(Animal):
    def speak(self):
        print('Horse sound!')

    def walk(self):
        print('Horse walk')


class Snake(Animal):

    def walk(self):
        print('Snake walk')		

		
def main():
    horse = Horse()
    horse.speak()
    horse.walk()
    print('hello ', type(horse))
    Snake('Kaa').speak()


if __name__ == '__main__': main()