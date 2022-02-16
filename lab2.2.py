"""LAB 2.2"""
import json
import sys


def reading_json(path_to_json):
    """
    Reads the json file
    >>> reading_json("twitter1.json") #doctest: +ELLIPSIS
    [{'created_at': 'Sun Jan 30 16:36:22 +0000 2022',...
    """
    with open(path_to_json, "r", encoding='utf-8') as new_file:
        data = json.load(new_file)
    return data


def checking():
    """
    Checking if the user really wants to explore data
    """
    print("Do you want to explore data? y/n")
    your_choice = input()
    if your_choice == "n":
        print("Very sad :(")
        sys.exit()
    while your_choice != "y":
        print("Choose the right answer")
        your_choice = input()
        if your_choice == "n":
            print("Very sad :(")
            sys.exit()
        elif your_choice == "y":
            break
    if your_choice == "y":
        print(f"There are some elements, you can explore")


def navigation(data):
    """
    Navigates in the json file with recursion
    """
    if isinstance(data, list):
        len_of_json = len(data)
        if len_of_json == 0:
            print("The list is empty")
            return
        print("----------------------")
        for item in range(len_of_json):
            print(f"{item + 1} Object")
        print("----------------------")
        print("Please, enter the number of the object, you want to explore")
        number = input()
        while not(number.isdigit() and 0 < int(number) < len_of_json + 1):
            print("Please, enter the the right number of the object, you want to explore")
            number = input()
        print(f"You choose the {number} object")
        print()
        navigation(data[int(number) - 1])
    elif isinstance(data, dict):
        print("----------------------")
        for key in data:
            print(str(key))
        print("----------------------")
        print("Enter the key you want to see: ")
        keyy = input()
        while keyy not in data:
            print("Enter the right key")
            keyy = input()
        navigation(data[keyy])
    else:
        print("Your data is " + str(data))


def main():
    """
    Main function to run all the functions
    """
    while True:
        try:
            path_to_json = input("Enter the path to json file: ")
            data = reading_json(path_to_json)
            checking()
            break
        except FileNotFoundError:
            print("Wrong file")
    navigation(data)


if __name__ == '__main__':
    main()
