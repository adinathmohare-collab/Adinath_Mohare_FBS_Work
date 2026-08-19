# 3. Create a class Shirt with members as sid,sname,type(formal etc), price and
# size(small,large etc) .Add following methods:
# j. Constructor (Support both parameterized and parameterless)
# k. Destructor
# l. ShowShirt
# m. For each size of shirt price should change by 10%.
# (eg. If 1000 is price then small price = 1000, medium = 1100,large=1200 and
# xlarge=1300) Use static concept.

class Shirt:
    increment = 10

    def __init__(self, sid=None, sname=None, type=None, price=None, size=None):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size

    def updatePrice(self):

        if self.size.lower() == "small":
            self.price = self.price

        elif self.size.lower() == "medium":
            self.price = self.price + (self.price * Shirt.increment / 100)

        elif self.size.lower() == "large":
            self.price = self.price + (self.price * 2 * Shirt.increment / 100)

        elif self.size.lower() == "xlarge":
            self.price = self.price + (self.price * 3 * Shirt.increment / 100)

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
s1.updatePrice()
s1.ShowShirt()



# Parameterized Constructor
s2 = Shirt(102, "Linen Shirt", "Casual", 1500, "Medium")

print("Shirt 2 Details")
s2.ShowShirt()
s2.updatePrice()
s2.ShowShirt()
