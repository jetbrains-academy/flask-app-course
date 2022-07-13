## Deploying on local without Docker

(Need to elaborate on this)

While this course is focused on deploying with Docker, you can deploy on local without it too. 

You will need to change the routes in the `gateway`:
instead of 
```python
'http://invsys:5000/items'
```

use 

```python
'http://0.0.0.0:5000/items'
```

You can then open two terminal windows in the IDE. 

In the first, `cd` to `invsys` and then run 
```shell
$ python3 app.py
```

In the other terminal window, do the same but in the `gateway` directory. Both microservices are now up and 
using Postman you can target either backend on `127.0.0.1` (or `0.0.0.0`). 