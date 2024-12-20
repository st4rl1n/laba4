#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 15:06:57 2024

@author: user
"""

class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        return f"Animal {self.name} makes a sound"
    
class Dog(Animal):
    def speak(self):
        return f"Dog {self.name} is barking"
    
class Cat(Animal):
    def speak(self):
        return f"Cat {self.name} is meowing"
    
my_dog = Dog("Boss")
my_cat = Cat("PushOK")

def animal_speaks(animal):
    print(animal.speak())

[Dog1, Dog2, Dog3, Dog4] = [Dog("kdsad"),Dog("fdsf"),Dog("qwew"),Dog("fffd")]

animal_speaks(Dog3) 
        
