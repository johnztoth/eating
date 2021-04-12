""" agentframework.py """

import random

class Agent():
    """ initialise and move an agent object"""
    
    def __init__ (self,environment):
        
        """ find no. of rows and columns in the environment list """
        self.rows=len(environment)
        self.cols=len(environment[0])
                
        """ initialise the agent object with a randon position """
        self._x = random.randint(0,self.rows-1)
        self._y = random.randint(0,self.cols-1)
        self.env = environment
        self.store = 0 
        
        
    def move(self):
        """ randonly move the agent by one unit in x and y direction """
        """ keeping within boundaries """
        if random.random() < 0.5:
            self._y = (self._y + 1) % self.rows
        else:
            self._y = (self._y - 1) % self.rows

        if random.random() < 0.5:
            self._x = (self._x + 1) % self.cols
        else:
            self._x = (self._x - 1) % self.cols


    def eat(self):
        """ eat 10 units of the environment """
        """ if there are less than 10 units eat them all """
        if self.env[self._y][self._x] > 10:
            self.env[self._y][self._x] -= 10
            self.store +=10
        else:
            self.store += self.env[self._y][self._x] 
            self.env[self._y][self._x] = 0

        """ agent is sick if store greater than 100 """
        if self.store > 100:
            self.env[self._y][self._x] += self.store
            self.store = 0


    def __str__(self) :
        """ override print to print agents location and store """
        return ("y= " + str(self._y) + " x= " + str(self._x)\
                + " store= " + str(self.store))


    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")
    

    def gety(self):
        return self._y

    def sety(self, value):
        self._y = value

    def dely(self):
        del self._y

    y = property(gety, sety, dely, "I'm the 'y' property.")
    
    