import os
os.system("del starttime.txt")
file1 = open('time_spent.txt','w')
file1.write("0\n")
file1.close()
print("Reset done")