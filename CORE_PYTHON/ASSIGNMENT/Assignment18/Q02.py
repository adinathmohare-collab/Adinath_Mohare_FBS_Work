# 2. Create a class Distance with data members as km,m and cm and add following
# methods :
# a. Constructor
# b. Destructor
# c. Overload +,- operator

class Distance:

    def __init__(self, km, m, cm):
        self.km = km
        self.m = m
        self.cm = cm

    def __add__(self, other):
        return Distance(
            self.km + other.km,
            self.m + other.m,
            self.cm + other.cm
        )

    def __sub__(self, other):
        return Distance(
            self.km - other.km,
            self.m - other.m,
            self.cm - other.cm
        )

    def __str__(self):
        return f"{self.km} km {self.m} m {self.cm} cm"

    def __del__(self):
        print("Distance object destroyed")


d1 = Distance(2, 300, 50)
d2 = Distance(1, 700, 25)

print("Distance 1 :", d1)
print("Distance 2 :", d2)

d3 = d1 + d2
print("Addition :", d3)

d4 = d1 - d2
print("Subtraction :", d4)