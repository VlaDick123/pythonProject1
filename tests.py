# class My_Test(unittest.TestCase):
#     def test_args(self):
#         self.assertEqual(adder(2, 2), 4)
#
#     def test_kwargs(self):
#         self.assertEqual(adder(a=10, b=11), 21)
#
#     def test_mixed(self):
#         self.assertEqual(adder(1, a=2), 3)
#
#     def test_diff(self):
#         x = 10
#         y = 0
#         self.assertEqual(adder(0, -5, y, a=x), 5)
#
#     def test_wrong_datatype(self):
#         self.assertEqual(adder("5", "abc", 10), 15)

def adder(*args, **kwargs):
    result = 0
    for _ in args:
        if type(_) == int or type(_) == bool or type(_) == float:
            result += _
        else:
            try:
                result += float(_)
                continue
            except (ValueError, TypeError):
                pass
            try:
                result += int(_)
                continue
            except (ValueError, TypeError):
                pass
        for _ in kwargs.values():
            if type(_) == int or type(_) == bool or type(_) == float:
                result += _
            else:
                try:
                    result += float(_)
                    continue
                except (ValueError, TypeError):
                    pass
                try:
                    result += int(_)
                    continue
                except (ValueError, TypeError):
                    pass
    return result