
from os.path import exists

from_file, to_file = sample.txt, 

print "Copying from %s to %s" % (from_file, to_file)

in_file = open(from_file)
inData = in_file.read()

print "The input file is %d bytes long" % len(inData)


print "Does the output file exist?  %r" % exists(to_file)
print "Ready, hit RETURN to continue, or CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(inData)
out_file.close()

print "complete!"

check = open(out_file, 'r')
print check.read()
print "\n"

print in_file.read()


out_file.close()
