import sys
import getopt

def myfunction(*args,**kwargs):
    print(args[0])
    print(args[1])
    print(args[2])
    print(args[3])
    print(kwargs['keyone'])
    print(kwargs['keytwo'])

myfunction('hey',True,19,'wow',keyone="test",keytwo=7)

filename = sys.argv[1]
message = sys.argv[2]

with open(filename,'w+') as f:
    f.write(message)

opts , args = getopt.getopt(sys.argv[1:],"f:m:",['filename','message'])

print(opts)
print(args)

for opts , args in opts:
    if opts =='-f':
        filename = args
    if opts == '-m':
        message = args

with open(filename,'w+') as f:
    f.write(message)


# print(sys.argv[1])
