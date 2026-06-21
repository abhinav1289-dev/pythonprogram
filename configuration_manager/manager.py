#Build a User Configuration Manager
'''You should define a function named add_setting with two parameters representing a dictionary of settings and a tuple containing a key-value pair

add_setting function should:

Convert the key and value to lowercase.
If the key setting exists, return Setting '[key]' already exists! Cannot add a new setting with this name.
If the key setting doesn't exist, add the key-value pair to the given dictionary of settings and return Setting '[key]' added with value '[value]' successfully!.
The messages returned should have the key and value in lowercase.
You should define a function named update_setting with two parameters representing a dictionary of settings and a tuple containing a key-value pair.

update_setting function should:

Convert the key and value to lowercase.
If the key setting exists, update its value in the given dictionary of settings and return: Setting '[key]' updated to '[value]' successfully!
If the key setting doesn't exist, return Setting '[key]' does not exist! Cannot update a non-existing setting.
The messages returned should have the key and value in lowercase.
You should define a function named delete_setting with two parameters representing a dictionary of settings and a key.

delete_setting function should:

Convert the key passed to lowercase.
If the key setting exists, remove the key-value pair from the given dictionary of settings and return Setting '[key]' deleted successfully!
If the key setting does not exist, return Setting not found!
The messages returned should have the key in lowercase.
You should define a function named view_settings with one parameter representing a dictionary of settings.

view_settings function should:

Return No settings available. if the given dictionary of settings is empty.
If the dictionary contains any settings, return a string displaying the settings. The string should start with Current User Settings: followed by the key-value pairs, 
each on a new line and with the key capitalized. For example, view_settings({'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}) should return:


Current User Settings:
Theme: dark
Notifications: enabled
Volume: high

For testing the code, you should create a dictionary named test_settings to store some user configuration preferences.'''




test_settings={'theme': 'light',"mode":"dark"}

def add_setting(main,tup):
    l=list(tup)
    for i in range (len(tup)):
        l[i]=tup[i].lower()

    if l[0] in main:
        print("Setting",l[0],"already exists! Cannot add new setting with this name. ")
        

    else:
        main[l[0]]=l[1]
        print("Setting ",l[0],"added with value ",l[1],"successfully!")

def update_setting(main,tup):
    l=list(tup)
    for i in range (len(tup)):
        l[i]=tup[i].lower()

    if l[0] in main:
        main[l[0]]=l[1]
        print("Setting ",l[0] ,"updated to ",l[1]," successfully!")
    else:
        print("Setting ",l[0] ,"does not exist! Cannot update a non-existing setting.")   

def delete_setting(main,key):
    key=key.lower()
    if key not in main:
        print("Setting not found")    
    else:
        main.pop(key)
        print("Setting",key,"deleted successfully!")      
def view_setting(main):
    if len(main)==0:
        print("no Setting available")
    else:
        for i in range(len(main)):
            print(main[i].title())
for i,j in (test_settings.items()):
    print(i.title," ",j.title)