#Task-1

Email = 'Amit-ML@gmail.com'

def validation_mail(Email):

    if Email.count('َ@') == 1:
        return('valid Mail')
    
    username , domain = Email.split('@')
    
    if '.' not in domain:
        return('Invalid Mail')
    
    return "Vaild Mail"

result = validation_mail(Email)
print(result)

#print user name
print(Email[0:7])
#Extract Domain
print(Email[-3:])


def domain_check(Email):
    if Email[-4:] == '.com':
        return 'Commercial Email'
    elif Email[-4:] == '.edu':
        return 'Eductional Email'
    
    return 'Other Domain Name '

result2 = domain_check(Email)
print(result2)

