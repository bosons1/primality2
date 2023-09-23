#!/usr/bin/python3
import sys

def is_prime(num):
    f=open("./pi.txt","r")
    g=open("./e.txt","r")
    f.read(2)
    g.read(2)
    num = str(sys.argv[1])
    nr = 0
    dr = 0
    _num_ = num
    while True:
        ll = len(num)
        pp = str(f.read(ll))
        ee = str(g.read(ll))
        if pp[-1] == num[-1]:
            if pp[-1] == "0":
                nr = nr + 10
            else:
                nr = int(pp[-1])
        if ee[-1] == num[-1]:
            if ee[-1] == "0":
                dr = dr + 10
            else:
                dr = int(ee[-1])
        if dr > 0 and nr == 2*dr:
            return False
        elif nr > 0 and dr == 2*nr:
            return True
        num = str(int(num) + 1)
    f.close()
    g.close()

if __name__ == "__main__":
    num = str(sys.argv[1])
    primality = is_prime(num)
