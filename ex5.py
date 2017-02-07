# -*- coding: utf-8 -*-
name = "Anthony"
age = 32 #Jahre
height = 74 #inches
weight = 180 #punds
eyes = "Brown"
teeth = "White"
hair = "Brown"

in_Centimeters = height / 0.393701
in_Kilograms = weight / 2.20462

print "Let's talk about %s" % name
print "He is %d inches tall" % height
print "He's %d kilo heavy" % weight
print "Actually that's not too heavy"
print "He's got %s eyes and %s hair" % (eyes, hair)
print "His teeth are usually %s depending in the coffee." % teeth

print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

print "Das entspricht %r Kilogramm." % in_Kilograms
print "Das entspricht %r Zentimeter" % in_Centimeters
