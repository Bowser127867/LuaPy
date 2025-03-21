"""LuaPy owned by WinbloxOS.

    WinbloxOS is a Roblox Group that makes games.
    You can learn more about WinbloxOS from here : https://winbloxos.pythonanywhere.com
"""

__version__ = "v1"

import time
import sys
import random
from lupa import LuaRuntime

class task():
    """time.sleep() in lua in another way."""
    def wait(number:int = 1):
        time.sleep(number)

def wait(number:int = 1):
    """time.sleep() in lua.
    """
    time.sleep(number)

class Function:
    """This does the thing that def thingy does.
    """
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
    """sys.exit() in lua."""
    sys.exit(code)

import importlib

def require(module_name):
    """This does what import does."""
    try:
        return importlib.import_module(module_name)
    except ModuleNotFoundError:
        print(f"Module '{module_name}' not found.")
        return None

class math():
    """math."""
    def random(n1:int,n2:int):
        """random.randint() in lua."""
        random.randint(n1,n2)

# Initialize Lua runtime
lua = LuaRuntime(unpack_returned_tuples=True)

def run_lua(file_path):
    """Runs lua files in phyton"""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lua_code = file.read()
            lua_env = lua.eval(f"""
            (function()
                {lua_code}
                return _G  -- Return the global Lua environment
            end)()
            """)
            return lua_env  # Return the Lua global table
    except Exception as e:
        print(f"🛑 Lua Execution Error: {e}")
        return None

if __name__ == "__main__":
    exit("from luapy import task, function, os_exit, require, math")

print(f"Running LuaPy {__version__}.Expect bugs and errors.")
