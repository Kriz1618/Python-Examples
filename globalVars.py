glovar = 10

def read1():
    print(glovar)

def write1():
    global glovar
    glovar = 5

def write2():
    glovar = 15
    
read1()
write1()
read1()
write2()
read1()