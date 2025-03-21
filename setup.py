from setuptools import setup, find_packages

setup(
    name="luapy",  # Package name (used for pip install)
    version="0.1.1",  # First version
    author="Bowser127867",
    author_email="kenny.animator.dotexe@gmail.com",
    description="A Lua-inspired scripting environment for Python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Bowser127867/LuaPy",  # Your GitHub repository
    packages=find_packages(),
    install_requires=[
        "lupa",  # Ensure Lupa (LuaJIT) is installed
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)