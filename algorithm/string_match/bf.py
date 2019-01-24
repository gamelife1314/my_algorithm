
def bf(main: str, sub: str) -> int:

    main_length = len(main)
    sub_length = len(sub)

    if main_length <= sub_length:
        return 0 if main == sub else -1

    for i in range(0, main_length):
        for j in range(sub_length):
            if main[i + j] == sub[j]:
                if j == sub_length - 1:
                    return i
                else:
                    continue
            else:
                break

    return -1


def test():
    assert bf("abcdefghij", "abc") == 0
    assert bf("abc", "abcd") == -1
    assert bf("abcdefghij", "ebcd") == -1
    assert bf("abcdefghij", "cde") == 2


if __name__ == '__main__':
    test()
