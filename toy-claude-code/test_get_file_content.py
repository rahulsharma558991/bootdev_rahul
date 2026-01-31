from functions.get_file_content import get_file_content
from config import MAX_CHARS

def test():
    result = get_file_content("calculator", "lorem.txt")
    # Check that result starts with MAX_CHARS of content and ends with truncation message
    assert len(result) > MAX_CHARS
    assert result[MAX_CHARS:].startswith("[...File")
    assert result.endswith("characters]")

    result = get_file_content("calculator", "main.py")
    print(result)

    result = get_file_content("calculator", "pkg/calculator.py")
    print(result)

    result = get_file_content("calculator", "/bin/cat")
    print(result)

    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print(result)

if __name__ == "__main__":
    test()