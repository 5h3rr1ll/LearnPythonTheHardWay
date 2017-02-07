# -*- coding: utf-8 -*-

#Gibt nur den Satz aus
print "I will coun't my chickens:"

#hier wird mit dem Symobol % geprüft wie häufig die 4 in die 30 passt.
#nachdem festegstestllt ist, dass die 4 sieben mal in die 30 passt, wird
#der Rest, der übrig bleibt wieder zurückgegeben, also 2.
#die zwei wird dann zu den 25 addiert, was dann 27 ergibt.
print "Hens", 25 + 30.0 % 4.0
#hier ist interessant: Es gilt grunsätzlich punkt vor Strichrechnung, aber ansonsten
#arbeitet sich der Terminal strikt von links nach rechts. Zuerst nimmt er also
#die 25*3 und dann gibt er den rest zurück, der überig bleibt, wenn die 4 so häufig wie möglich abgezogen wurde.
print "Roosters", 100 - 25 * 3.0 % 4.0
#wieder einfach nur Text
print "Now I will count the eggs:"
#Hier ist zu bemerken, wenn die Zahlen als Integers geschreiben sind, ergibt 1 geteilt durch 4 gleich 0.
print 3 + 2 + 1 - 5 + 4.0 % 2.0 - 1.0 / 4.0 + 6
#wieder nur Text
print "Is it true that 3 + 2 < 5 - 7?"
#Eifnach line
print 3 + 2 < 5 - 7
#man beachte die mehreren Prints, die durch das Komma ausgeführt werden
print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7
#der Rest ist selbsterklärend
print  "Oh, that's why it's False."

print "How aout some more."

print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2
