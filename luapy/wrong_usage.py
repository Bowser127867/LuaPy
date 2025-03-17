from luapy import task, function, wait

#task.wait()

Any = object

h = Any

task.wait(h) #WRONG!!!!! It needs a number not a object.

task.wait("1") #WRONG!!!!! It needs a number not a string.

#function

function()("", """
print("oops")
""")  #WRONG!!!!! Function name is required!

function("test")("", 123)  #WRONG!!!!! Function body is not a string.

f = function("f")("a, b, c", """
return a + b + d 
""")
f(1, 2, 3)  #WRONG!!!!! Runtime error - d ISN'T DEFINED!!!!!

#wait()

wait(h) #WRONG!!!!! It needs a number not a object.

wait("1") #WRONG!!!!! It needs a number not a string.