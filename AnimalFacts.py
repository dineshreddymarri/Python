print("I will Give you 3 hints,guess what animal I am")
class Animal:
    def __init__(self,name):
        self.name = name
        
    def guess_who_am_i(self):
        if self.name == "elephant":
            questions = ['I have exceptional memory','I am the largest land-Living mammal in the world','I have the big trunk']
        elif self.name == "tiger":
            questions = ['I am the biggest cat','I come in black and white or orange and black','I am the symbol of strength and courage']
        elif self.name == "bat":
            questions = ['I use Echo-location','I can Fly','I see well in dark']
        false_count  = 0
        for quote in questions:
            print(quote)
            input_name = input("Who am I?")
            if (input_name == self.name):
                print("You got it! I am  ",self.name)
                break
            else:
                false_count = false_count + 1
                print("Try Again!!")
                #break
            if false_count == 3:
                print("I am out of Hints! The answer is: ",self.name)
                false_count = 0
        
e= Animal("elephant")
t= Animal("tiger")
b= Animal("bat")
e.guess_who_am_i()
t.guess_who_am_i()
b.guess_who_am_i()
