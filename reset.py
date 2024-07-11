import os
os.system("del starttime.txt")
file1 = open('time_spent.txt','w')
file1.write("0\n")
file1.close()
file1 = open('word_count.txt','w')
file1.write("0\n")
file1.close()
file1 = open('file_length_mins.txt','w')
file_length = input('File length?:')
if ':' in file_length:
    mins = file_length.split(':')[0]
    secs = file_length.split(':')[1]
    total = float(mins) + (float(secs) / 60)
    file_length = str(round(total,2))
    print(file_length)
file1.write(file_length + "\n")
file1.close()
print("Reset done")