# derping with underpants Nick and Gracie
class Derp:
    def __init__(self):
        self.name = "herp"
    def count(self, n=5, name = self.name):
        print name
        print n
        if n == 0:
            return 0
        return self.count(n-1)