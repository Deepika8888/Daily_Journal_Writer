#Lets create a daily journal writer 

import datetime

print("Welcome to your Daily Journal.")
print(""" Press [1] To add entry 
                [2] To view the journal 
                [3] To delete entry 
                [4] To exit 
      """)


def add():
    entry = input("\n Enter your new entry: ")
    now = datetime.datetime.now()
    formatted_date = now.strftime("%Y-%m-%d %H:%M")
    with open ("Diary.txt", 'a') as file:
        entries = file.write(f"[{formatted_date}] {entry}\n")
    print("Your entry has been added.")

def view():
    try: 
        with open("Diary.txt", "r") as file: 
            entries = file.readlines()

        if not entries:
            print("Your journal is empty.")
        else:
            print("\nYour Journal Entries:")
            for idx, entry in enumerate(entries, start=1):
                print(f"{idx}. {entry.strip()}")
    except FileNotFoundError:
        print("Nothing is here.")


def delete ():
    with open("Diary.txt", "r") as file: 
       entries = file.readlines()
    if not entries:
        print('Your journal is empty.') 
    else: 
        print("\n Your Diary Journal") 
        for idx, entry in enumerate(entries, start=1):
            print(f"{idx}. {entry.strip()}")
    entry_num = int(input("Enter the entry you want to delete."))
    deleted_entry = entries.pop(entry_num-1)
    with open("Diary.txt", "w") as file:
        file.writelines(entries)
    print(f"Deleted entry: {deleted_entry.strip()}")


while True:

    Entry = input("What do you want to do? ")

    if Entry == "1":
        add()
    elif Entry =="2":
        view()
    elif Entry =="3":
        delete() 
    elif Entry == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")



