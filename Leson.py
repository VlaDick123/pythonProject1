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

# def adder(*args, **kwargs):
#     result = 0
#     for _ in args:
#         result += _
#     for _ in kwargs.values():
#         result += _
#     return result

result = []


def divider(a, b):
    if a < b:
        raise ValueError
    if b > 100:
        raise IndexError
    return a / b


data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8: 4}
for key in data:
    res = divider(key, data[kem])
    result.append(res)

print(result)
