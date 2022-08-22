class Myclass(object):
	def infor(self):
		print("this is a class")

myclass = Myclass()
myclass.infor()

class Bird():
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print('Aaaah...')
            self.hungry = False
        else:
            print('No,thanks!')
b1=Bird()
b1.eat()
b1.eat()

class Bird_son(Bird):
    def eat(self):
        if self.hungry:
            print('Yaaah...')
            self.hungry = False
        else:
            print('Noooo...')
    def sleep(self):
        print('Whooo...')

b_son = Bird_son()
b_son.eat()
b_son.eat()
b_son.sleep()

del b_son
b_son.eat()