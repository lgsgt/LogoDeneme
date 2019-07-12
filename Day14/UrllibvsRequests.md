# Urllib vs Requests in Python

>Python contains libraries to interact with websites or used for opening HTTP URLs.
Example:**urllib/urllib2 , requests.**

## **1) urllib/urllib2:**

· Urllib is a python module used for opening HTTP URLs.

· It accomplish tasks such as basic authentication, getting cookies, serving GET/POST requests, error handling, viewing headers.

· Urllib2 is an improved Python module and provides additional functionalities to several methods.

· Hence some urllib methods have been replaced by urllib2 methods.

· In spite of having additional features, urllib cannot be completely replaced by urllib2 since the former provides important methods (_e.g., urlencode()_, used for generating GET query strings) that are absent in urllib2.

## **2) Python Requests:**

· ‘Requests’ is a simple, easy-to-use HTTP library written in Python.
· Requests makes interacting with Web services seamless.
<p align="center">
  <b>Features of Python Requests:</b><br>
</p>

· **Connection pooling**: There is a pool of connections, and a connection is released only once all its data has been read.

· **Sessions with cookie persistence**: You can make a session object and set certain parameters and cookie values. This allows you to persist these parameters and cookies across all requests made from the session instance.

· Python Requests encodes the parameters automatically so you just pass them as simple arguments, unlike in the case of urllib, where you need to use the method urllib.encode() to encode the parameters before passing them.

· Python Requests automatically decodes the response into Unicode.

· Python Requests handles multi-part file uploads, as well as automatic form-encoding.

· In Python, _Requests .get()_ is a method, auth is an optional parameter (since we may or may not require authentication).

· Python Requests supports the entire **restful API, i.e., all its methods – PUT, GET, DELETE, POST.**

· Unlike the urllib/urllib2 module, there is no confusion caused by Requests, as there is only a single module that can do the entire task.

· Can write easier and shorter code.

----

***Reference*** : [Informations](http://avi-urllib-vs-requests.blogspot.com/)

