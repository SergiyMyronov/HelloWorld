"""
2. Нужно сделать что бы код не падал, а был обработан каждый случай в отдельном except.
 На код стоит посмотреть внимательно, может что-то в нем не так)
"""

# RANDOM RAISE

import random

try:
    raise random.choice([ZeroDivisionError, ImportError, KeyError, UnicodeError, StopIteration])
except ZeroDivisionError:
    print("ERROR: ZeroDivisionError")
except ImportError:
    print("ERROR: ImportError")
except KeyError:
    print("ERROR: KeyError")
except UnicodeError:
    print("ERROR: UnicodeError")
except StopIteration:
    print("ERROR: StopIteration")

