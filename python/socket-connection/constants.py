NUM_BYTES: int = 32


def pad_message(message: str | bytes, size: int = NUM_BYTES) -> bytes:
    """Pad messages in order to match the size used by the socket.

    Args:
        message (str | bytes): Message to be padded.
        size (int, optional): Size used by the socket. Defaults to NUM_BYTES.

    Raises:
        ValueError: If message is longer than NUM_BYTES.

    Returns:
        bytes: The padded message.
    """
    length = len(message)
    if length > size:
        raise ValueError("Message is longer than the size.")

    return bytes(message, encoding="utf-8") + b" " * (size - length)
