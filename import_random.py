import random as rnd
def num():
    return rnd.uniform(0,1)
print(num)
num()


def dice():
    return rnd.randint(1,6)
print("your dice",dice)
dice()

def random():
        for num in range(5):
                rand = rnd.uniform(5.5,9.5)

                print(rand)
random()

def fruits():
      fruit = ["apple","mango","blueberry","strawberry"]
      choice_random = rnd.choice(fruit)
      print(choice_random)
fruits()

def shuffle():
      cards = ["Ace", "King", "Queen", "Jack", "10", "9"]
      shuffled_card = rnd.shuffle(cards)
      print(shuffled_card)
shuffle()