## 3. Process User Records with Mixed Exceptions
def process_records(records):
    clean_records = []
    error_log = []

    for i, record in enumerate(records):
        try:
            name = record["name"]
            age = int(record["age"])
            score = float(record["score"])

        except (KeyError, TypeError) as e:
            error_log.append((i, type(e).__name__, str(e)))

        except ValueError as e:
            error_log.append((i, type(e).__name__, str(e)))

        else:
            clean_records.append({
                "name": name,
                "age": age,
                "score": score
            })

    return clean_records, error_log
def process_strict(records):
    try:
        clean_records, error_log = process_records(records)

        if len(error_log) > 0:
            raise RuntimeError(
                str(len(error_log)) + " record(s) failed to process"
            )

        return clean_records

    except RuntimeError:
        raise
records = [
    {"name": "Alice", "age": "25", "score": "88.5"},
    {"name": "Bob", "age": "abc", "score": "70"},
    {"name": "Carol", "age": "30"},
    "not a dict",
    {"name": "Dan", "age": "40", "score": "55.5"}
]
clean_records, error_log = process_records(records)

print("Clean Records:")
print(clean_records)

print("\nError Log:")
print(error_log)
try:
    process_strict(records)

except RuntimeError as e:
    print("\nStrict mode raised:")
    print("RuntimeError:", e)