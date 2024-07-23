We added the four functions needed in our gateway application for routing requests (in addition to `index()`, which doesn't really do anything).
Each of these four functions will send a request to the other application.
In this task, you will add the appropriate routes to all of them.

The application will accept requests to:

- POST `/items`
- GET `/items`
- GET `/items/<string:item_id>`
- PUT `/items/<string:item_id>`
- DELETE `/items/<string:item_id>`

The first route has already been added for you; you now need to complete the others.

