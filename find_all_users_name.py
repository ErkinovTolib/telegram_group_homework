from read_data import read_data

def find_all_users_name(data: dict)->list:
    """
    This function will find all the users in the json file and return the list of users name.
 
    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        list: List containing all the users name.
    """
    user_name = []
    messages = data["messages"]
    for i in messages:
        if i.get("actor") and i.get("actor") not in user_name:
            user_name.append(i["actor"])
        if i.get("from") and i.get("from") not in user_name:
            user_name.append(i["from"])

    return user_name

print(find_all_users_name(read_data('data/result.json')))
