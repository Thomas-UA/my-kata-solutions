def zero(args=None): return 0 if args == None else int(0+args[1]) if args[0] == 'p' else int(0-args[1]) if args[0] == 'm' \
    else int(0*args[1]) if args[0] == 't' else int(0/args[1]) if args[0] == 'd' else None
def one(args=None): return 1 if args == None else int(1+args[1]) if args[0] == 'p' else int(1-args[1]) if args[0] == 'm' \
    else int(1*args[1]) if args[0] == 't' else int(1/args[1]) if args[0] == 'd' else None
def two(args=None): return 2 if args == None else int(2+args[1]) if args[0] == 'p' else int(2-args[1]) if args[0] == 'm' \
    else int(2*args[1]) if args[0] == 't' else int(2/args[1]) if args[0] == 'd' else None
def three(args=None): return 3 if args == None else int(3+args[1]) if args[0] == 'p' else int(3-args[1]) if args[0] == 'm' \
    else int(3*args[1]) if args[0] == 't' else int(3/args[1]) if args[0] == 'd' else None
def four(args=None): return 4 if args == None else int(4+args[1]) if args[0] == 'p' else int(4-args[1]) if args[0] == 'm' \
    else int(4*args[1]) if args[0] == 't' else int(4/args[1]) if args[0] == 'd' else None
def five(args=None): return 5 if args == None else int(5+args[1]) if args[0] == 'p' else int(5-args[1]) if args[0] == 'm' \
    else int(5*args[1]) if args[0] == 't' else int(5/args[1]) if args[0] == 'd' else None
def six(args=None): return 6 if args == None else int(6+args[1]) if args[0] == 'p' else int(6-args[1]) if args[0] == 'm' \
    else int(6*args[1]) if args[0] == 't' else int(6/args[1]) if args[0] == 'd' else None
def seven(args=None): return 7 if args == None else int(7+args[1]) if args[0] == 'p' else int(7-args[1]) if args[0] == 'm' \
    else int(7*args[1]) if args[0] == 't' else int(7/args[1]) if args[0] == 'd' else None
def eight(args=None): return 8 if args == None else int(8+args[1]) if args[0] == 'p' else int(8-args[1]) if args[0] == 'm' \
    else int(8*args[1]) if args[0] == 't' else int(8/args[1]) if args[0] == 'd' else None
def nine(args=None): return 9 if args == None else int(9+args[1]) if args[0] == 'p' else int(9-args[1]) if args[0] == 'm' \
    else int(9*args[1]) if args[0] == 't' else int(9/args[1]) if args[0] == 'd' else None

def plus(args): return ['p', args]
def minus(args): return ['m', args]
def times(args): return ['t', args]
def divided_by(args): return ['d', args]

assert seven(times(five())) == 35
assert four(plus(nine())) == 13
assert eight(minus(three())) == 5
assert six(divided_by(two())) == 3