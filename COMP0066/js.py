import json
#JSON python教程https://opensource.com/article/19/7/save-and-load-data-python-json

def write(file, data):
    """
    json write method, write data in file
    :param file: (String)
    :param data: (Dictionary)
    :return:
    """
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)


def read(file):
    """
    json read method, get data from file
    :param file: (String)
    :return: (Dictionary)
    """
    f = open(file)
    data = json.load(f)
    f.close()
    return data
