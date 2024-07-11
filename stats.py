ff = open('record.txt','r')
lines = ff.readlines()
ff.close()
total_file_duration = 0
total_time_spent = 0
total_pay = 0
first_date = lines[0].split("|")[0]
for line in lines:
    tokens = line.split("|")
    date_str = tokens[0]
    time_spent = float(tokens[1])
    file_duration = float(tokens[2])
    rate_per_min = float(tokens[3])
    rate_per_hour = float(tokens[4])
    pay = file_duration * rate_per_min
    total_file_duration += file_duration
    total_time_spent += time_spent
    total_pay += pay
    last_date = date_str
avg_pay_per_hour = (total_pay / total_time_spent) * 60 * 60
print("Time period:", first_date,"to",last_date)
print("Total files:", len(lines))
print("Total pay: £" + str(round(total_pay,2)))
print("Total audio done:", str(int(total_file_duration)), "minutes (" + str(round(total_file_duration / 60, 2)) + " hours)")
print("Total time spent:", str(int(round(total_time_spent / 60,0))) + " minutes (" + str(round(total_time_spent / 60 / 60,2)) + " hours)")
print("Average pay rate: £" + str(round(avg_pay_per_hour,2)) + " per hour")