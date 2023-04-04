"""
1) . What is the difference between enclosing a list comprehension in square brackets and
parentheses?

ANSWER..

Enclosing a list comprehension in square brackets creates a list, while enclosing it in parentheses creates a generator object.


----------------------------------------------------------------------------------------------------------------


2) What is the relationship between generators and iterators?

ANSWER..

Generators are a type of iterator that are used to lazily generate values on the fly, rather than
creating a complete sequence in memory all at once. In other words, a generator is a special type
of iterator that is defined using a function.


----------------------------------------------------------------------------------------------------------------


3) What are the signs that a function is a generator function?

ANSWER..

A function is a generator function if it contains a "yield" statement. This statement tells Python
to temporarily suspend the execution of the function, and return a value to the caller. The function
can be resumed later on from where it left off, allowing it to generate a sequence of values over time.


----------------------------------------------------------------------------------------------------------------


4) What is the purpose of a yield statement?

ANSWER..

The purpose of a "yield" statement in a generator function is to temporarily suspend the execution of
the function, and return a value to the caller. The function can be resumed later on from where it left
off, allowing it to generate a sequence of values over time.



----------------------------------------------------------------------------------------------------------------


5) What is the relationship between map calls and list comprehensions? Make a comparison and
contrast between the two.

ANSWER..

Map calls and list comprehensions are both used to transform a sequence of values into another
sequence of values, based on some function or transformation rule. The main difference between
the two is that map returns an iterator object, while a list comprehension returns a list. Map
is generally used for larger sequences or when memory is a concern, while list comprehensions
are preferred for smaller sequences. Additionally, map can be slower than a list comprehension
due to the overhead of creating the iterator object.



----------------------------------------------------------------------------------------------------------------


"""
