def word_count(text):
    """Return the number of words in a string."""
    return len(text.split())


def remove_extra_spaces(text):
    """Remove extra spaces and clean text."""
    return " ".join(text.split())


def to_snake_case(text):
    """Convert text to snake_case."""
    cleaned = text.replace("-", " ").replace(".", " ")
    words = cleaned.strip().split()
    return "_".join(word.lower() for word in words)
