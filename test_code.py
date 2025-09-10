import random
import assignment
import mock_input_tests

def run_test(mocked_inputs, seed=None):
    # set seed so random questions are predictable
    if seed is not None:
        random.seed(seed)

    mock_input_tests.set_keyboard_input(mocked_inputs)
    assignment.main()
    return mock_input_tests.get_display_output()


def test_all_correct():
    # With seed=1, the first 5 problems are predictable
    # Random sequence (1–10) → (3, 10), (2, 5), (2, 8), (8, 8), (7, 4)
    # Answers: 30, 10, 16, 64, 28
    inputs = ["30", "10", "16", "64", "28"]
    output = run_test(inputs, seed=1)
    assert any("You got 5/5 correct." in line for line in output)


def test_some_incorrect():
    inputs = ["30", "99", "99", "64", "99"]  # intentionally wrong guesses
    output = run_test(inputs, seed=1)
    assert any("You got 2/5 correct." in line for line in output)


def test_all_incorrect():
    inputs = ["0", "0", "0", "0", "0"]
    output = run_test(inputs, seed=1)
    assert any("You got 0/5 correct." in line for line in output)
