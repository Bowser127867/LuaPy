from luapy import task, function, wait, os_exit

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

if __name__ == "__main__":
    a()  # Output: a
    b()  # Output: b
    greet("Python User")  # Output: Hello, Python User!
    print(add(5, 3))  # Output: 8
    os_exit(111) #