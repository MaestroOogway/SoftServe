import re

def check_pass(password):
    
    if len(password) < 6:
        print("Password too short (min 6 characters)")
        return False
    
    if len(password) > 16:
        print("Password too long (max 16 characters)")
        return False
    
    if not re.search(r"[a-z]", password):
        print("Password must contain at least one lowercase letter")
        return False
    
    if not re.search(r"[A-Z]", password):
        print("Password must contain at least one uppercase letter")
        return False
    
    if not re.search(r"[0-9]", password):
        print("Password must contain at least one number")
        return False
    
    if not re.search(r"[$#@]", password):
        print("Password must contain at least one special character ($, #, @)")
        return False
    
    print("Password is valid")
    return True
