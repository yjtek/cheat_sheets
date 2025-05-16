import argparse

# if __name__ == '__main__':
def main():
    '''
    USAGE [if using `if __name__ == "__main__"`]:
        > python3 argparse_cli.py yj --arg1 test --arg2 --arg3 --arg4 test1 --arg4 test2 --extra-string "send help"
        > Hi yj. Extra string: send help
        > args.arg1='test', args.arg2=123, args.arg3=True, args.arg4=['test1', 'test2']

    USAGE [if using `def main()`]:
        > 
    '''
    parser = argparse.ArgumentParser(description='Define arguments for your simple CLI greeting')
    parser.add_argument('name', help='Name of the person to greet')

    ## Double dash arguments are optional
    parser.add_argument('--extra-string', help='Append any string to the greeting')

    ## argparse also allows you to add predefined actions for specific cli commands. The default "action" is "store", which means parser stores whatever is provided in the commandline.  We'll go through some useful ones below, but you can see all of them here https://docs.python.org/3/library/argparse.html#action
    parser.add_argument('--arg1', action='store') # stores whatever string you provide

    parser.add_argument('--arg2', action='store_const', const=123) # stores some constant that you define. 

    # if flag is present, arg3 is 'true'/'false'
    parser.add_argument('--arg3', action='store_true') 
    # parser.add_argument('--arg3', action='store_false') 

    # Allows the argument to be called multiple times, and appends values to each other in the same list
    parser.add_argument('--arg4', action='append')
    
    args = parser.parse_args()
    print(f"Hi {args.name}. Extra string: {args.extra_string}")
    print(f"{args.arg1=}, {args.arg2=}, {args.arg3=}, {args.arg4=}")

    