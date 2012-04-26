values = []
pc = 0

def read(table, n, value):
    if (len(table) < n):
        table[n]=value
    else:
        table += [value]
    n += 1
    return

read(values,pc,"potato")
read(values,pc," is")
read(values,pc,"KAWAII!!!")
print values

def hello(this):
    print "hello, world!\n"
    return this
def main():
    print hello("Again!")
if __name__ == '__main__':
    main()
