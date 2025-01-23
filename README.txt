PRECaL User Guide

This guide will help you set up and use "Python Routines Enhancing Calculations and Logic", or PRECaL, which includes examples and a sandbox for experimenting with math functions.

Step 1: Extract the ZIP File
1. Locate the .zip file you downloaded.
2. Right-click the file and choose Extract All (or use a similar extraction tool).
3. Choose a folder to extract the files and click Extract.

Step 2: Install Python from the Microsoft Store
1. Open the Microsoft Store.
2. Search for Python in the store.
3. Download and install Python 3.x (the latest version).
4. Once installed, Python will automatically be added to your system's PATH.

Step 3: Install Visual Studio Code from the Microsoft Store
1. Open the Microsoft Store.
2. Search for Visual Studio Code in the store.
3. Download and install Visual Studio Code.
4. Once installed, you can open Visual Studio Code from the Start menu.

Step 4: Run Math Examples.py
1. Open the extracted folder in a code editor (e.g., Visual Studio Code or IDLE).
2. Open the file Math Examples.py, which includes:
   import PreCal
   from sympy.abc import *
   from sympy import *
3. Run the file:
   - In IDLE: Press F5.
   - In VS Code: Press Ctrl+F5 (or use the terminal with python "Math Examples.py").

Step 5: Experiment in Math Sandbox.py
1. Open Math Sandbox.py. This file serves as a blank template where you can test functions from Precal.py.
2. Example:
   import PreCal

   # Test simplifying a quadratic equation
   roots = PreCal.quadratic_formula(1, -7, 12)
   print(f"Roots of the quadratic: {roots}")

   # Plot a quadratic equation
   PreCal.standard_quadratic(a=1, b=2, c=-3)
3. Save the file and run it as you did with Math Examples.py.

Step 6: Keep Files in the Same Folder
Ensure all three files (Precal.py, Math Examples.py, Math Sandbox.py) are in the same folder. This ensures that the Precal.py library can be imported correctly.

Step 7: Debugging and Troubleshooting
1. Missing Python Installation: Ensure Python is installed from the Microsoft Store.
2. Libraries Not Installed: Ensure the necessary libraries (e.g., matplotlib, numpy, sympy) are installed.
3. File Not Found: Confirm all files are in the same folder.

Happy coding! Enjoy experimenting with PRECaL!
