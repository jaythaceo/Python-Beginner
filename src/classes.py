#!/usr/env python

# base class
class Bird:
    def __init__(self, kind, call):
        self.call = call
        self.kind = kind

    def do_call(self):
        print "a %s goes %s" % (self.kind, self.call)

class Parrot(Bird):
    def __init__(self):
        Bird.__init__(self,"Parrot", "KahKah!")

class Cukoo(Bird):
    def __init__(self):
        Bird.__init__(self, "Cuckoo", "Cuckoo!")


if __name__ == "__main__":
    parrot = Parrot()
    cuckoo = Cukoo()

    parrot.do_call()
    cuckoo.do_call()


