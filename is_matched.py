def is_matched(expr):
    """Return true if all delimiters are
    properly match; False otherwise."""
    lefty ='({[' #opening delimiters
    reighty = ')}]' # respective closing delimiters
    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False
            if righty.index(c) != lefty.index(S.pop()):
                return False
    return S.is_empty()
