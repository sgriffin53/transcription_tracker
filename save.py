# record format:
# date | time spent (secs) | file duration (mins) | rate per audio min | rate per hour

from datetime import date
today = date.today()
date_str = today.strftime("%d-%m-%y")
file1 = open('file_rate.txt','r')
lines = file1.readlines()
file1.close()
file_rate = float(lines[0].replace("\n",""))

ff = open('file_length_mins.txt','r')
lines = ff.readlines()
file_length = float(lines[0].replace('\n',''))
ff.close()
#print(file_length)
ff = open('time_spent.txt','r')
lines = ff.readlines()
time_spent = round(float(lines[0].replace('\n','')),2)
ff.close()
total_pay = file_length * file_rate
rate_per_hour = (total_pay / time_spent) * 60 * 60
#print(rate_per_hour)
print("Date:", date_str)
print("File length:", file_length, "minutes")
print("Time spent:",round((round(time_spent,2) / 60),2), "minutes")
print("Total pay: £" + str(round(total_pay,2)))
print("Rate per hour: £" + str(round(rate_per_hour,2)))
print("")
do_save = input("Save this record (y/n)? ")
if do_save[0] == 'y':
    line = date_str + "|" + str(time_spent) + "|" + str(file_length) + "|" + str(file_rate) + "|" + str(round(rate_per_hour,2))
    ff = open('record.txt','a')
    ff.write(line + '\n')
    ff.close()
    print("Record saved.")