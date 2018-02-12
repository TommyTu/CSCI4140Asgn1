#! /usr/bin/env python

import cgi
import cgitb
import time
import os
cgitb.enable()

print ("Content-Type: text/html")
print ("""
<html>
<body>
<h2>Hello World!</h2>
</body>
</html>
""")
