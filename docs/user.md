# User


Request userinformations.


## The request
```py
from api import api # In the future will it be changed to disweb (dir).


r = await client.fetch_user(USER_ID) # Replace the USER_ID with the id from a user.
username = r['username'] # JSON Response
print(username) # Print the username into the console.
