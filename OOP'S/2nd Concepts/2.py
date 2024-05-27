# Private(like) attributes & methods
# Conceptual Implementations in Python
# Private attributes & methods are meant to be used only
# within the class and are not accessible from outside
# the class

class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass # private property
    def reset_pass(self):
        print(self.__acc_pass)

acc1 = Account("12345", "Adsffsadsfgssdf")
print(acc1.acc_no)
print(acc1.reset_pass())
# print(acc1.acc_pass)