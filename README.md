# transcription_tracker
A tracker for use with Express Scribe which tracks your stats while working audio transcription

Before working on a file, run reset.py and enter the duration in the format MM:SS (e.g. 45:20) and the file rate in pounds per audio minute (e.g. 0.50).

When you're about to start working on your file, run main.py. It will track stats such as time spent, audio done and remaining, estimated time remaining, WPM, amount earned, and hourly pay rate.

![r111mmj](https://github.com/user-attachments/assets/42ce3b77-49a5-41ab-bee6-b0137b7ace13)

Press ctrl+c to exit when you're finished or want to take a break, and run main.py again when you resume working.

Once you're finished transcribing, you can save your stats by running save.py.

You can view your all-time stats by running stats.py, which will show your total hours spent, total hours transcribed, total amount made, as well as your average hourly pay rate.
