#!/usr/bin/env python3

import builtins


class Replacer:
    def __enter__(self):
        #  Replace system method by inadequate one
        assert (self.original is None)
        self.original = builtins.print
        builtins.print = exit   # No printing allowed. Use logging instead

    def __exit__(self, comment):
        # replace it back
        builtins.print = self.original
        self.original = None  # set back to None to denote it is not used


# class Sample:
#     pass


if __name__ == "__main__":
    print("Hello")

    with Replacer as r:   # AttributeError: __enter__
        print("Can you see it?")

    print("Bye")  # Ok to print here
