import subprocess

def run_test(input_data, expected_output):
    """Run the word_freq.py script with the given input and compare output."""
    process = subprocess.run(
        ["python3", "word_freq.py"],
        input=input_data,
        text=True,
        capture_output=True
    )
    output = process.stdout.strip()
    assert output == expected_output, f"Expected: {expected_output}, Got: {output}"

# Test cases
def test_word_freq():
    run_test(
        "This is a test. This is only a test.",
        "this: 2\nis: 2\na: 2\ntest: 2\nonly: 1"
    )
    run_test(
        "Hello world! Hello everyone.",
        "hello: 2\nworld: 1\neveryone: 1"
    )
    run_test(
        "Python is fun. Python is powerful.",
        "python: 2\nis: 2\nfun: 1\npowerful: 1"
    )
    print("All tests passed!")

if __name__ == "__main__":
    test_word_freq()

