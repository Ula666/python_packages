# Python packages

### package - list of different functions
### why should we use them?
### What is PIP?
- `pip` It's a package manager in Python to install packages
- To use pip `pip install packacge_name`
- `pip install requests`
- To import a package
```python
from random import random # this package generates random numbers
import math
```

`print(random())`  - it generates random number

```python
num_float = 23.6
print("Actual float value " + str(num_float))
print(math.ceil(num_float)) 
 ```
- if number .5 round it up
- ceil() rounds up the value
```python
print(math.floor(num_float))` # if number .4 or less round it down
```
- floor() round down the number 

### Python modules:
```python
import os
import datetime, sys
print((os.cpu_count()))
```

### Python requests package:
- api - application programming interface
- example of function that check the website status code:
 ```python
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
```

