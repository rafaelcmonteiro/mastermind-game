import pymongo


# Getting connection with mongodb
def db_connection():
    my_connection = pymongo.MongoClient("mongodb://localhost:27017/")
    my_db = my_connection["mastermindDB"]
    return my_db


def creating_user(user_data):
    connection = db_connection()
    my_col = connection["users"]
    x = my_col.insert_one(user_data)
    print(x.inserted_id)


# This function add a new line element on a specific document, or update the past content.
def updating_user(user_key, dict_update):
    connection = db_connection()
    my_col = connection["users"]
    user = find_user(user_key)
    # Setting the new content.
    new_values = {"$set": dict_update}
    # Merging the content with the existent content.
    my_col.update_one(user, new_values)

    user = find_user(user_key)
    print(user)


def find_users():
    connection = db_connection()
    my_col = connection["users"]
    for x in my_col.find():
        print(x)


# The key is the person name.
def find_user(user_key):
    connection = db_connection()
    my_col = connection["users"]
    my_query = {"name": user_key}
    x = my_col.find_one(my_query, {"_id": 0})
    return x


if __name__ == '__main__':
    update_dict = {"password": "123456"}
    updating_user("Rafael", update_dict)
