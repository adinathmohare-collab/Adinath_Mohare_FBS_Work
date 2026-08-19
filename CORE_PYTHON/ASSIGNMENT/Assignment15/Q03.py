# 3. Create a class Shirt with members as sid,sname,type(formal etc), price and
# size(small,large etc) .Add following methods:
# g. Constructor (Support both parameterized and parameterless)
# h. Destructor
# i. ShowShirt

class Shirt:

    def __init__(self, sid=None, sname=None, type=None, price=None, size=None):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size

    def ShowShirt(self):          
        print(f'sid:{self.sid}\tsname:{self.sname}\tType:{self.type}\tPrice:{self.price}\tsize:{self.size}\n')

    def __del__(self):
        print("Shirt object destroyed")


# Parameterless Constructor
s1 = Shirt()

s1.sid = 101
s1.sname = "Cotton Shirt"
s1.type = "Formal"
s1.price = 1200
s1.size = "Large"

print("Shirt 1 Details")
s1.ShowShirt()

print()

# Parameterized Constructor
s2 = Shirt(102, "Linen Shirt", "Casual", 1500, "Medium")

print("Shirt 2 Details")
s2.ShowShirt()