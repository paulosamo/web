class Human:
    def james(self):
        print("i can walk")

    def tom(self):
        print("i can run")
# hh = Human()
# print(hh.james())
# print(hh.tom())
class Racoon(Human):#human in these case is parent class and Racoon is child class
    def racoon(self):
        print("can smile")
rr = Racoon()
# print(rr.tom())
print(f"{rr.james()} + {rr.tom()} + {rr.racoon()}")