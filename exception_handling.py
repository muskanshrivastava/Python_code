def increment() :
    try:
        num = int(input("Enter number : "))
        num += 1
    except Exception as e:
        print("INVALID INPUT")
    else:                                           
        print("Number incremented successfully")       # else block will run if try block have run successfully

def division():

    try:
        num =  int(input("Enter number : "))
        d = 5//num
    except Exception as e:
        # raise ValueError("Please enter valid number")
        print("Invalid Input")
    #finally block will not run if expception is raised manually by usin raise keyword. Otherwise finally will execute whether try or except block run.
    finally:
        print("Finished Successfully")             

increment()
division()