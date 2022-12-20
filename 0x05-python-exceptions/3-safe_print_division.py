#!/usr/bin/python3


def safe_print_division(a, b):
    result = 0
    try:
        result = a/b
        return result

    except TypeError:
        return None
    except ValueError:
        return None
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {:.1f}".format(result))

    print()
