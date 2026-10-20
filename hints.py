def get_hint(secret_number: int) -> str:
    parity = "even" if secret_number % 2 == 0 else "odd"
    return f"The number is {parity}."
