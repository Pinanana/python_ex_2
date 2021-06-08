# Python refresher exercises 2 - task 2

# - as part of some app, the user has to create a valid email address
# - any address will do as long as it's valid
# - your validation will only allow a number of retries if a invalid email is given (default 3)
# - once the number of attempts is exhausted (you should show how many retries are left!), set the
#   variable (flag) gave_up to True and bail out.
# 
# - it's OK to start with my solution from the lecture in flow control, although I 
#   encourage you to try you own solution first (if you can't remember). Any other, working
#   solution is fine, too!
# - when it comes to how to react to an error, your user MUST re-enter a string, but it's up to 
#   you how helpful you want to be:
#   - you could just list all the rules on error and demand a new input
#   - you could list the appropriate error message returned from you function and demand a new input
#   - you could do something fancy and only require re-typing of what's wrong (if that's technically possible):
#       e.g. if the pre @ is wrong (too long, contains a invalid char) you could demand that
#       only that incorrect part is re-entered. Warning - this can be complicated and laborious to test!
# - Note that the check for a valid email is a bit weird (b/c of how I set it up):
#   - iff the first return is None (r == None), the email is valid (yes, None doesn't sound like an OK ...)
#   - if you didn't get None (r != None), then r contains an error code, which you could use in your 
#     flow control for branching, if you want to do something fancy

# Optionally, you can use regex for all this!

# Once you're solved this, run some tests to show me that it works. 
# Again, manually copy/paste the console output in a text file (results2.txt)
"""
import ex_2_task_1
print(dir(ex_2_task_1))
print(ex_2_task_1.is_valid_email_address("bla@bla.com"))
"""
# import your function from the previous .py file as a module (you can abbreviate it)
# use ex_2_task_2 here instead once your function works!
from ex_2_task_1 import is_valid_email_address as is_valid 



# your code - start

def validate_login(s):
    gave_up = False
    attempts_left = 3
    print("Thank you, now checking for validity of", s)
    r = is_valid(s)
    if r == None:
        print("Validity check is successful.")
        return True
    else:
        while attempts_left != 0 and r != None: #it says there is a problem here but I don't understand why.
            print(r)
            s = input("Please re-enter your email address: ")
            attempts_left = attempts_left - 1
            r = is_valid(s)
            if r == None:
                print("Validity check is successful.")
                return True
        else: 
            print("Sorry, you have run out of trials. You can exit now.")
            return False

#s = input("Please enter your email address: ")
#s = "pi@gmail.com"
#e = validate_login(s)

#print(e)

def validate_login_v2(attempts_left=3):
    #attempts_left = 3
    while True:
        s = input("Please enter your email address: ")

        #evaluating r, bail out if correct
        r = is_valid(s)
        if r == None:
            print("Validity check is successful.")
            return s
        attempts_left -= 1
        print(r, "attempts left:", attempts_left)
        
        #bail out when no attempt left
        if attempts_left == 0:
            return None

print(validate_login_v2(5))

# your code - end
#if not gave_up:
#    print("valid email", email)
#else:
#    print("invalid email", email)
