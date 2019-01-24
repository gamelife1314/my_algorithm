def simple_hash(s: str, start: int, end: int) -> int:
    """
    求字符串子串的hash值，ASCII码求和
    :param s:
    :param start:
    :param end:
    :return:
    """
    result = 0
    for i in range(start, end + 1):
        result += ord(s[i])
    return result


def rk(main, pattern) -> int:
    """
    在字符串 main 中查找 pattern
    :param main:
    :param pattern:
    :return:
    """
    n = len(main)
    m = len(pattern)

    if n <= m:
        return 0 if pattern == main else -1

    # 生成子串hash表
    hash_table = [None] * (n - m + 1)
    hash_table[0] = simple_hash(main, 0, m - 1)
    for i in range(1, n - m + 1):
        hash_table[i] = hash_table[i - 1] - simple_hash(main, i - 1, i - 1) + simple_hash(main, i + m - 1, i + m - 1)
    hash_pattern = simple_hash(pattern, 0, m - 1)
    for index, h in enumerate(hash_table):
        if hash_table[index] == hash_pattern:
            if pattern == main[index:index + m]:
                return index
            else:
                continue

    return -1


def test():
    assert rk("abcdefghij", "abc") == 0
    assert rk("abc", "abcd") == -1
    assert rk("abcdefghij", "ebcd") == -1
    assert rk("abcdefghij", "cde") == 2


if __name__ == '__main__':
    test()

