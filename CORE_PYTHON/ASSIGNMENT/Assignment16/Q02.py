# 2. Create a class Product with members as pid,pname,price and quantity .Add following methods:
# e. Constructor (Support both parameterized and parameterless)
# f. Destructor
# g. ShowProduct
# h. Add static member discount.
# i. Provide methods for applying discount on price of product.

class Product:
    discount = 10

    def __init__(self,pid=None,pname=None,price=None,quantity=None):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity
   
    def Discount(self):
        print('Discount is 10%')
        self.price = self.price-(self.price*Product.discount/100)

    def Showproduct(self):
        print(f'pid:{self.pid}\tpname:{self.pname}\tPrice:{self.price}\tquantity:{self.quantity}')

    def __del__(self):
        print('\nproduct object Destructed')

p1 = Product()

p1.pid = 101
p1.pname = "Laptop"
p1.price = 50000
p1.quantity = "10"

print("product 1 details:")
print('Before discount:')
p1.Showproduct()
print('After Discount:')
p1.Discount()
p1.Showproduct()
p2 = Product(102, "Mouse", 700, 25)
print("\nproduct 2 details:")
print('Before discount:')
p2.Showproduct()
p2.Discount()
print('After Discount:')
p2.Showproduct()


    
