import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoSpeak 1.1. Created by Namrah Juweria Sayed")

    command = pyttsx3.init()

    while(True):
        x = input("Enter what you want me to say: ")
        if x == "q":
            message = "Thank you and goodbye friend!"
            command.say(message)
            command.runAndWait()
            break
        command.say(x)
        command.runAndWait()








