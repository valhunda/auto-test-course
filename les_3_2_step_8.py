def test_input_text(expected_result, actual_result):
    assert actual_result == expected_result, \
        f"expected {expected_result}, got {actual_result}"


def checking_function_test_input_text():
    x = input()
    y = input()
    test_input_text(x, y)
