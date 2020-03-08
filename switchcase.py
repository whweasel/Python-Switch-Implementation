class NotMatchedError(Exception):
    pass
class Matched(Exception):
    pass
class _Case(object):
    def __init__(self, function, case=None):
        self.function = function
        self.case = case

    def __call__(self, ref, *args):
        if ref == self.case:
            ref1 = self.function(ref, *args)
            Matched.msg = ref1
            raise Matched(ref1)
        else:
            raise NotMatchedError(ref)
def case(function=None, **kwargs):
    """ 
    Decorator, used to indicate a case inside a switch.
  
    The user may pass any keyword argument in, as the reference value, but it cannot be a positional one.
  
    Parameters: 
        ?: The value, used to compare with the reference.    
    """
    if function:
        return _Case(function)
    else:
        def wrapper(function):
            return _Case(function, list(kwargs.values())[0])
        return wrapper

@case
def _() -> None:
    """This function is used to set the @case decorator"""
    return None
def copyEnable(switch, ref):
    """DON'T USE THIS"""
    for thing in switch.__dict__:
        #print("{}  :  {}".format(thing, switch.__dict__[thing]))
        if isinstance(switch.__dict__[thing], _Case):
            try:
                switch.__dict__[thing](ref)
            except NotMatchedError:
                continue
            except Matched:
                return Matched.msg
def enable(switch: type, ref: any) -> object:
    """ 
    Activate a switch class.
  
    This allows the user to 'enter' the switch.
  
    Parameters: 
        switch (class): A class, representing a switch.
        ref (any): The value that the switch compares its cases to.
    
    Returns: 
        ref: The reference, this value is returned to allow the reference to be altered from within a case, therefore creating a dynamic state machine, if encased within a loop.
    """
    for thing in switch.__dict__:
        #print("{}  :  {}".format(thing, switch.__dict__[thing]))
        if isinstance(switch.__dict__[thing], _Case):
            try:
                switch.__dict__[thing](ref)
            except NotMatchedError:
                pass
            except Matched:
                return Matched.msg
    copyEnable(switch, ref="__default__")

    

    
