## Deploying on local without Docker

(Need to elaborate on this)

While this tutorial is focused on deploying with Docker, you are able to deploy on local without it too. 
Set up your network to route `invsys -> 127.0.0.1` by updating your `/etc/hosts` file with an extra line like `127.0.0.1 invsys`. 
You can then open two terminal windows. In the first, `cd` to `invsys` and then run python `application.py`, and in the other terminal 
window, do the same but in the gateway directory. Then with Postman you can target either backend on `127.0.0.1`. Docker is for 
more than just deploying though, so this sub-section is just an aside for those interested.