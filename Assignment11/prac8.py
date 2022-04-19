class P1_class:
    def show(self):
        print('inside parant class 1')

class P2_class:
    def display(self):
        print('inside paran class 2')

class Child_class(P1_class,P2_class):
    def show (self):
        print('inside child class')

obj= Child_class()
obj.show()
obj.display()