# Abstract
Most traditional languages, including Visual Basic, C, C#, C++, Java, and JavaScript, include switch statements. 
Switch statements act very much like a light switch. Referencing a variable, a group of cases are compared, and when the comparison is true, a block of code is executed.
They are a much better solution to long chains of if/elif/else statements, which are a direct violation of [PEP8](https://www.python.org/dev/peps/pep-0008/), and are very hard to read. With switch statements, a single condition, a value, is stated, and along with that, the block of code.
Often times, switch statements point to functions.
# Implementation
Consider the following sample code:
```py
#I'm working on a switch for Python. This is what I have so far.

from switchcase import case, enable

class mySwitch:
    @case(1)
    def case1(ctx):
        print("This is a SWITCH statement.")
        print("Oh, yeah, integer, 1, blah blah blah")
        return ctx
    @case(2)
    def case2(ctx):
        print("Second case, where you put the integer two.")
        return ctx
    @case("__default__")
    def __default__(ctx):
        print("Default case.")
        return ctx
enable(mySwitch, 6)

```
Ignoring all the comments and fancy stuff, what we have is this:
```py
class mySwitch:
    @case(1)
    def case1(ctx):
        print("This is a SWITCH statement.")
        print("Oh, yeah, integer, 1, blah blah blah")
        return ctx
    @case(2)
    def case2(ctx):
        print("Second case, where you put the integer two.")
        return ctx
    @case("__default__")
    def __default__(ctx):
        print("If no case is matched")
        return ctx
enable(mySwitch, 2)
```
You can see a few things. I want you to focus on the ``@case`` decorator. First of all, all these methods are inside a ``mySwitch`` class.
The ``@case`` decorator has one argument, representing the case's value.
Example:
```py
@case(1)
```
or...
```py
@case("bar")
```
This is the exact same thing that the following Java code snippet does:
```java
case "bar" : //code
```
In Java, or other languages, all you need is the case, then the code, followed by a ``break;``. However, since this isn't officially part of Python, there are a few changes.
For example, the code to be executed for each case, is a function. This should be obvious, as ``@case`` is a decorator, and decorators can only decorate function or method declarations.
Consider the following code:
```py
@case("baz")
def case1(ctx):
    print("Hello World!")
    return ctx
```
As you see, there is a method, named ``case1(ctx)``. It does not matter the name of the method, but it is suggested to use ``case<number or code>``, to avoid code confusion, as well as to make sure two cases don't have the same method name. Perhaps a more suitable course of action, would be to give the method a name, a description of what the method does in that specific case.
Example:
```py
@case("printHelloWorld")
def print_hello_world(ctx):
    print("Hello World!")
    return ctx
```
As you can see, the case names also follow this construct. A coding convention, as set forth by me, is to name case conditions, if they are strings, as you would in any compiled language. Instead of using underscores, one would define a string like ``"stringContent"``

As for the definition of the method, the name does not matter on a technical level, as long as it is unique in the scope of the switch. You may notice that there is an argument, ``ctx``, passed to the method. This acts as a reference of context, the current case. The switch goes through every case using a for loop, and checks if the case's condition matches the current index variable in memory. If it matches, the corresponding method is called. ``ctx`` is not actually passed to the method, but to ``@case``, where it is handled, and then, it is passed to the method.
You may also notice that ``ctx`` is returned. That is not to match code convention, but to allow dynamic switches, that can change the value of ctx, within a method, whilst returning it.

CTX is needed, just like cls and self are needed in classes.

You may also notice a special case:
```py
@case("__default__")
    def __default__(ctx):
        print("If no case is matched")
        return ctx
```
This is a default case, in the event that no matching case is found, a fallback case is used, in order to prevent the program from suddenly exiting, or worse, bugs.
The name of the string is ``"__default__"``, to avoid conflicts, just in case there is a case with a string, called ``"default"``.
It is also a convention to name the function ``__default__``, for the same reason the condition must be named that, however, it is not required to do so.

And now, we've reached the end. As you know, states, in Python, using this implementation, are actually classes. Therefore, they cannot be executed on their own. What is nice about Python, is that there is a function that does that for us. Remember that ``enable`` that was imported? We're gonna use that.
```py
enable(mySwitch, 2)
```
The first argument shall be the switch itself, aka the class, and the second argument is the value to be compared to by the switch.

And putting it all together, this is the code:
```py
from switchcase import case, enable

class mySwitch:
    @case(1)
    def case1(ctx):
        print("This is a SWITCH statement.")
        print("Oh, yeah, integer, 1, blah blah blah")
        return ctx
    @case(2)
    def case2(ctx):
        print("Second case, where you put the integer two.")
        return ctx
    @case("__default__")
    def __default__(ctx):
        print("Default case.")
        return ctx
enable(mySwitch, "fdk")
```
When we run this code, the following is outputted:
```json
Out[1]:Default case.
```
That is because we have our passed switch variable, as a case which doesn't exist. If we change the enable() call to this:
```py
enable(mySwitch, 2)
```
, we get the following:
```json
Out[1]:Second case, where you put the integer two.
```
# Creating a Finite State Machine using Switches
So that's the gist of it all. Now, let's briefly talk about making a finite state machine with this. A finite state machine, is very different from a pure switch, in that it repeats, and that the value of the reference, may change.
Here is an example:
```py
class stateMachine:
    @case("idle")
    def idle(ctx):
        print("Idle state. About to change that (=")
        ctx = "attack"
        return ctx
    @case("attack")
    def attack(ctx):
        print("Attack state. Awaiting next state.")
        ctx = "sleep"
        return ctx
    @case("sleep")
    def sleep(ctx):
        print("Sleep state. Loop has been finished.")
        ctx = "__finish__"
        return ctx
ctx = "idle"
while ctx != "__finish__":
    ctx = enable(stateMachine, ctx)
```
I'll just leave you with that. If there are any bugs, go ahead and tell me via Reddit, or GitHub. And as always, have a great day.
