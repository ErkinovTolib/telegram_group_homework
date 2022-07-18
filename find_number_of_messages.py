from cgitb import text
from read_data import read_data

def find_number_of_messages(data: dict)->int:
    """
    Get the total number of messages.

    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        int: Total number of messages.
    
    """
    message = []
    c = 0
    messages = data["messages"]
    for i in messages:
        if i.get("text") and i.get("text") not in message:
            message.append(i["text"])
            c += 1


    return c

print(find_number_of_messages(read_data('data/result.json')))