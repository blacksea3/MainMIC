# coding: utf-8

f1 = open('data.txt','r')
f2 = open('lat.txt','w+')

oldloc = 0
while True:
#for a in range(55):
    temp1 = f1.read(1)
    if temp1 in ('A','B','C','D','E','F'):
        temp2 = f1.read(1)
        if temp2.isdigit()==True or temp2 in ('A','B','C','D','E','F'):
            temp3 = f1.read(1)
            if temp3 in ('A','B','C','D','E','F'):
                f2.write('\n')
                f2.write(temp1+temp2+temp3)
            else:
                f2.write(temp1+temp2+temp3)
        else:
            f2.write(temp1+temp2)
    else:
        f2.write(temp1)
    #oldloc = f1.tell()
    newloc = f1.tell()
    if oldloc == newloc:
        break
    else:
        oldloc = newloc

f1.close()
f2.close()