import sys

def orify(str_in_lower_and_upper):
    return "".join(map(lambda x: "[" + x.lower() + x.upper() + "]" if x.isalpha() else x, str_in_lower_and_upper))  # :)

if len(sys.argv) < 2:
    print("At least one argument needed!")
    print("\nI mean, %s" % orify("At least one argument needed"))
else:
    print(orify("".join([i for s in sys.argv[1:] for i in s])))
