import random
import os

path = os.getcwd()


def generate_number():
    random_list = random.sample(range(9), 4)
    str_list = list(map(str, random_list))
    str_number = ""
    for number in str_list:
        str_number = str_number + number
    dict_number = {"number": str_number}
    return dict_number


def to_txt():
    number = generate_number()
    print("{}/random.txt".format(path))
    with open('{}/random.txt'.format(path), 'w') as file:
        file.write("{}\n".format(number))
    # This try check if the file was created correctly.
    try:
        f = open('random.txt')
        f.close()
        resolution = "Ok"
    # If the no file was found throw an error, and return Oops.
    except FileNotFoundError:
        resolution = "Oops!"
    # The resolution is return with the content 'Ok' or 'Oops'
    return resolution


def master_mind(number_typed):
    with open("{}/random.txt".format(path), 'r') as f:
        random_number = f.readline()
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
    value = master_mind("5412")
    print(value)