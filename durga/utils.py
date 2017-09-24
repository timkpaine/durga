

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
