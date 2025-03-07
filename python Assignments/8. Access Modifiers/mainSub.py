from subclasses import _protected
class naming():
    def __init__(self):
        access=_protected()
        print(access._message)
obj=naming()
