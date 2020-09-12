Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> print('My Grandfather's name is Kanaylal Modi')
      
SyntaxError: invalid syntax
>>> print('My Grandfather\'s name is Kanaylal Modi')
My Grandfather's name is Kanaylal Modi
>>> name='Paarin Modi \'The Great'
>>> print(name)
Paarin Modi 'The Great
>>> favorite_number=3
>>> type(favorite_number)
<class 'int'>
>>> favorite_number="3"
>>> type(favorite_number)
<class 'str'>
>>> mood="delighted"
>>> print("I'm so {mood} to learn code in Python!!)
      
SyntaxError: EOL while scanning string literal
>>> print("I'm so {mood} to learn code in Python!!")
I'm so {mood} to learn code in Python!!
>>> print(f"I'm so {mood} to learn code in Python!!")
I'm so delighted to learn code in Python!!
>>> 