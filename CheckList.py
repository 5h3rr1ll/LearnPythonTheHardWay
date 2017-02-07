# -*- coding: utf-8 -*-
LessonIndex = [1,2,3]
UserInput = raw_input("Welche Lektion hast du gerade gemacht? ")


if UserInput in LessonIndex:
    print "haste schon"
else:
    print """Ah, die Lektion hattest du noch nicht. Ich füge Sie die Liste
    bereits absolvierten Lektionen."""
