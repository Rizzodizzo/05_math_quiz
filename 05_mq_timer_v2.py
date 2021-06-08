# timer be like 
import time

# how does work
# functions
# Yes no checker
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("<error> Please say yes or no")
            print()


# Number checker to make sure user inputs correctly
def num_check(question, error, num_type, low=None, high=None):

    valid = False
    while not valid:
        try:
            response = num_type(input(question))

            if low is not None and high is not None:
                if low < response < high:
                    return response
                else:
                    print(error)
                    print()
                    continue

            elif low is not None:
                if response > low:
                    return response
                else:
                    print(error)
                    print()
                    continue

            else:
                return response

        except ValueError:
            print(error)
            print()



# Main routine
time_set = yes_no("Would you like a timer? ")
if time_set == "yes":
    # ask for the number of seconds
    seconds = num_check("how many seconds? ", "enetr an number between 1, 59", int, 0, 60)
    print("Timer set! ")
    # Set timer
    start = time.time()
    while time.time() - start < seconds:
        name = input("What is your name? ")
        print(name)
        print()

else:
    print("No timer. ")
print()


