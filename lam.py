import os


def color_matric():
  os.system("color 0A")


def color_yellow():
  os.system("color 0E")


print("LAM by memolfe\n 0.1")
print("devlog 0.1: this is first version")
while True:
  choice = input("choice action ")
  if choice == ("custom"):
    color = input("choice text color: matric, yellow")
    if color == ("matric"):
      color_matric()
    if color == ("yellow"):
      color_yellow()
  elif choice == ("help"):
    print("commands: help, custom")
  elif choice == "exit":
    break
  else:
    print("idk, commands: help, custom ")
