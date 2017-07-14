# example 20 from learn python the hard way with all print coman ds in the python3 syntax


from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("first lets print the whole file: \n")

print_all(current_file)

print("now we will roll back the tape")

rewind(current_file)

print("Lets print 3 lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)