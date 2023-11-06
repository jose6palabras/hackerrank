import math

class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __sub__(self, no):
        return Points(self.x - no.x, self.y - no.y, self.z - no.z)
    def dot(self, no):
        return self.x*no.x + self.y*no.y + self.z*no.z
    def cross(self, no):
        return Points(self.y*no.z - self.z*no.y, -(self.x*no.z - self.z*no.x), self.x*no.y - self.y*no.x)        
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)
if __name__ == '__main__':
    a = map(int,input().split())
    b = map(int,input().split())
    c = map(int,input().split())
    d = map(int,input().split())
    A = Points(*a)
    B = Points(*b)
    C = Points(*c)
    D = Points(*d)
    AB = B - A
    BC = C - B
    CD = D - C
    X = AB.cross(BC)
    Y = BC.cross(CD)
    phi = math.acos((X.dot(Y))/(X.absolute()*Y.absolute()))    
    print("%.2f" % math.degrees(phi))