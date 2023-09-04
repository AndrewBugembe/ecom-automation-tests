import random
import string


def get_random_email_password(domain=None, prefix=None):
    if not domain:
        domain = "bugie.com"
    if not prefix:
        prefix = "testuser"

    random_string_length = 15
    random_email = "".join(random.choices(string.ascii_lowercase, k=random_string_length))
    email = prefix + '_' + random_email + '@' + domain

    password_length = 10
    random_password = "".join(random.choices(string.ascii_letters, k=password_length))
    random_info = {"email":email, 'password':random_password}
    return random_info