def test_substring(full_string, substring):
    assert substring in full_string, \
        f"expected '{substring}' to be substring of '{full_string}'"


def checking_test_substring():
    string, substring = input().split()
    test_substring(string, substring)


checking_test_substring()
