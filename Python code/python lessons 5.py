Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:/Users/gabriel.harrison/Desktop/Python code/python lessons 5.py =
>>> x="hello world"
>>> 'hello' in x
True
>>> x=input()
hello
>>> 'hello' in x
True
>>>  x=input("type in any thing")
SyntaxError: unexpected indent
>>> x=input("type in any thing")
type in any thingbob
>>> 'hello' in x
False
>>> x.startswith('h')
False
>>> x.endswith('b')
True
>>> x.contains('bob')
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    x.contains('bob')
AttributeError: 'str' object has no attribute 'contains'
>>> 
