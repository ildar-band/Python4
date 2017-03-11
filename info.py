user_info = {'key1':'first_name', 'key2':'last_name'}

user_name = input("Please, enter you name: ")
user_info["key1"] = user_name

user_surname = input("Please, enter you surname: ")
user_info["key2"] = user_surname

print(user_info)