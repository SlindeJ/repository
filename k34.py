from stanfordkarel import *


class ktools:

    def m(self):
        """Shorthand for Move"""
        move()

    def tl(self):
        """Turn Left"""
        turn_left()

    def tr(self):
        """Turn Right"""
        self.tl()
        self.tl()
        self.tl()

    def ta(self):
        """Turn Around"""
        self.tl()
        self.tl()

    def pick(self):
        """Pick Beeper"""
        pick_beeper()

    def put(self):
        """Put Beeper"""
        put_beeper()

    def put2(self):
        """Put 2 beepers in a line"""
        self.put()
        self.m()
        self.put()

    def put5(self):
        self.put2()
        self.m()
        self.put2()
        self.m()
        self.put()

    def h(self):
        """Print H using beepers"""
        self.tl()
        self.put5()
        self.tr()
        self.m()
        self.m()
        self.m()
        self.tr()
        self.put5()
        self.ta()
        self.m()
        self.m()
        self.tl()
        self.m()
        self.put2()
        self.tl()
        self.m()
        self.m()
        self.tl()
        self.m()
        self.m()
        self.m()
        self.m()

    def ddiagp(self):
        """Modified ddiag to pick up beepers in double diagonal lines"""
        self.m()
        self.pick()
        self.tl()
        self.m()
        self.tl()
        self.m()
        self.pick()
        self.ta()
        self.m()
        """Can chain or add if nessisary"""


def main():
    """ Karel code goes here! """
    kt = ktools()
    kt.m()
    kt.m()
    kt.m()
    kt.m()
    kt.m()
    kt.tl()
    """Now the real code starts"""
    kt.m()
    kt.tl()
    kt.m()
    kt.ta()
    kt.ddiagp()
    kt.ddiagp()
    kt.ddiagp()
    kt.ddiagp()
    kt.ta()
    kt.m()
    kt.m()
    kt.m()
    kt.m()
    kt.m()
    kt.m()
    kt.tl()
    kt.m()
    kt.m()
    kt.tl()
    kt.ddiagp()
    kt.ddiagp()
    kt.ddiagp()
    kt.ddiagp()
    kt.tr()
    kt.m()
    kt.m()
    kt.m()
    kt.m()
    kt.m()
    kt.m()
    kt.m()
    kt.tr()
    kt.m()
    kt.tr()
    pass


if __name__ == "__main__":
    run_karel_program()
