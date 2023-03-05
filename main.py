import random




# # def adder(*args, **kwargs):
# #     result = 0
# #     for _ in args:
# #         result += _
# #     for _ in kwargs.values():
# #         result += _
# #     return result
#
# def adder(*args, **kwargs):
#     result = 0
#     for _ in args:
#         if type(_) == int or type(_) == bool or type(_) == float:
#             result += _
#         else:
#             try:
#                 result += float(_)
#                 continue
#             except (ValueError, TypeError):
#                 pass
#             try:
#                 result += int(_)
#                 continue
#             except (ValueError, TypeError):
#                 pass
#     for _ in kwargs.values():
#         if type(_) == int or type(_) == bool or type(_) == float:
#             result += _
#         else:
#             try:
#                 result += float(_)
#                 continue
#             except (ValueError, TypeError):
#                 pass
#             try:
#                 result += int(_)
#                 continue
#             except (ValueError, TypeError):
#                 pass
#     return result

def adder(*args, **kwargs):
    result = 0
    for _ in args:
        result += _
    for _ in kwargs.values():
        result += _
    return result
