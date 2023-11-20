ri = input("please enter four digits: ")
res = 0
for n in ri:
    res += int(n)
print (ri[0]+"+"+ri[1]+"+"+ri[2]+"+"+ri[3]+"="+str(res))