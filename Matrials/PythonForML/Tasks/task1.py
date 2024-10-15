#Task-1
"""
    Suppose you have this email address “Amit_ml@gmail.edu” -
    Input Validation: Check if the input string contains exactly one "@" symbol and at least one "." after the "@" symbol.
    If it's not a valid email, return "Invalid email". - Extract Username: Extract and return the part of the email before the "@" symbol.
    - Extract Domain: Extract and return the domain (the part between "@" and the last ".").
    - Check for Domain Ending: Check if the email ends with ".com". If it does, return "Commercial Domain". If it ends with ".edu",
    return "Educational Domain". Otherwise, return "Other Domain".
 """
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


#Task 2
"""
Encoded Message: # # # ! ! @ m o c l e W   E P G T Q !!!6789
Steps to Decode:
1. Extract the core part of the message: "mocleW EPGTQ".
2. Reverse the first word: "mocleW" becomes "Welcome".
3. Replace shifted vowels in the second word:
o "EPGTQ": No vowels to change.
4. Final decoded message: "Welcome PGTQ".
"""

Encoded_Message= "###!!@mocleW EPGTQ!!!6789"
print(Encoded_Message)

#extract a core message
core_message = Encoded_Message[7:18]
print(core_message)

txt = Encoded_Message[6:11]
text = txt[::-1]            #ask about this is very comlpex
print(txt)

first , second = core_message.split('E')
print(first)
print(second)

print(text + ' ' + second)

#Task 3
"""
Encoded Message: &&&**$gnirtS PLIO!!@1234
Steps to Decode:
1. Extract the core part of the message: "gnirtS PLIO".
2. Reverse the first word: "gnirtS" becomes "String".
3. Replace shifted vowels in the second word:
o "PLIO": Replace I->E and O->U to get "PLEU".
4. Final decoded message: "String PLEU".
"""
Encoded_Message = "&&&**$gnirtS PLIO!!@1234"

core_message2 = Encoded_Message[6:17]
print(core_message2)

#reverse

word = Encoded_Message[12:17]
replaced = word.replace('I' , 'E'  )
print(replaced)

print(type(type))

learning= ['amit','python','jupyter']


learning.extend('machine_leaing')
print(learning)


