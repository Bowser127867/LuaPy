from main import task,function,wait,math,run_lua,os_exit,require

task.wait() #It works cuz the value for number is 1 when it's empty.

task.wait(2) #This works aswell.

wait() #If you don't want to use task.wait() then use this instead.
wait(5) #this also works.

a = function("a")("", """
print("a")
""")

b = function("b")("", """
print("b")
""")

greet = function("greet")("name", """
print(f"Hello, {name}!")
""")

add = function("add")("x, y", """
return x + y
""")

math.random(1,5) #random.randint() works like this in lua.

if __name__ == "__main__":
    a()  # Output: a
    b()  # Output: b
    greet("Python User")  # Output: Hello, Python User!
    print(add(5, 3))  # Output: 8
    require("time") # We used time but you can use something else that require can find.
    run_lua("./tests/lua_test/main.lua") # Now with LuaPy v2 you can execute lua files in python using run_lua function.
    os_exit(111) # sys.exit() in lua.
    