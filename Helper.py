# class Helper:
#     def __init__(self, work):
#         self.work = work
#     def __call__(self, work):
#         return f"I will help you with you {self.work}." \
#                f"Afterwards I will help you with {work}"
# helper = Helper("homework")
# print(helper("cleaning"))
# print(helper("eating"))
# import logging
# logging.basicConfig(level=logging.DEBUG,
#                     filename="logs.log", filemode="w",
#                     format="We have next logging massage: "
#                     "%(asctime)s:%(levelname)s-%(message)s"
#                     )
# try:
#     print(10/0)
# except Exception:
#     logging.exception("Exception")
# logging.debug("debug")
# logging.info("info")
# logging.warning("warning")
# logging.error("error")
# logging.critical("critical")

"""
>>>2+2
5
"""
if __name__ == "__main__":
    import doctest
    doctest.testmode()