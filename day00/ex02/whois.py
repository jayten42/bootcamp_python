import sys

args = sys.argv[1:]
if len(args) == 0:
    exit()
elif len(args) > 1:
    exit("ERROR")

arg = args[0]

if not arg.isnumeric():
    exit("ERROR")
number =  int(arg)
if number == 0:
    print("I'm Zero")
elif number % 2 == 0:
    print("I'm Even")
else:
    print("I'm Odd")
