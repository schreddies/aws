import re
pattern = re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,}")

for i, line in enumerate(open('test.txt')):
    for match in re.finditer(pattern, line):
        print 'Line and password | %s: %s' % (i+1, line) 
