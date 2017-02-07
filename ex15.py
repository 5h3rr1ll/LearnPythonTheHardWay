#importing the method argv (argument variable) from the library sys into my code
from sys import argv

"""now I defining which two arguments I want to have set while typing the
filename. So you are forced to type: python ex15.py ArgumentVariable1
ArgumentVariable2"""
script, filename = argv

#since the filename is given at the comandline, open just opens the named file
#and pass it to the variable txt
txt = open(filename)

#Just writes a line of text
print "Here's your file %r:" % filename
#looks like you can't just print the content from the file, you also need to
#.read() to print it out
print txt.read()

#just writes a line of text
print "Type the filename again:"
#getting a input from the user and saves it into the variable "file_again"
file_again = raw_input("> ")

#open the file with the givin name and saves it's content into the variable
#text_again
txt_again = open(file_again)

#prints out the content which was givin to the variable "txt_again". Spent
#attation to the .read()!Won't work without it!
print txt_again.read()

txt.close()
txt_again.close()
