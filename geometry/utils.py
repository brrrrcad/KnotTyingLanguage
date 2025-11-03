def split_param(p):
    if isinstance(p, tuple) and len(p) == 2:
        return p[0], p[1]
    else:
        return p, p