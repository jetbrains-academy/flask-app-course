We expect our application to receive the request from the API client, forward the payload or query strings to invsys, then forward the response from invsys back to the API client. No need for any additional stuff here (no db, no dal etc)

To forward our requests, we will use the requests module, which can install using pip install requests. Remember to add this to requirements.txt.