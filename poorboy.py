import sys
import time

def typewriter_effect(text, delay = 0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    typewriter_effect("Who are you?")

    typewriter_effect("1. Tony Montana")
    typewriter_effect("2. Henry Hill")
    typewriter_effect("3. Lalo Salamanca")

    choice = input("Enter the number corresponding to your choice (1/2/3): ")

    if choice == "1":
        typewriter_effect("You are from Cuba")
    elif choice == "2":
        typewriter_effect("You are from New York")
    elif choice == "3":
        typewriter_effect("You are from Mexico")
    else:
        typewriter_effect("Type the right number!")

    typewriter_effect("What do you desire?")

    typewriter_effect("1. Money")
    typewriter_effect("2. Power")
    typewriter_effect("3. Women")

    choice = input("Enter the number corresponding to your choice (1/2/3): ")

    if choice == "1":
        typewriter_effect("Money cant buy you happines")
    elif choice == "2":
        typewriter_effect("Power will eventually destroys you")
    elif choice == "3":
        typewriter_effect("Women will only come for your money and power")
    else:
        typewriter_effect("Type the right number!")

    
    typewriter_effect("ahahahah just kidding...we need money to get power then we need power to get women")
    typewriter_effect("Aint that right?")
    typewriter_effect("Yeah right")



if __name__=="__main__":
    main()