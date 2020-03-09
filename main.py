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
