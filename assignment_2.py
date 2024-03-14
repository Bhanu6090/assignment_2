#Q1. How do you comment code in Python? What are the different types of comments? 
"""to comment the specific line we use '#' and if there are multiple line then we use there double inverted commas  """
#Q2. What are variables in Python? How do you declare and assign values to variables?
"""in python , variables are used to store data values , They act as containers for storing datat that can bereferenced and munipulated with in  a program 
   code to declare variable 
   x = 10 
   my_string = 'hello, world!'
   my_integer = 42
   my_float = 3.14 
   my_boolean = True
   """
#Q3. How do you convert one data type to another in Python?
"""there are two type of conversion are follow depends on the operation
1.Implicit Conversion (Automatic Conversion): Python automatically converts data types in certain situations, such as when performing operations
 involving different types. For example, when adding an integer to a float, Python automatically converts the integer to a float.

2.Explicit Conversion (Manual Conversion):

Using Built-in Functions: Python provides built-in functions like int(), float(), str(), bool(), etc., to convert one data type to another explicitly.
Using Constructor Functions: Constructor functions like int(), float(), str(), bool(), etc., can also be used to convert between data types. 
   """
# Q4. How do you write and execute a Python script from the command line?
"""
Write Your Python Script:
Use a text editor to write your Python script. Save the file with a .py extension, which indicates that it's a Python script. For example, you can create a file named myscript.py.

Navigate to the Directory:
Open a terminal or command prompt and navigate to the directory where your Python script is located. You can use the cd command to change directories.

Execute the Script:
Once you're in the correct directory, you can execute the Python script using the python command followed by the name of your script file. For example
python myscript.py
"""
#Q5. Given a list my_list = [1, 2, 3, 4, 5], write the code to slice the list and obtain the sub-list [2, 3].
"""
my_list = [1,2,3,4,5]
sub_list = my_list[1:3]
print(sub_list)
"""
#Q6. What is a complex number in mathematics, and how is it represented in Python?
"""x = 4+ 4j 
print(x.real)
print(x.imag)
print(x.conjugate())
"""
#Q7. What is the correct way to declare a variable named age and assign the value 25 to it? 
"""age = 25 """
# Q8. Declare a variable named price and assign the value 9.99 to it. What data type does this variable belong to?
"""
price = 9.99 
print(type(price))
print(int(price))
"""
# Q9. Create a variable named name and assign your full name to it as a string. How would you print the value of this variable?
"""
name = "bhanu dangi " # declaring the name variable to store the name data 
print(name) # to print the name variable 

"""
#Q10. Given the string "Hello, World!", extract the substring "World".
"""
my_string = "hello, World!"
print(my_string[7:12])
"""
#Q11. Create a variable named "is_student" and assign it a boolean value indicating whether you are currently a student or not.
"""

is_student = True

"""