carRunning = False
print("""Welcome to the car simulator! 
Press help to see commands.""")
while True:
    userInput = input("> ").lower()

    if userInput == "help":
        print("start - start the car")
        print("stop - stop the car")
        print("quit - to exit")
        print("check - check if car is running")  # prints out help commands

    elif userInput == "start":
        if carRunning:
            print("Car is already running.")
        else:
            print("Car started... ready to go!")
            carRunning = True

    elif userInput == "stop":
        if carRunning:
            print("Car stopped. ")
            carRunning = False
        else:
            print("Car is already stopped.")

    elif userInput == "quit":
        print("Goodbye.")
        break

    else:
        print("I don't understand that...")
