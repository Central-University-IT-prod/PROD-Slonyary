import hashlib
import hmac

from shared.core.config import settings


def verify_user_data(data_check_string: str, hash) -> bool:
    """Verifying user sended telegram data by given hash."""
    secret_key = hashlib.sha256(settings.BOT_TOKEN.encode("utf-8")).hexdigest()
    correct_hash = hmac.new(
        bytes(secret_key.encode("utf-8")),
        bytes(data_check_string.encode("utf-8")),
        hashlib.sha256,
    ).hexdigest()
    return hmac.compare_digest(hash, correct_hash)
