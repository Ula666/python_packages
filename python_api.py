# python api - application programming interface - industry property
# Python requests package
# connect to live web using python request api
# we will connect to www.bbc.com and check if the web is live

# import requests
#
# responses = requests.get("http://www.bbc.co.uk/")

# if responses.status_code == 200:
#     print("The website is up and running! The status code is: " + str(responses.status_code))
# else:
#     print("OOPs something went wrong" + str(responses.status_code) )

# status code 200 means success, the website is running
# status code 400 or 404 means not working

# create a function called status code check
# function should return status code with appropriate message
# DRY


# address = input("Please enter website ")


# def status_code_check():
#     if responses.status_code == 200:
#         print("The website is up and running! The status code is: " + str(responses.status_code))
#     else:
#         print("OOPs something went wrong" + str(responses.status_code))
#
#
# status_code_check()


# 2nd version
# def status_code_check(website):
#
#     status = requests.get(website).status_code
#     if responses.status_code == 200:
#         print("The website {website} is up and running! The status code is: " )
#     else:
#         print("OOPs something went wrong {website}, status code {status}")
# if __name__ == "__main__":
#     print(status_code_check("http://www.bbc.co.uk/"))

import requests

response = requests.get("http://www.bbc.co.uk/")


def check_status():
    if response: # the condition is true
        print("Success " + str(response.status_code))
    elif response:
        print("failure")
    elif response:
        print("OOPs something went wrong")

check_status()
# requests goes one step further is simplifying this process for us
# if you use response instance in a condition expression
# it will evaluation to True if the status code was between 200 and 400, False otherwise
# therefore, you can simplify last example by rewriting the if statement as above

#print(response.status_code)


