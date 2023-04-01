# import logging
# logging.basicConfig(level=logging.DEBUG,
#                     filename="logs.log", filemode="a",
#                     format="We have next logging message: "
#                            "%(asctime)s:%(levelname)s-%(message)s"
#                     )
# try:
#     print(10/0)
# except Exception:
#     logging.exception("Exception")

# assert 2+2 == 5, "wrong assert uslovie nepravilno"

def adder(*args, **kwargs):
    result = 0
    for _ in args:
        result += _
    for _ in kwargs.values():
        result += _
    return result
