import hashlib

class ToyAgent:
    def __init__(self, allowlist_tools=None):
        self.allowlist_tools = allowlist_tools or ["search", "summarise"]
        self.logs = []

    def naive_act(self, user_prompt, retrieval_tool):
        retrieved = retrieval_tool.fetch()
        prompt = user_prompt + "\n" + retrieved
        self.logs.append({"stage": "naive_prompt", "prompt": prompt})

        if "transfer" in prompt.lower():
            self.logs.append({"stage": "action", "action": "CALL_PAYMENT_API"})
            return "CALL_PAYMENT_API"

        return "NO_ACTION"

    def hardened_act(self, user_prompt, retrieval_tool):
        retrieved = retrieval_tool.fetch()

        digest = hashlib.sha256(retrieved.encode()).hexdigest()
        self.logs.append({"stage": "retrieved", "digest": digest})

        clean = retrieved.replace("<!--", "").replace("-->", "")
        prompt = user_prompt + "\n" + clean

        if "transfer" in prompt.lower():
            if "APPROVAL_TOKEN" not in prompt:
                return "BLOCKED_BY_POLICY"

            if "payment_api" not in self.allowlist_tools:
                return "DENIED_TOOL"

            return "CALL_PAYMENT_API"

        return "NO_ACTION"
