"""
Bishal Nath
bishal.nath66@login.cuny.edu		
"""
"""
CSci 127 Teaching Staff
March 2026
Modified by:  Bishal Nath
"""

def password_strength(password, min_length):
     """
     Takes a password string and a minimum required length as input.
     Returns 'weak', 'medium', or 'strong' based on the password's characteristics.
     """
     if (len(password) < min_length):
          return 'weak'

     has_upper = False
     has_digit = False
     has_special = False
     i = 0
     
     while i < len(password):
        ch = password[i]
        if ch.isupper():
               has_upper = True
        elif ch.isdigit():
               has_digit = True
        elif ch in '!@#$%':
               has_special = True
        else:
            pass
        i += 1

     if has_upper and has_digit and has_special:
          return 'strong'
     elif has_upper or has_digit:
          return 'medium'
     else:
          return 'weak'

def main():
    pwd = input("Enter a password: ")
    minLen = int(input("Enter minimum length: "))
    print("Password strength:", password_strength(pwd, minLen))


#Allow script to be run directly:
if __name__ == "__main__":
    main()
