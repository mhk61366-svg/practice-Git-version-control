d1 = {"apples":6,"oranges":4,"mangoes":8,"banana":7,"grapes":12}

value = input("Enter a value to search: ")
value = int(value)

new_d1 = {key: val for key,val in d1.items() if val==value }
if new_d1:
        print("Matching Key values : ")
        print(new_d1)
else:
    print("No match found for the value")

print("This file has been modified again for testing")
print("hello again !!!")