import win32gui
import os
import time
global current_time

current_time = 0

def winEnumHandler( hwnd, ctx ):
    global current_time
    if win32gui.IsWindowVisible( hwnd ) or True:
        #print ( hex( hwnd ), win32gui.GetWindowText( hwnd ) )
        title = win32gui.GetWindowText( hwnd )
        if "Express Scribe" in title:
            current_time = title.split(" ")[0]
            hours = int(float(current_time.split(":")[0]))
            mins = int(float(current_time.split(":")[1]))
            secs = int(float(current_time.split(":")[2]))
            tot_secs = hours * 60 * 60 + mins * 60 + secs
            current_time = tot_secs

win32gui.EnumWindows( winEnumHandler, None )

if not os.path.isfile('starttime.txt'):
    file1 = open('starttime.txt','w')
    file1.write(str(current_time) + "\n")
    file1.close()
file1 = open('starttime.txt', 'r')
lines = file1.readlines()
file1.close()
start_time = lines[0].replace("\n","")
file2 = open('time_spent.txt', 'r')
lines = file2.readlines()
file2.close()
time_spent = int(float(lines[0].replace("\n","")))
init_time_spent = time_spent
start_audio_time = int(float(start_time))
start_time = time.time()
last_updated = time.time()
while True:
    if time.time() - last_updated >= 1.5:
        # update

        last_updated = time.time()
        time_spent = init_time_spent + (time.time() - start_time)
        time_spent = int(time_spent)
        file1 = open('time_spent.txt', 'w')
        file1.write(str(time_spent) + "\n")
        file1.close()
        last_current_time = current_time
        win32gui.EnumWindows(winEnumHandler, None)
        audio_done_secs = current_time - start_audio_time
        time_spent_hours = int(time_spent / 60 / 60)
        time_spent_mins = int(time_spent / 60) - time_spent_hours * 60 * 60
        time_spent_secs = time_spent - time_spent_mins * 60
        audio_done_mins = int(audio_done_secs / 60)
        audio_done_secs_show = audio_done_secs - int(audio_done_secs / 60) * 60
        amount_earned = 0.50 * (audio_done_secs / 60)
        pay_rate_per_sec = amount_earned / time_spent
        pay_rate = pay_rate_per_sec * 60 * 60
        pay_rate = round(pay_rate,2)
        os.system("cls")
        print("Time spent: " + str(time_spent_hours) + " hrs " + str(time_spent_mins) + " mins " + str(time_spent_secs) + " secs")
        print("Audio done: " + str(audio_done_mins) + " mins " + str(audio_done_secs_show) + " secs")
        print("Pay rate: £" + str(pay_rate) + "/hour")