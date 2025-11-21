from utils.file_tools import read_file, line_count
from utils.text_tools import word_count, remove_extra_spaces, to_snake_case

# Demo usage
example_text = "Hello   world,   this is   a test."

print("Original:", example_text)
print("Cleaned:", remove_extra_spaces(example_text))
print("Word count:", word_count(example_text))
print("Snake case:", to_snake_case("Hello World Example"))

# File example (optional)
# print("Lines in file:", line_count("sample.txt"))
