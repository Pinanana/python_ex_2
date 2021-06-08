# Python refresher exercises 2 - task 1

# Write and test a function is_valid_email_address(s) that evaluates string s as a valid email address 
# Returns: tuple of 2 elements (res, err):
#          res contains the result (None or error code)
#          err contains an error string ("seems legit" for None,  a short error message for the error code
#
# Rules: (these are mine, not the official web standards!)
# must have 3 parts: <A>@<B>.<C>
# A must have between 3 and 16 alpha numeric chars (test: isalnum()) 
# B must have between 2 and 8 alpha numeric chars (test: isalnum()) 
# C must be one of these:  com edu org gov 
#
# Here are some tests and the expected results:
# 
# charding@iastate.edu (None, 'Seems legit')
# chris.edu (1, 'Must have exactly one @!')
# chris@edu (4, 'post @ part must have exactly one dot!')
# @bla.edu (2, 'pre @ part must contain 3 - 16 alfanum chars')
# throatwobblermangrove@mpfc.org (2, 'pre @ part must contain 3 - 16 alfanum chars')
# chris@X.com (5, 'part after @ and before . must contain 2 - 8 alfanum chars')
# chris.harding@iastate.edu (3, 'pre @ part must only contain alfanum chars')
# chris@pymart.biz (7, 'past-dot part invalid, must be from: com, edu, org, gov')
# chris@letsgo!.org (6, 'part after @ and before . must only contain alfanum chars')
# chris@megasavings.org (5, 'part after @ and before . must contain 2 - 8 alfanum chars')
# tc@tank.com (2, 'pre @ part must contain 3 - 16 alfanum chars')
#
# your function MUST react the same (OK or error) but you don't have to use my exact error messages or codes 
# just something similar to that effect. You could even be more helpful e.g. 
# "throatwobblermangrove is too long (21 chars), must be 3 - 16"
# It's OK to bail out at the first proven error, even if there would have been more errors later!
# Also, I prb. forgot some possible edge cases, please add more if needed!

# As proof, please manually copy/paste the console output for one run into a file called
# results1.txt

s = "pinaradanir96@gmail.com"

email = s.split("@") 
username = email[0]
tech = email[1].split(".")
hosting = tech[0]
ending = tech[1]

validending = ["com", "edu", "org", "gov"]

print(username, hosting, ending)


def is_valid_email_address(s):
    # your code here
    if len(username) < 3:
        print("Sorry, username too short.")
    elif len(username) > 16:
        print("Sorry, username too long.")
    if len(hosting) < 2 or len(hosting) > 8:
        print("Sorry, not a valid email hosting name.")
    if ending not in validending :
        print("Sorry, invalid ending.")
    else:
        print("Valid email address! Thank you.")

is_valid_email_address(s)

# A must have between 3 and 16 alpha numeric chars (test: isalnum())
# B must have between 2 and 8 alpha numeric chars (test: isalnum()) 
# C must be one of these:  com edu org gov 


# CH: this is really not how functions are supposed to work!
# inside your function, you cannot access vars defined outside the def block, you can only use arguments!
# you can create local vars inside the def but they won't be valid outside the function
# You were supposed to return something, not just print a string. 
#          res contains the result (None or error code)
#          err contains an error string ("seems legit" for None,  a short error message for the error code
# Fix the other elif blocks accordingly
# Run the validation loop at the end 

def is_valid_email_address_CH(s):

    # create local vars from arg s
    email = s.split("@") 
    username = email[0]
    tech = email[1].split(".")
    hosting = tech[0]
    ending = tech[1]
    validending = ["com", "edu", "org", "gov"]

    if len(username) < 3:
        res = 1
        err = "Sorry, username too short."
    elif len(username) > 16:
        print("Sorry, username too long.")
    if len(hosting) < 2 or len(hosting) > 8:
        print("Sorry, not a valid email hosting name.")
    if ending not in validending :
        print("Sorry, invalid ending.")
    else:
        print("Valid email address! Thank you.")

    return res, err # return both variables as a tuple

# This if ensures that the following is NOT run if this file was imported as a module (which we'll do next!)
if __name__ == "__main__":

    # tests, including edge cases (incomplete? add more!)
    email_list = ["charding@iastate.edu", 
        "chris.edu",
        "chris@edu",
        "@bla.edu",
        "throatwobblermangrove@mpfc.org", 
        "chris@X.com",
        "chris.harding@iastate.edu",
        "chris@pymart.biz",
        "chris@letsgo!.org",
        "chris@megasavings.org",
        "tc@tank.com",
        ]
    # validate each email from the list
    for e in email_list:
        r, s = is_valid_email_address_CH(e) 
        if r == None:
            print(e, s) # OK
        else:
            print(f"{e} - error: {s}, error code: {r}") # Error

        
