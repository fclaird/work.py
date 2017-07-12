filename = "sample.txt"

print "Opening the file..."
target = open(filename)
print "now I am going to read the text from %r." % filename


print target.read()

print "And finealy we close it."
target.close()
