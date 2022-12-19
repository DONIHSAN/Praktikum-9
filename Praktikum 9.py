def KelvinToFahrenheit(Temperature):
    assert (Temperature >= 0),"Colder than absolute zero!"
    return ((Temperature-273)*1.8)+32
print (KelvinToFahrenheit(273))
print (int(KelvinToFahrenheit(505.78)))
print (KelvinToFahrenheit(-5))

# Menangani Pengecualian

try:
    fh = open("testfile", "w")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print ("Error: can\'t find file or read data")
else:
    print ("Written content in the file successfully")
fh.close()

# Menangani Pengecualian

try:
    fh = open("testfile", "r")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print ("Error: can\'t find file or read data")
else:
    print ("Written content in the file successfully")

# Klausa Coba Akhirnya

try:
   fh = open("testfile", "w")
   fh.write("This is my test file for exception handling!!")
finally:
    print ("Error: can\'t find file or read data")

# Klausa Coba Akhirnya

try:
    fh = open("testfile", "w")
    try:
        fh.write("This is my test file for exception handling!!")
    finally:
     print ("Going to close the file")
     fh.close()
except IOError:
   print ("Error: can\'t find file or read data")

# Argumen Pengecualian

# Define a function here.

def temp_convert(var):
    try:
       return int(var)
    except ValueError (Arguments):
        print ("The argument does not contain numbers\n", Argument)
# Call above function here.
temp_convert("xyz")

# Melempar Pengecualian

def functionName( level ):
    if level < 1:
       raise ("Invalid level!", level)

# The code below to this would not be executed
# if we raise the exception

# Pengecualian yang di tetapkan pengguna

class Networkerror(RuntimeError):
   def __init__(self, arg):
    self.args = arg
try:
   raise Networkerror("Bad hostname")
except Networkerror (e):
    print (e.arg)



