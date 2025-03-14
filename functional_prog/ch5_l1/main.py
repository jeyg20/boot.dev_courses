def get_logger(formatter):
    def logger(*args):
        print(formatter(*args))

    return logger


# Don't edit below this line


def test(first, errors, formatter, timestamp=None):
    print("Logs:")
    logger = get_logger(formatter)
    for err in errors:
        if timestamp:
            logger(first, err, timestamp)
        else:
            logger(first, err)
    print("====================================")


def colon_delimit(first, second):
    return f"{first}: {second}"


def dash_delimit(first, second):
    return f"{first} - {second}"


def timestamp_delimit(first, second, timestamp):
    return f"[{timestamp}] {first} -> {second}"


def main():
    db_errors = [
        "out of memory",
        "cpu is pegged",
        "networking issue",
        "invalid syntax",
    ]
    test("Doc2Doc FATAL", db_errors, colon_delimit)

    mail_errors = [
        "email too large",
        "non alphanumeric symbols found",
    ]
    test("Doc2Doc WARNING", mail_errors, dash_delimit)

    system_errors = [
        "disk failure",
        "kernel panic",
    ]
    test(
        "SYSTEM ERROR",
        system_errors,
        timestamp_delimit,
        timestamp="2023-10-01 12:00:00",
    )


main()
