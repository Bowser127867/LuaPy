"""LuaPy owned by WinbloxOS.

    WinbloxOS is a Roblox Group that makes games.
    You can learn more about WinbloxOS from here : https://winbloxos.pythonanywhere.com
"""

__version__ = "v1"

import time
import sys

class task():
    def wait(number:int = 1):
        time.sleep(number)

def wait(number:int = 1):
    time.sleep(number)

class Function:
    def __call__(self, name):
        def wrapper(params, func_body):
            # Ensure return works properly
            if "return " in func_body:
                func_body = func_body.replace("return ", "    return ")

            # Generate function definition dynamically
            func_code = f"def {name}({params}):\n" + "\n".join(f"    {line}" for line in func_body.strip().split("\n"))

            # Create a local scope and execute the function definition
            local_scope = {}
            exec(func_code, globals(), local_scope)

            # Return the dynamically created function
            return local_scope[name]

        return wrapper

function = Function()

def os_exit(code=0):
    sys.exit(code)

if __name__ == "__main__":
    exit("from luapy import task, function")

print(f"Running LuaPy {__version__}.Expect bugs and errors.")
