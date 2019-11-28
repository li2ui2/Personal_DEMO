# # 单个修饰器
# def w1(func):
#     def inner():
#         print('...验证权限...')
#         func()
#     return inner
#
#
# @w1
# def f1():
#     print('f1 called')
#
#
# @w1
# def f2():
#     print('f2 called')
#
#
# f1()
# f2()


# # 多个修饰器
# def makeBold(fun):
#     print('----a----')
#
#     def inner():
#         print('----1----')
#         print(fun())
#         return '<b>' + fun() + '</b>'
#     return inner
# def makeItalic(fun):
#     print('----b----')
#
#     def inner():
#         print('----2----')
#         print(fun())
#         return '<i>' + fun() + '</i>'
#     return inner
# @makeBold
# @makeItalic
# def ttest():
#     print('----c----')
#     print('----3----')
#     return 'hello python decorator'
# ret = ttest()
# print(ret)
