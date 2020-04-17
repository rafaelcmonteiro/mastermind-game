import pymongo


# Getting connection with mongodb
def db_connection():
    my_connection = pymongo.MongoClient("mongodb://localhost:27017/")
    my_db = my_connection["mastermindDB"]
    return my_db


# Create a user, the parameter brings a dict.
def creating_user(user_data):
    connection = db_connection()
    my_col = connection["users"]
    user_id = my_col.insert_one(user_data)
    return user_id.inserted_id


# Find all users.
def find_users():
    connection = db_connection()
    my_col = connection["users"]
    for x in my_col.find():
        print(x)


# The user_key is the user.
def find_user(user_key):
    connection = db_connection()
    my_col = connection["users"]
    my_query = {"user": user_key}
    result = my_col.find_one(my_query, {"_id": 0})
    return result


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
    return user


def removing_user(user_id):
    connection = db_connection()
    my_col = connection["users"]
    my_query = {"user": user_id}
    my_col.delete_one(my_query)


if __name__ == '__main__':
    print(find_user('rafael_shene@hotmail.com'))
