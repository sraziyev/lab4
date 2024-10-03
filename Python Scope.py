'''Consider the following code:'''
x = 300
def myfunc():
  x = 200
myfunc()
print(x)
'''What will be the printed result?'''

#300

'''Consider the following code:'''
x = 300
def myfunc():
  global x
  x = 200
myfunc()
print(x)

#200

'''Which statement keyword can be used for variables inside nested function?'''
#nonlocal