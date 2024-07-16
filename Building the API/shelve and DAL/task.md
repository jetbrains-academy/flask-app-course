### Shelve
We'll use the term "database" to refer to a file on which we will perform Create, Retrieve, Update, and Delete (CRUD) operations on data elements in an arbitrary order.
The [`shelve`](https://docs.python.org/3/library/shelve.html) module provides a very flexible database, implementing persistent storage for arbitrary Python objects — anything that the [pickle](https://docs.python.org/3/library/pickle.html#module-pickle) module can handle.
A "shelf" is a persistent, dictionary-like object accessed by keys.

The `shelve` module can be used as a simple persistent storage option for Python objects when a relational database is an overkill. Shelf objects support most methods and operations supported by dictionaries (except copying, constructors, and operators `|` and `|=`). 
This eases the transition from dictionary based scripts to those requiring persistent storage.

The code in this task initializes a `shelve` database with some initial data. This initial data is taken from the same dictionary we used before.

### DALs

If you look at the code in previous tasks, you will see that we mention the "database" directly. 
For some applications, this is fine, but if we later decide to change the kind of 
database we are using, all our database references and routes will need updating. 

We could decouple the database by using a concept known as DAOs (data access objects) or **DALs (data access layers)**.
A DAL is a layer of a computer program that provides simplified access to data stored in persistent storage, 
such as an entity-relational database. The DAL hides the complexity of the underlying data store from the external world.
For example, instead of using commands such as `insert`, `delete`, and `update` to access a specific table in a database, 
we could create a class and a few stored procedures in the database or execute the commands  
within simple functions stored within the data access layer.

### Task

We are going to write a DAL with simple functions performing CRUD operations on a shelve database. In this task, 
you only need to populate the database `db` with data from the dictionary. 

<div class="hint">

Remember that `db` is a dictionary-like object accessed by keys.
</div>
