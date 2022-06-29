def l(y):
    if (y % 4) == 0:
        if (y % 100) == 0:
            if (y % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
nly = [0,31, 28, 31, 30, 31, 30,
           31, 31, 30, 31, 30, 31]
ly = [0,31, 29, 31, 30, 31, 30,
          31, 31, 30, 31, 30, 31]
def sum(l,j):
    s=0
    for i in range(j):
        s+=l[i]
    return s
def odd(y,m):
    odd = 0
    if y > 1600:
        for i in range(y - (y % 400) + 1, y):
            if l(i) == True:
                odd += 2
            else:
                odd += 1
        if l(y)==True:
                odd=odd+sum(ly,m)
        else:
            odd=odd+sum(nly,m)
        return (odd+1)%7
print(odd(2010,8))

def calender(y):
    f=open("Calendar.txt","w")
    f.write(str(y).center(67)+"\n")
    month = {1: 'January', 2: 'February', 3: 'March',
             4: 'April', 5: 'May', 6: 'June', 7: 'July',
             8: 'August', 9: 'September', 10: 'October',
             11: 'November', 12: 'December'}
    space=' '
    space=space.rjust(2,' ')
    for j in range(0, 4):
        f.write(month[3 * j + 1].center(22)+ month[3 * j + 2].center(22)+ month[3 * j + 3].center(22)+'\n')
        f.write('Su'+ ' Mo'+ ' Tu'+ ' We'+ ' Th'+' Fr' +' Sa'+ "  "+ ' Su'+ ' Mo'+ ' Tu'+ ' We'+ ' Th'+ ' Fr'+ ' Sa'+ "  "+ ' Su'+' Mo'+' Tu'+ 'We'+ ' Th'+ ' Fr'+ ' Sa'+'\n')
        for p in  range(1,4):
            for i in range(0, odd(y,3*j+p)):
                f.write(space+' ')
            t=3*j+p
            for k in range(1,7-odd(y,t)):
                f.write(str("{:02d}".format(k))+' ')
            for k in range(7-odd(y,t),8-odd(y,t)):
                f.write(str("{:02d}".format(k))+'   ')
        f.write("\n")
        for z in range(1, 6):
            for p in range(1, 4):
                t = 3 * j + p
                for k in range(7*z+1-odd(y,t),7*(z)+8-odd(y,t)):
                    if l(y)==True:
                        if k>=ly[t]+1 and k<7*(z)+7-odd(y,t):
                            f.write(space+' ')
                        elif k<ly[t]+1 and k==7*(z)+7-odd(y,t):
                            f.write(str("{:02d}".format(k))+'   ')
                        elif k>=ly[t]+1 and k==7*(z)+7-odd(y,t):
                            f.write('  '+'   ')
                        else:
                            f.write(str("{:02d}".format(k))+' ')
                    else:
                        if k>=nly[t]+1 and k<7*(z)+7-odd(y,t):
                            f.write(space+' ')
                        elif k<nly[t]+1 and k==7*(z)+7-odd(y,t):
                            f.write(str("{:02d}".format(k))+'   ')
                        elif k>=nly[t]+1 and k==7*(z)+7-odd(y,t):
                            f.write('  '+'   ')
                        else:
                            f.write(str("{:02d}".format(k))+' ')
            f.write("\n")

calender(2021)