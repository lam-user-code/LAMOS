import datetime
import operator
import os

def color_matric():
  os.system("color 0A")

def color_yellow():
  os.system("color 0E")

def color_red():
  os.system("color 0C")

def color_white():
  os.system("color 0F")

def color_blue():
  os.system("color 09")

print("hi,")
print(os.getlogin())

print(r"""
╭──────────────────────────────────────────────╮
│                                              │
│   ██╗      █████╗ ███╗   ███╗ ██████╗ ███████╗
│   ██║     ██╔══██╗████╗ ████║██╔═══██╗██╔════╝
│   ██║     ███████║██╔████╔██║██║   ██║███████╗
│   ██║     ██╔══██║██║╚██╔╝██║██║   ██║╚════██║
│   ███████╗██║  ██║██║ ╚═╝ ██║╚██████╔╝███████╗
│   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚══════╝
│                                              │
│              LAMOS TERMINAL                  │
│              Version 0.1.4-beta              │
│              Status: Beta                    │
│                                              │
╰──────────────────────────────────────────────╯
""")
while True:
  choice = input("choice action ")

  if choice == ("custom"):
    color = input("choice text color: matric, yellow, red, white, blue")

    if color == ("matric"):
      color_matric()
    if color == ("yellow"):
      color_yellow()
    if color == ("red"):
      color_red()
    if color == ("white"):
      color_white()
    if color == ("blue"):
      color_blue()
  elif choice == ("help"):
    print("commands: help, custom, time, devlog, exit, clear, echo, calc, mkdir, ls, rmdir, cd, pwd")

  elif choice == ("time"):
    datetime.datetime.now()
    print(datetime.datetime.now())

  elif choice == ("devlog"):
    print("0.1.4: new colors for custom: red, white, blue")

  elif choice == ("echo"):
    echo = input("type")

    print(echo)

  elif choice == ("clear"):
    os.system('cls')

  elif choice == ("calc"):
    ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

    a = float(input('first number: '))
    op = input('operator (+, -, *, /): ')
    b = float(input('second number: '))

    print('result:', ops[op](a, b))

  elif choice == "mkdir":
    folder = input("Folder name: ")
    os.mkdir(folder)

  elif choice == "ls":
    print(os.listdir())

  elif choice == "rmdir":
    folder = input("Folder name: ")
    os.rmdir(folder)

  elif choice == "cd":
    folder = input("Directory: ")
    os.chdir(folder)

  elif choice == "pwd":
    print(os.getcwd())

  elif choice == "exit":
    break
  else:
    print("idk, type 'help' ")
