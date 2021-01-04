#'I pledge my honor that I have abided by the Stevens Honor System'
#Zachary Jones
#Homework 4 10/29/20

def get_names():
    with open('Before.txt') as file:
        names = file.readlines()

    names_list = []
    for line in names:
        names_list.append(line.strip())
    return names_list


def capitalize_list(list):
    cap_list = []
    for item in list:
        cap_list.append(item.upper())
    return cap_list


def write_names(list):
    file = open('After.txt', 'w')
    for item in list:
        file.write(item + '\n')
    file.close()


write_names(capitalize_list(get_names()))