from datetime import datetime
Text=input("What did you learn or code today?\n")
try:
    focus=int(input("What is your focus level/energy today (1-10)?\n"))
    if not 1<=focus<=10:
        focus=5
        print("Invalid range!, defaulting to 5")
except ValueError:
    focus=5
    print("Invalid Value!, Defaulting to focus level (5)")
now=datetime.now()
time=now.strftime("%d-%m-%y %H:%M:%S")
with open("dev_diary.txt","a") as file:
    file.write(f"What you learned today is {Text} and your focus level/energy is {focus} at {time}\n")
print("Sucessfully logged!")