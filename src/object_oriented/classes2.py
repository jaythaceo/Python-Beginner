#!/usr/bin/env python
#Created by Jaythaceo@gmail.com/ google.com/+ceobrooks
# July 17 2014: Revised October 26, 2014

import math

class Circle:

    def __init__(self, value):
        self.__radius = value

    def setRadius(self, value):
        self.__radius = value

    def getRadius(self, value):
        return self.__radius

    def doArea(self):
        return math.pi * self.__radius * self.__radius

class Rectangle:

    def __init__(self, h, w):
        self.__height = h
        self.__width = w

    def setWidth(self, value):
        self.__width = value

    def setHeight(self, value):
        self.__height = value

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height

    def doArea(self):
        return self.__height * self.__width

class Square:

    def __init__(self, value):
        self.__side = value

    def setSide(self, value):
        self.__side = value

    def getSide(self):
        return self.__side

    def doArea(self):
        return self.__side * self.__side

def Square2(Rectangle):

    def __init__(self, value):
        Rectangle.__init__(self, value, value)

    def setSide(self, value):
        self.__width = value
        self.__height = value

def main():
    jay = Circle(23.5)
    print("The area of a circle with radius",
            jay.getRadius(), "is",
            jay.doArea())

    chris = Rectangle(12.4, 18.1)
    print("The area of a square with side",
            chris.getHeight(), "and width",
            chris.getWidth(), "is",
            chris.doArea())

    ana = Square(3)
    print("The area of a square with side",
            ana.getSide(), "is",
            ana.doArea())
    jason = Square2(4.2)
    print("The area of a square with side",
            jason.getWidth(), "is",
            jason.doArea())

main()

