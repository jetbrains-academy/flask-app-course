### Virtual environments

Python applications often use packages and modules that aren't part of the standard library. 
Sometimes, applications need a specific version of a library because they require 
a particular bug fix or use an obsolete version of the library’s interface.
Different applications might have conflicting requirements.

The solution to this problem is to create a virtual environment – a self-contained directory tree that contains 
a particular version of Python and a number of additional packages. Different applications can then use different virtual environments. By resolving the problem of 
conflicting requirements, applications can have their own virtual environments with compatible library versions installed. 
If one application requires a library to be upgraded, this will not affect other applications.

The `venv` module provides support for creating lightweight virtual environments with their own site 
directories, optionally isolated from system site directories. Each virtual environment has its own 
Python binary (which matches the version of the binary that was used to create this environment) and 
can have its own independent set of installed Python packages in its site directories.

IntelliJ IDEA makes it possible to use the [virtualenv](https://virtualenv.pypa.io/en/latest/index.html) tool to create a project-specific isolated virtual environment. This course already incledes one. 
For each isolated application that you build in this course, a new virtual environment will be created.

### Managing packages with pip

You can install, upgrade, and remove packages using a program called pip. By default, pip will install packages from the Python Package Index, <https://pypi.org>. You can browse the Python Package Index by visiting it in your web browser.

pip has a number of subcommands: “install”, “uninstall”, “freeze”, etc. 

You can install the latest version of a package by specifying its name. 
```text
python -m pip install requests
```
You can also install a specific version of a package.
```text
python -m pip install requests==2.6.0
```

`pip freeze` will produce a list of installed packages, and the output uses the format that `pip install` expects. A common convention is to store this list in a `requirements.txt` file.
The `requirements.txt` can be committed to version control and shipped as part of an application. Users can then install all the necessary packages with `pip install -r requirements.txt`.
We will use this and talk about it in more detail later.

### Managing packages in the IDE

IntelliJ IDEA provides methods for installing, uninstalling, and upgrading Python packages for a particular Python SDK. You can preview and manage packages in the **Python Packages** tool window and in the Python interpreter **Settings/Preferences**. 
You can read more about managing Python packages in IntelliJ IDEA on [this help page](https://www.jetbrains.com/help/idea/installing-uninstalling-and-upgrading-packages.html).


Read more about virtual environments and packages in [The Python Tutorial](https://docs.python.org/3/tutorial/venv.html) and [IntelliJ IDEA Documentation](https://www.jetbrains.com/help/idea/creating-virtual-environment.html).
