from replit import audio
import os, time

#function to play the audio file 
def play():
  source = audio.play_file('audio.wav')
  source.paused = False # unpause the playback
  print("Audio playback started. Press 2 anytime to pause.")
  print()
  while True:
    # Start taking user input and doing something with it
    user_input = int(input("Press 1 to unpause. Press 2 to pause. Press 3 to exit. \nPress anything else to continue.\n"))
    print()
    if user_input == 1:
      source.paused = False
    elif user_input == 2:
      source.paused = True
    elif user_input == 3:
      source.paused = True
      break
    else:
      continue

# Function to display the main menu
def main_menu():
  time.sleep(3)
  os.system("clear")
  print("🎵 MyPod Music Player")
  print("\nPress 1 to Play")
  print("Press 3 to Exit")
  print("\nPress anything else to see the menu again.")
  print()

# Main Program Loop 
def main():
  while True:
    main_menu()
    print()
    user_input = int(input("> "))
    if user_input == 1:
      play()
    elif user_input == 3:
      print("Exiting MyPod Music Player. Goodbye!")
      exit()
    else:
      continue

main()
