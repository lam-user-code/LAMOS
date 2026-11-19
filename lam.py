import datetime
import os


def color_matric():
  os.system("color 0A")


def color_yellow():
  os.system("color 0E")


print("LAM by memolfe\n 0.1.2")
print("devlog 0.1.2: type 'devlog'")

while True:
  choice = input("choice action ")

  if choice == ("custom"):
    color = input("choice text color: matric, yellow")

    if color == ("matric"):
      color_matric()
    if color == ("yellow"):
      color_yellow()

  elif choice == ("help"):
    print("commands: help, custom, time, devlog, exit, clear, echo")

  elif choice == ("time"):
    datetime.datetime.now()
    print(datetime.datetime.now())
  elif choice == ("devlog"):
    print("0.1.2: new commands: exit, clear, echo")
  elif choice == ("echo"):
    echo = input("type")
    print(echo)
  elif choice == ("clear"):
    os.system('cls')
  elif choice == "exit":
    break
  else:
    print("idk, type 'help' ")
