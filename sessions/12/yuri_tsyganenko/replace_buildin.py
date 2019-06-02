#!/usr/bin/env python3

import builtins


class Replacer:
    def __enter__(self):
        #  Replace system method by inadequate one
        # assert (self.original is None)
        self.original = builtins.print
        # def fake_print(*args):
        #     pass  # exit(0)
        # builtins.print = exit   # No printing allowed. Use logging instead
        builtins.print = builtins.exit   # No printing allowed. Use logging instead

    def __exit__(self, comment, *args):
        # replace it back
        builtins.print = self.original
        self.original = None  # set back to None to denote it is not used


# class Sample:
#     pass


if __name__ == "__main__":
    print("Hello")

    with Replacer() as r:
        print("Can you see it?")  # Why this is still printed (in red - as stderr)! - due to incorrect param?
        print(0)       # just exit.   #  Why "Process finished with exit code 1"   Expected exit code 0
        print("What about now - do you see it?")

    print("Bye")  # Ok to print here
