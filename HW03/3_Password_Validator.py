"""
3. Совместить валидацию email и валидацию пароля и вместо принтов райзить ошибки если пароль или 
email не подходит по критериям (критерии надежности пароля можно брать с прошлого ДЗ или придумать новые). 
Ошибки брать на выбор 
"""

# PASSWORD AND EMAIL VALIDATOR
# ------------------------------------------

# EMAIL VALIDATOR

email: str = input('Input email: ')

if '@' not in email:
    raise SyntaxError("Email must include '@'-symbol!")
elif '.' not in email:
    raise SyntaxError("Email must include at least one '.'-symbol!")
at_sign_index = email.index('@')
for sign in {'.', '@'}:
    if email[at_sign_index + 1] == sign or email[at_sign_index - 1] == sign:
        raise RuntimeError("ERROR: '.' can't stand next to '@'")
    elif email[-1] == sign or email[0] == sign:
        raise RuntimeError("ERROR: '.' or '@' can't be the first or the last symbol!")
print(f"'{email}' is ok. Good job!")


# PASSWORD VALIDATOR

passw: str = input('Please input new password: ')

if passw:
    if len(passw) < 8:
        raise RuntimeError('Strong password must consist of at least 8 characters!')
    elif passw.isalpha() or passw.isnumeric():
        raise SyntaxError('Strong password must be a mixture of letters and numbers!')
    elif passw.isalnum():
        raise SyntaxError('Strong password must include at least one special character, e.g. ! @ # ? ]')
    elif passw.islower():
        raise SyntaxError('Strong password must include at least one uppercase letter!')
    elif passw.isupper():
        raise SyntaxError('Strong password must include at least one lowercase letter!')
    else:
        print(f"'{passw}' is a strong-enough password. Good job!")
else:
    print("You didn't enter any symbol!")


