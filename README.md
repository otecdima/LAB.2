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

# Lab 2.3

The goal of that lab was to learn how to get and work with API in Twitter, to get the location of friends of the username that we write on the site.

## Getting information
```diff
get_information_from_keys(username)
```
The first function help to get the information about friends of the user (username) using key and module requests:
```python
def get_information_from_keys(username):
    """
    Return dictionary with information about friends on Twitter.
    """
    key = 'AAAAAAAAAAAAAAAAAAAAABcXZQEAAAAAFitawJoUzroZoiCP41R0%2F\
yXXPHc%3DvATE65kkopZn2sQBHIXT5bCRF1v61uESR5ZGGDfR94pOiEldUd'
    headers = {'Authorization': f'Bearer {key}'}
    params = {'screen_name': username, 'count': 200}

    response = requests.get('https://api.twitter.com/1.1/friends/list.json',
                            headers=headers,
                            params=params)
    return response.json()
```
## Getting location
```
get_location(info)
```
The function reads the info, which is in dictionary type, and returns the list with the username of a friend as the first element, and tuple of coordinates as the second one.
## Building a map
```
building_map(list_with_coor)
```
The function builds the map using the module folium
## Main
```
main(username)
```
The main function, which unites all functions
```python
def main(username):
    """
    Manin function with all the previous ones
    """
    info = get_information_from_keys(username)
    list_with_coor = get_location(info)
    if list_with_coor == False:
        return False
    else:
        building_map(list_with_coor)
```

## The problem, I encountered
When the username doesn't exist or doesn't have friends, that function returns the same template with the HTML page with the form.
```python
def run_a_site():
    """
    Using of method POST for getting usernames and creating a mao according to that username
    """
    username = request.form['text']
    mainf = main(username)
    if mainf == False:
        return render_template('index.html')
    else:
        return render_template('mapwithfriends.html')
```
## Conclusion
___That laboratory work was quite useful, we got acquainted with new modules and how to work with them.___
