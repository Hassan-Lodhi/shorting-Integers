"""
Program to take list of integers and then sort it...
"""
int_list = []

while True:

    user_input = input("Enter integers to add to the list (separated by spaces), or 'done' to finish: ")
    if user_input == 'done':
        break

    try:
        num_list = [int(x) for x in user_input.split()]
    except ValueError:
        print("Invalid input. Please enter integers separated by spaces.")
        continue

    int_list.extend(num_list)
    int_list.sort()
    print("Sorted list:", int_list)

while user_input != "done":

    user_input = input("Enter an integer to add to the list, or 'done' to finish: ")
    if user_input == 'done':
        break
    try:
        num = int(user_input)
    except ValueError:
        print("Invalid input. Please enter an integer.")
        continue

    pos = 0
    while pos < len(int_list) and num > int_list[pos]:
        pos += 1

    int_list.insert(pos, num)
    print("Updated list:", int_list)

