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
    inputs = ["58"]
    output = run_test(inputs, seed=32)
    assert output == [
        "Welcome to the Random Math Quiz!",
        "You will be asked 1 question",
        "\nWhat is 19 + 39? ",
        "Correct!",
        "\nYou got 1/1 correct."
    ]


def test_some_incorrect():
    inputs = ["100", "-12", "-4", "37"]
    output = run_test(inputs, seed=61)
    assert output == [
        "Welcome to the Random Math Quiz!",
        "You will be asked 4 questions",
        "\nWhat is 72 + 28? ",
        "Correct!",
        "\nWhat is 38 - 42? ",
        "Incorrect. The correct answer was -4",
        "\nWhat is 1 * 8? ",
        "Incorrect. The correct answer was 8",
        "\nWhat is 46 - 9? ",
        "Correct!",
        "\nYou got 2/4 correct."
    ]


def test_all_incorrect():
    inputs = ["0", "0", "0", "0"]
    output = run_test(inputs, seed=24)
    assert output == [
        "Welcome to the Random Math Quiz!",
        "You will be asked 4 questions",
        "\nWhat is 3 * 4? ",
        "Incorrect. The correct answer was 12",
        "\nWhat is 25 + 22? ",
        "Incorrect. The correct answer was 47",
        "\nWhat is 11 * 2? ",
        "Incorrect. The correct answer was 22",
        "\nWhat is 3 * 12? ",
        "Incorrect. The correct answer was 36",
        "\nYou got 0/4 correct."
    ]
