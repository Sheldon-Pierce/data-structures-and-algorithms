cat_queue = []
dog_queue = []


class AnimalShelter:
    def enqueue(self, animal):
        if animal.species == 'cat':
            cat_queue.append(animal)
        if animal.species == 'dog':
            dog_queue.append(animal)

    def dequeue(self, pref):
        if pref == 'cat':
            print(cat_queue)
            return cat_queue.pop()
        if pref == 'dog':
            print(dog_queue)
            return dog_queue.pop(0)
        else:
            return None


class Dog:

    def __init__(self):
        self.species = 'dog'
        self.name = 'Wilbur'


class Cat:
    def __init__(self):
        self.species = 'cat'
        self.name = 'Oreo'


if __name__ == '__main__':
    print(dog_queue)
    print(cat_queue)
