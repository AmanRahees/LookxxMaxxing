from django.core import signing
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str


def encode_id(item_id):
    signed_id = signing.dumps(item_id)
    encoded_id = urlsafe_base64_encode(force_bytes(signed_id))
    return encoded_id


def decode_id(encoded_id):
    decoded_signed_id = force_str(urlsafe_base64_decode(encoded_id))
    original_id = signing.loads(decoded_signed_id)
    return original_id
