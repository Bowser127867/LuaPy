from main import task,time,function,wait,math,run_lua,os_exit,require

#Set h to Any (which is object.)

Any = object
h = Any

#task.wait()
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

#math.random()

math.random(4) #WRONG!!!!! math.random() needs 2 numbers not 1 number.

math.random() #WRONG!!!!! math.random() needs 2 numbers.There isn't any in this situation.

math.random("1","2") #WRONG!!!!! math.random needs 2 numbers,NOT 2 STRINGS!!!!!!

#require()

require() #WRONG!!!!! require needs a module for it to work.

require(h) #WRONG!!!!! require needs a module not a type.

require("require_test") #WRONG!!!!! Since require uses importlib it must be something that importlib recongizes.

#run_lua()

run_lua() #WRONG!!!!! It needs the path of the file.