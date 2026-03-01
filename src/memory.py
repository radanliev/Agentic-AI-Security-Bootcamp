import time
import json
import uuid
import hashlib
import hmac

class SignedMemoryStore:
    def __init__(self, secret_key: bytes):
        self.key = secret_key
        self.store = {}

    def write(self, entry: str, author: str, session_id: str):
        timestamp = time.time()
        meta = {"author": author, "timestamp": timestamp, "session": session_id}
        payload = json.dumps({"entry": entry, "meta": meta}, sort_keys=True).encode()

        signature = hmac.new(self.key, payload, hashlib.sha256).hexdigest()
        entry_id = str(uuid.uuid4())

        self.store[entry_id] = {
            "payload": payload.decode(),
            "signature": signature,
            "meta": meta,
        }

        return entry_id

    def read(self, entry_id: str):
        record = self.store.get(entry_id)
        if not record:
            return None

        payload = record["payload"].encode()
        expected = hmac.new(self.key, payload, hashlib.sha256).hexdigest()

        return {
            "payload": payload.decode(),
            "signature_valid": hmac.compare_digest(expected, record["signature"]),
            "meta": record["meta"],
        }
