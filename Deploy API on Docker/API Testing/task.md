Developers need testing their APIs. There are plenty of tools for these tasks, allowing you to send a wide variety of HTTP, REST and other requests. For example, [Postman](https://www.postman.com/) or integrated into PyCharm Professional [HTTP Client](https://www.jetbrains.com/help/pycharm/http-client-in-product-code-editor.html). 

In this task we will use the open-source [HTTPie](https://httpie.io) tool. All such applications are similar in some way, so you can use HTTPie too or any other by analogy.

You can download and install a desktop version of HTTPie [here](https://httpie.io/desktop).

### GET request
As with all such programs, the interface allows you to specify the query type, parameters, headers, authorization type, and more. For the very first request, we only need to specify the URL `http://0.0.0.0:5000/items` and press **Send** button.

Remember to launch our flask application beforehand! 

![](images/httpie_get.png)

HTTPie automatically detects the language of the response, links, and formats text inside the body to make inspection easy.

### POST request
Next, create a POST request. To do this, specify the `POST` request type, URL `http://0.0.0.0:5000/items` as well as the Body of the request. Select `Text` as the Body type.

After executing the request, you should get a response containing the request body.

![](images/httpie_post.png)

### Explore your app
Check that all the other methods defined in your API work as expected (getting a specific device, deleting a device, updating a device).
