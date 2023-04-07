result = []
def divider(a, b):
    try:
        if a < b:
            raise ValueError("a < b")
        if b > 100:
            raise IndexError("b > 100")
        return a/b
    except ValueError as e:
        print(f"ValueError: {e}")
    except IndexError as e:
        print(f"IndexError: {e}")
    except TypeError as e:
        print(f"TypeError: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return None

data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8: 4}
for key in data:
    res = divider(key, data[key])
    if res is not None:
        result.append(res)

print(result)