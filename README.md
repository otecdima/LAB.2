# LAB 2.2

The goal of the lab is the simple navigation in the json file. The user can navigate through the lists and dictionaries in converted json file and find information in different locations.

## Reading the file
```diff
reading_json(path_to_json) 

```
It helps us to read the file with json library, using json.load()
```python
def reading_json(path_to_json):
    """
    Reads the json file
    >>> reading_json("twitter1.json") #doctest: +ELLIPSIS
    [{'created_at': 'Sun Jan 30 16:36:22 +0000 2022',...
    """
    with open(path_to_json, "r", encoding='utf-8') as new_file:
        data = json.load(new_file)
    return data
```

   
## Checking of the user's intention
```diff
checking()
```
   Checks if the user really wants to explore the data, by entering "y" or "n" in command line.
## The navigation through the file
```diff
navigation(data)
```
   The function for navigating in the file, using recursion.
Firstly we check if the data which we extract from json is list or dictionary, they both have the algorithms on that cases. Ans then we use recursing to go deeply into the file. 
## Main 
```diff
main()
```
   The main function to get the navigation in json file, using the functions above.
```python
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
```
## Conclusion
___That module helps us "run" through the json file without any problems (any cases are taken into account and don't cause the errors)___
