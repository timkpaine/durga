import random


def _gen_random(lst, start=0, end=10000):
    id = random.randint(start, end)
    while id in lst:
        id = random.randint(start, end)
    return id


def parseArgs(argv):
    args = []
    kwargs = {}
    for arg in argv:
        if '--' not in arg and '-' not in arg:
            print('ignoring argument: %s', arg)
            continue
        if '=' in arg:
            k, v = arg.replace('-', '').split('=')
            kwargs[k] = v
        else:
            args.append(arg.replace('-', ''))
    return args, kwargs
