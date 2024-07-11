import win32gui
import os
import keyboard
import time
global current_time
global words
global keystrokes

keystrokes = ''
words = 0

current_time = 0
def keyEvent(e):
    global keystrokes
    global words
    if e.event_type == 'down':
        if e.name == 'space':
            words+=1
            #print("space")

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

if __name__ == '__main__':
    win32gui.EnumWindows(winEnumHandler, None)

    if not os.path.isfile('starttime.txt'):
        file1 = open('starttime.txt', 'w')
        file1.write(str(current_time) + "\n")
        file1.close()
    if not os.path.isfile('word_count.txt'):
        file1 = open('word_count.txt', 'w')
        file1.write("0\n")
        file1.close()
    file1 = open('word_count.txt', 'r')
    lines = file1.readlines()
    file1.close()
    words = int(lines[0].replace("\n",""))
    file1 = open('starttime.txt', 'r')
    lines = file1.readlines()
    file1.close()
    start_time = lines[0].replace("\n","")
    file2 = open('time_spent.txt', 'r')
    lines = file2.readlines()
    file2.close()
    time_spent = int(float(lines[0].replace("\n","")))
    init_time_spent = time_spent
    file1 = open('file_rate.txt','r')
    lines = file1.readlines()
    file1.close()
    file_rate = float(lines[0].replace("\n",""))
    start_audio_time = int(float(start_time))
    start_time = time.time()
    last_updated = time.time()
    keyboard.hook(keyEvent)
    while True:
        time.sleep(0.1)
        if time.time() - last_updated >= 1.5:
            # update

            last_updated = time.time()
            time_spent = init_time_spent + (time.time() - start_time)
            time_spent = int(time_spent)
            file1 = open('time_spent.txt', 'w')
            file1.write(str(time_spent) + "\n")
            file1.close()
            file1 = open('word_count.txt', 'w')
            file1.write(str(words) + "\n")
            file1.close()
            last_current_time = current_time
            win32gui.EnumWindows(winEnumHandler, None)
            audio_done_secs = current_time - start_audio_time
            time_spent_hours = int(time_spent / 60 / 60)
            time_spent_mins = int(time_spent / 60) - time_spent_hours * 60
            time_spent_secs = time_spent - time_spent_mins * 60 - time_spent_hours * 60 * 60
            audio_done_mins = int(audio_done_secs / 60)
            audio_done_secs_show = audio_done_secs - int(audio_done_secs / 60) * 60
            amount_earned = file_rate * (audio_done_secs / 60)
            pay_rate_per_sec = amount_earned / time_spent
            pay_rate = pay_rate_per_sec * 60 * 60
            pay_rate = round(pay_rate,2)

            # estimate time remaining
            audio_secs_per_sec_spent = audio_done_secs / time_spent
            audio_mins_per_min_spent = (audio_done_secs * 60) / (time_spent * 60)
            #file_length_mins = 55.36
            file1 = open('file_length_mins.txt', 'r')
            lines = file1.readlines()
            file_length_mins = float(lines[0])
            file_remaining_mins = file_length_mins - (current_time / 60)
            time_remaining_mins = 60 # default in case audio_mins_per_min_spent is 0
            show_file_remaining_hrs = int(file_remaining_mins / 60) # audio left
            show_file_remaining_mins = int(file_remaining_mins) - show_file_remaining_hrs * 60 # audio left
            if audio_mins_per_min_spent != 0: time_remaining_mins = file_remaining_mins / audio_mins_per_min_spent
            time_remaining_hrs_show = int(time_remaining_mins / 60)
            time_remaining_mins_show = int(time_remaining_mins) - time_remaining_hrs_show * 60
            time_remaining_secs = (time_remaining_mins * 60)
            time_remaining_secs_show = time_remaining_secs - int(time_remaining_mins) * 60
            time_remaining_secs_show = int(float(time_remaining_secs_show))
            time_remaining_mins_show = int(float(time_remaining_mins_show))
            percentage = current_time * 100 / (file_length_mins * 60)
            percentage = round(percentage, 1)
            wpm = int(words / (time_spent / 60))
            os.system("cls")
            print("Time spent: " + str(time_spent_hours) + " hrs " + str(time_spent_mins) + " mins " + str(time_spent_secs) + " secs")
            print("Audio done: " + str(audio_done_mins) + " mins " + str(audio_done_secs_show) + " secs")
            print("Audio left: " + str(show_file_remaining_hrs) + " hrs " + str(show_file_remaining_mins) + " mins")
            print("Time remaining: " + str(time_remaining_hrs_show) + " hrs " + str(time_remaining_mins_show) + " mins " + str(time_remaining_secs_show) + " secs (" + str(percentage) + "%)")
            print("WPM: " + str(wpm))
            print("Amount earned: £" + str(round(amount_earned,2)))
            print("Pay rate: £" + str(pay_rate) + "/hour")