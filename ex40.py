#! /usr/bin/env python
# -*- coding: utf-8 -*-

class Song(object): # Das argument "object" macht lediglich, dass die Klasse
#direkt die fähigkeit von allen Objekten hat. Objekte ist sozusagen ebenfalls
#eine klasse, die bereits in Python definiert ist.

    def __init__(self, lyrics): # hier die Initiierung defniniert, der Start
    #Was also als Argument übergeben wird, wenn die Klasse Song(Argument)
    #aufgerufen wird, wird in die Variabel "lyrics" gespeichert.
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
#via der Klasse wird nun der Text, innerhalb der Liste in Variablen gespeichert.
#Innerhalb der Klasse in die Variabel "lyrics" im Code wir eine Instanz der Klasse u.a.in die
#Variabel happy_bday gespeichert.
songText1 = ["Happy birthday to you",
"I don't want to get sued",
"so I'll stop right there"]

# hier wollte ich lediglich schauen, ob ich eine Klasse auch benutzen kann, ohne
#erst eine Instanz von ihr zu Erzeugen. Und? geht!
#Song(songText1).sing_me_a_song()

songText2 = ["They rally around tha family",
"With pockets full of shells"]

happy_bday = Song(songText1)

bulls_on_parade = Song(songText2)

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
