# -*- coding: utf-8 -*-
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
# Die Kommas am Ende der Zeile 10, 11, 12 + 13 sind nicht dafür da, dass er alle
# in eine Zeile printet, sondern um genügend Arguemten für die viel Platzhalter
# zu haben!
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
