## 2. Safe List Access 
def safe_get(items, index):
    try:
        value = items[index]
        return ("ok", value)

    except IndexError:
        return ("error", "Index out of range")

    except TypeError:
        return ("error", "Index must be an int")

    except Exception as e:
        return ("error", "Unexpected error: " + str(e))
print(safe_get([10, 20, 30, 40], 2))
print(safe_get([10, 20, 30], 7))
print(safe_get([10, 20, 30], "1"))