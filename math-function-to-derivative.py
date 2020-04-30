# Python 3.8.0 64-bit macOS
from sympy import *
from sympy.parsing.sympy_parser import parse_expr
from sympy.abc import _clash1
import re
import os

# Clean terminal screen
os.system("clear")

# Create x symbol
x = Symbol('x')

# User inputs
user_f_input = input("Enter a math function: f(x)= ")
user_f_input = user_f_input.replace("^", "**")
user_f_input = re.sub(r"(\d+)([a-z])", r"\1*\2", user_f_input)

user_df_input = input("Enter derivative function of f(x).  f'(x)= ")
user_df_input = user_df_input.replace("^", "**")
user_df_input = re.sub(r"(\d+)([a-z])", r"\1*\2", user_df_input)

# Create math function - e.g. f(x)=2x^2+4
mf = parse_expr(user_f_input)

# Calculate derivative function of 'f'
df = mf.diff(x)

# Check if math function equals to the calculated derivative function
if(df == parse_expr(user_df_input)):
    print("Correct answer.")
else:
    print ("Wrong answer. Solution: f'(x)= ", end = '')
    print (df)     
