import sys

args = sys.argv[1:]
if len(args) > 0:
    joined_args = " ".join(args)
    reversed_ord = "".join(reversed(joined_args))
    reversed_case = "".join([c.upper() if c.islower() else c.lower() if c.upper() else c for c in reversed_ord])
    print(reversed_case)
