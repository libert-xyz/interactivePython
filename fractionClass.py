from fractions import Fraction
from fractions import gcd

class Fractions:

    def __init__(self,top,bottom):

        self.num = top
        self.den = bottom

    def __str__(self):

        return str(self.num)+"/"+str(self.den)


    def __add__(self,other):

        #gcdres = gcd(self.num,other.den)
        #newnum = (gcdres/self.den * self.num) + (gcdres/other.den * other.num)
        #newden = gcdres
	
	
	newden = self.den * other.den
	newnum = ((newden/self.den) * self.num) + ((newden/other.den) * other.num)

        return Fractions(newnum,newden)
