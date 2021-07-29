
def vogal(v):
    if(v in ('a','e','i','o','u','A','E','I','O','U')):
        return True
    else:
        return False

v = input("Letra: ")

print(vogal(v))