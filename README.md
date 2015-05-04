#summary How to install the package.

## Dependency

  * neo-utils
  * web2py

## Installation

The project contains only one package: neo_web2py_utils. The project is called 
neo-web2py-utils and it contains the package neo_web2py_utils. It is 
neo_web2py_utils that must be moved in the "modules" directory of the web2py 
application or "site-packages" of web2py installation. Not the neo-web2py-utils
project.

Preferably, install the package in the "modules" folder for all applications 
using it. Otherwise, if you decide to use the "site-packages" folder, an 
upgrade may impact far more applications and it gives no version control over 
which versions of the package are used. Note that the package will work with 
both the "modules" and the "site-packages" folder.

Do not create a Pydev project in the site-packages of web2py. It is impossible 
to configure things properly this way. Put the project outside of the web2py 
installation. I suggest to put it inside the Eclipse workspace.

Put the project outside of the web2py installation. (I keep it in the Eclipse 
the workspace.) 


Project site: https://github.com/Pierre-Thibault/neo-web2py-utils/

Comments or questions? [Join the user group](http://groups.google.com/group/neo-users)

Author: Pierre Thibault (pierre.thibault1 -at- gmail.com)

License: MIT
