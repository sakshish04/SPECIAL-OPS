def reroute_gateway(from_bank, to_bank):
    """Action: Moves traffic to a healthy bank."""
    return f"🛠️ ACTION: Traffic successfully moved from {from_bank} to {to_bank}. Success rate should stabilize shortly."

def alert_human_manager(error_message):
    """Action: Escalates to Aryan when an issue is too complex or risky."""
    return f"📢 ALERT: Escalated to Aryan. Message: {error_message}"

def apply_guardrail(amount):
    """Guardrail: Checks if the amount is too high for autonomous action."""
    # Aryan's Rule: Anything over 10,000 needs a human eye!
    if amount > 10000:
        return "BLOCKED: High-value transaction risk. Human approval required."
    return "APPROVED"