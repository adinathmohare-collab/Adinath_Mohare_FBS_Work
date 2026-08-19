# 2. Create a class Product with members as pid,pname,price and quantity .Add following methods:
# d. Constructor (Support both parameterized and parameterless)
# e. Destructor
# f. Showproduct

class Product:
    def __init__(self,pid=None,pname=None,price=None,quantity=None):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity
   

    def Showproduct(self):
        print(f'pid:{self.pid}\tpname:{self.pname}\tPrice:{self.price}\tquantity:{self.quantity}\n')

    def __del__(self):
        print('product object Destructed')

p1 = Product()

p1.pid = 101
p1.pname = "Laptop"
p1.price = 50000
p1.quantity = "10"

p2 = Product(102, "Mouse", 700, 25)
print("product 1 details:")
p1.Showproduct()
print("\nproduct 2 details:")
p2.Showproduct()

    