# Python主要存在四种命名：
# （1）object #公用方法
# （2）__object__ #内建方法，用户不要这样定义
# （3）__object #全私有，全保护（private）
# （4）_object #半保护（protected）

class Foo():
    def __init__(self):
        print('init')

    def public_method(self):
        print('This is public method')

    def __fullprivate_method(self):
        print('This is fullprivate_method')

    def _halfprivate_method(self):
        print('This is halfprivate_method')


f = Foo()
f.public_method()  # OK
f._halfprivate_method()  # OK
f._Foo__fullprivate_method()  # OK
f.__fullprivate_method()  # Error occur
