While this course is focused on deploying with Docker, you can also deploy locally without it. 

You will need to change the routes in the `gateway`:
instead of 
```python
'http://invsys:5000/items'
```

use 

```python
'http://0.0.0.0:5000/items'
```

You can then run both applications directly in the IDE.


<details>
<summary><i>Running the apps from the terminal</i></summary>
You can also open two terminal windows in the IDE. 


In the first one, navigate to `invsys` using `cd` and then run 
```shell

$ python3 api.py
```

In the other terminal window, do the same but in the `gateway` directory: 
```shell

$ python3 application.py
```
</details>

Both microservices are now running, and 
you can target either backend using HTTPie at `127.0.0.1` (or `0.0.0.0`).
