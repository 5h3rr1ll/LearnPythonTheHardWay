# -*- coding: utf-8 -*-
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Capnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# Achtung! Die kommenden Zeilen sind eine Endlosschleife!
# while True:
#     counter = 0
#     for i in ["/", "-", "|", "\\", "|"]:
#         print "%s\r" % i
#         counter += 1
#         if counter < 4:
#             print counter
#         else:
#             break
