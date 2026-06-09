## 4. File Reader with try / except / else / finally
def read_numbers(path):
    numbers = []
    lines_read = 0

    try:
        with open(path, "r") as f:
            for line in f:
                number = float(line.strip())
                numbers.append(number)
                lines_read += 1

    except FileNotFoundError:
        return ("error", "File not found: " + path, 0)

    except PermissionError:
        return ("error", "Permission denied", lines_read)

    except ValueError:
        return ("error", "Invalid number on a line", lines_read)

    except Exception as e:
        return ("error", str(e), lines_read)

    else:
        total = sum(numbers)
        return ("ok", total, lines_read)

    finally:
        print("Done reading")

print(read_numbers("missing.txt"))
print(read_numbers("bad.txt"))