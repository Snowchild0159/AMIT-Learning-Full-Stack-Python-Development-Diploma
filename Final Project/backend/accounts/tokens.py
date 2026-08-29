from django.core import signing
from django.conf import settings

# signed tokens for activation and password reset links.
# no database table needed: the token itself contains the user id
# and signing.loads() rejects it after max_age seconds.

def make_token(user_id, purpose):
    return signing.dumps({"user_id": user_id, "purpose": purpose})


def check_token(token, purpose):
    try:
        data = signing.loads(token, max_age=settings.ACTIVATION_MAX_AGE)
    except signing.BadSignature:
        return None
    if data.get("purpose") != purpose:
        return None
    return data.get("user_id")
