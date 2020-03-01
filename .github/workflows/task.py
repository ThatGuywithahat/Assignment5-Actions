import math
import datetime

def firstrun():
    return "success"


def radius(C):
    return C / (2 * math.pi)


def getlist(list):
    size = len(list) - 1
    first = "first"
    last = "last"
    result = "First:{0} Last:{1}".format(list[0],list[size])
    return result

def getdate(date1,date2):
    return (date1 - date2)
