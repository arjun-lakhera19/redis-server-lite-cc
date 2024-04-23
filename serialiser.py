
def simpleString(str):
    return "+" + str + "\r\n"

def error(str):
    return "-" + str + "\r\n"

def integer(str):
    return ":" + str + "\r\n"

def bulkString(str):
    return "$" + len(str) + "\r\n" + str + "\r\n"

def null():
    return "$-1\r\n"

def array(arr):
    str = "*" + len(arr) + "\r\n"
    for x in arr:
        str += "$" + len(x) + "\r\n" + x + "\r\n"
    return str

