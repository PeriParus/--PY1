from random import sample
import string

def get_random_password(n=8) -> str:
    string_ = string.digits + string.ascii_lowercase + string.ascii_uppercase
    password=sample(string_,n)
    return(password)

print(get_random_password())
