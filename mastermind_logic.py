import user_dao as dao
import random
import os

path = os.getcwd()


# Generate a random number.
def generate_number():
    random_list = random.sample(range(9), 4)
    str_list = list(map(str, random_list))
    str_number = ""
    for number in str_list:
        str_number = str_number + number
    return str_number


# Update the user dict with random number. user_name = string
def inserting_random(user_name):
    number = generate_number()
    number_dict = {"random": number}
    user = dao.updating_user(user_name, number_dict)
    return user


# user_name = string
def master_mind(number_typed):
    #user_data = dao.find_user(user_name)
    #random_number = user_data["random"]
    random_number = '1234'
    result = ''
    for index, number in enumerate(number_typed):
        # Count gets how many times obj occurs on list.
        occurrence = random_number.count(number)
        # Check if the result is not equal zero.
        if occurrence != 0:
            position = random_number.find(number)
            if position == index:
                result += '1'
            else:
                result += '0'
    to_send = {"result": result, "number_typed": number_typed}
    return to_send


if __name__ == '__main__':
    pass
