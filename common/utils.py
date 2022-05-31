import random
from datetime import datetime, timedelta


def random_date():
    """
    This function will return a random datetime between two datetime
    objects.
    """
    start = datetime.now()
    end = start + timedelta(days=-365)
    random_date = start + (end - start) * random.random()
    return random_date
