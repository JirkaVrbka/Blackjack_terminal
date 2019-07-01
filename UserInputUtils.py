
def get_int(msg=""):
    while True:
        try:
            val = int(input(msg+"\n"))
            return val
        except ValueError:
            print("Unable to convert you value into number, try one more time")


def get_int_with_default(default, msg=""):
    while True:
        try:
            val = int(input(msg+"\n"))
            return val
        except ValueError:
            print("This is not a number! I set it for you {}".format(default))


def get_positive_int_with_default(default, msg=""):
    while True:
        try:
            val = int(input(msg+"\n"))
            if val >= 0:
                return val
            else:
                break;
        except ValueError:
            pass
        print("Unable to convert you value into number, so I set for you {}".format(default))
        return default
