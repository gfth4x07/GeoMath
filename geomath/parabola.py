#Parabola file for the GeoMath library
from geomath import point, line as p, l
import re

class Parabola:
    def __init__(self):
        #These are the initial parabola parameters
        self.vertex = None  # Point
        self.focus = None  # Point
        self.directrix = None  # Line
        self.equation = ""
        #ax**2 + bx + c
        self.a = 0
        self.b = 0
        self.c = 0

    #TODO: create a method to create that will acept any args

    def create_via_equation(self, equation):
        """
        This function is for getting a parabola created by a line equation
        Ex: y = x**2 +2x +3
        """
        # Only identify functions. In case of modification of the regex change the Geomath /test/regex file.
        self.equation = equation
        regex = re.compile(r'y\s*=\s*([\+\-]?\d*x\*\*2)\s*([\+\-]?\d*x)?\s*([\+\-]?\d)?')
        values = regex.findall(equation)[0]
        #y = ax**2 + bx + c
        self.a = 1 if values[0] == "x**2" or "+x**2" else -1 if values[0] == "-x**2" else int(values[0][:-4])
        self.b = 1 if values[1] == "+x" else -1 if values[1] == "-x" else int(values[1][:-1])
        self.c = int(values[2])

        
    def value():
        """
        This function return the equation or given a x return the y or
        given a point will return true or false if the pint is in parabola.
        """
        try:
            x = kwargs["x"]
            y = kwargs["y"]
            return self.a*x**2 + self.b*x + self.c == y

        except:
            try:
                x = kwargs["x"]
                return self.a*x**2 + self.b*x + self.c
            except:
                return self.equation
