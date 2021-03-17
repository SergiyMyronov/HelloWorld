
"""
2. Валидатор паролей. На занятии делали валидацию емейла, тут 
    нужно сделать валидацию пароля по такому же принципу.
    Придумать критаерии надежного пароля, описать их в условиях.
"""

# PASSWORD VALIDATOR

import sys

while 1:
    passw: str = input('Please input new password: ')

    if passw:
        if len(passw) < 8:
            print('Strong password must consist of at least 8 characters. Try again!')
        elif passw.isalpha() or passw.isnumeric():
            print('Strong password must be a mixture of letters and numbers. Try again!')
        elif passw.isalnum():
            print('Strong password must include at least one special character, e.g. ! @ # ? ]. Try again!')
        elif passw.islower():
            print('Strong password must include at least one uppercase letter. Try again!')
        else:
            print(f"'{passw}' is a strong-enough password. Good job!")
            sys.exit(0)
    else:
        print("You didn't enter any symbol. Try again!")


