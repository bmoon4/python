class Text(str):
    def duplicate(self):
        return self + self


tx = Text("Python")
print(tx.duplicate())


class TrackableList(list):
    def append(self, object):
        print("Append called")
        super().append(object)


tl = TrackableList()

tl.append("1")
tl.append("2")
tl.append("3")
print(tl)
