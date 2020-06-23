
'''
fire
'''
import fire
import os 

def cmd(cmd):
    command={
      "m":['python manage.py makemigrations','python manage.py migrate'],
      's':['python manage.py shell'],
      'r':['python manage.py runserver']
    }
    for item in command[cmd]:
      os.system(item)

if __name__ == "__main__":
    fire.Fire()