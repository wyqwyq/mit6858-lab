#!/usr/bin/python

fd = open('shellcodeasm.bin','r')
cont = fd.read()
print "size: %d" % len(cont)
print "type: ", type(cont)
for x in cont:
    if x == ' ':
        print "space",
    #if x == '\n':
    #    print "newline",
    if x == '\r':
        print 'carrage',
    print '0x' + str(ord(x)),
cont = cont[0:len(cont)-1] + '\0'
print cont
print ''
for x in cont:
    print '0x' + str(ord(x)),
print cont
