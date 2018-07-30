import greet
from wurlitzer import pipes


def main():
    with pipes() as (out, err):
        greet.greet('World')

if __name__ == "__main__":
    main()
