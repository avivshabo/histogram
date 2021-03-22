import sys
def get_int_array():
    intArr = []
    print("Enter numbers seperated by Enter key")
    print("Enter a blank line to start calculating the histogram")
    print("Enter Q to quit")
    while True:
        strInput = input("Enter a number: ")
        if strInput.isnumeric():
            try:
                intInput = int(strInput)
            except ValueError as err:
                print(f"Failed to convert {strInput} to integer: {err}")
            else:
                intArr.append(intInput)
        else:
            if strInput:
                print("Non numeric input recieved - Exiting.")
                sys.exit(0)
            else:
                break
    return intArr





def get_int():
    strNum = input("Enter number of buckets: ")
    if strNum.isnumeric():
            try:
                intNum = int(strNum)
            except ValueError as err:
                print(f"Failed to convert {strNum} to integer: {err}")
    else:
        print("Invalid value for number of buckets. Exiting.")
        sys.exit(0)
    return intNum

def print_arr(arr):
    print(' '.join(map(str, arr)))