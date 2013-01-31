import string
import random
def random_string():
    return ''.join(random.choice(string.ascii_lowercase) for i in range(10))

strings = [random_string() for i in range(10000)]
print strings