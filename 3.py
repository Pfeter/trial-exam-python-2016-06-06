# Create a class that represents a cuboid:
# It should take it's three sizes as constructor parameters (numbers)
# It should have a method called `getSurface` that returns the cuboid's surface
# It should have a method called `getVolume` that returns the cuboid's volume
class Cuboid():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def getSurface(self):
        return self.x * self.y * 2 + self.y * self.z * 2 + self.z * self.x *2

    def getVolume(self):
        return self.x * self.y * self.z

# kocka = Cuboid(2,2,2)
# print(kocka.getSurface())
# print(kocka.getVolume())
