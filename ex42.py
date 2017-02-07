#! /usr/bin/env python
# -*- coding: utf-8 -*-

## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is a ClassInstanz of Animals. Dog Instanz has a name.
class Dog(Animal):

    def __init__(self, name):
        ## A varibale which contains the name
        self.name = name

## Cat is ClassInstanz of Animals. Cat instance has a name.
class Cat(Animal):

    def __init__(self, name):
        ## A varibale which contains the name
        self.name = name

## Personen is a class of object. Person Class has a name and a pet.
class Person(object):

    def __init__(self, name):
        ## A varibale which contains the name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is a ClassInstance of Person. Employee has a name and a salary
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)# This line, somehow, takes the name
        #variable from the class Person(object).
        ## A variable which contains probaly a nuber for the salary
        self.salary = salary

## Is a class of objekt.
class Fish(object):
    pass

## Is a ClassInstance of fisch
class Salmon(Fish):
    pass

## Is a object from Fish-Class
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## Satan is-a Cat.
satan = Cat("Satan")

## Mary is-a Person
mary = Person("Mary")

## Satan is-a pet of Mary. Mary has-a cat, named Satan. Satan is-a Cat.
mary.pet = satan

## Frank is-a Employee
frank = Employee("Frank", 120000)

## Frank has-a pet, named rover. Rover is-a Dog
frank.pet = rover

## Flipper is-a Fish.
flipper = Fish()

## Crouse is-a Salmon
crouse = Salmon()

## Harry is-a Halibut
harry = Halibut()
