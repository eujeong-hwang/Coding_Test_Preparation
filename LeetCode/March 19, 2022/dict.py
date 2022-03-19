class wth:
    def __init__(self, l):
        self.l = l
        print("만들어진 dictionary: {0}".format(self.l))

    def diction(self, s):
        if s in self.l:
            print("True")
        else:
            print("False")

h = wth({"A": 1, "B" :2, "C" :3})
h.diction("A")

## Conclusion
## 00 in XX -> finding whether the "KEY" of the dictionary is in XX or not.