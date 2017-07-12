from os.path import exists

from_file, to_file = "sample.txt", "test.txt"

print "Copying from %s to %s\n" % (from_file, to_file)

in_file = open(from_file)
inData = in_file.read()

print "The input file is %d bytes long\n" % len(inData)

print "Does the output file exist?  %r\n" % exists(to_file)
print "Ready, hit RETURN to continue, or CTRL-C to abort.\n"

raw_input()

out_file = open(to_file, 'w')
out_file.write(inData)
out_file.close()

print "complete!\n"

check = open(to_file, 'r')
print check.read() + "\n"
print "\n"

print in_file.read() + "\n"


out_file.close()
