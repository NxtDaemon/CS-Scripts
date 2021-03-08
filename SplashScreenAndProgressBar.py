import os
import time

def splash_screen(seconds):
  print("\n")
  print(" ***********************")
  print(" *                     *")
  print(" *    SPLASH SCREEN    *")
  print(" *        v1.0         *")
  print(" *                     *")
  print(" ***********************")
  time.sleep(seconds)
  os.system('cls')  # CLS for windows , Clear for Linux / OS X
  
  
# Main Program Starts Here....
splash_screen(3)
# username=input("Type your username:")

def progress_bar(seconds):
  for progress in range(0,seconds+1):
    percent = (progress * 100) // seconds
    print("\n")
    print("Loading...")
    print("<" + ("=" * progress) + (" " * (seconds-progress)) + "> " + str(percent) + "%")
    print("\n")
    time.sleep(1)
    os.system('cls')  
  
  
#Main Program Starts Here....
progress_bar(10)
