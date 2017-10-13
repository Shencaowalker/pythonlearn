#!/home/alex/env/python2.7/bin/python
def normalize(name):
    return "%s" %(name[:1].upper()+name[1:].lower())

L1=['adam','Lisa','barT']
L2=list(map(normalize,L1))
print L2

