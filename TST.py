
import output, pandas


@output.output

def main():
    import string

    for i in string.ascii_uppercase:
        print(i)