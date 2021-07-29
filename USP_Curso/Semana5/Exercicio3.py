
def vogal(v):
    if(v in ('a','e','i','o','u')):
        return True
    else:
        return False

v = input("Letra: ")

print(vogal(v))