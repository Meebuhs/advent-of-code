from itertools import takewhile, islice


def decompress(data, nest):
    answer = 0
    chars = iter(data)
    for c in chars:
        if c == '(':
            n, m = map(int, [''.join(takewhile(lambda x: x not in 'x)', chars)) for _ in range(2)])
            s = ''.join(islice(chars, n))
            answer += (decompress(s, nest) if nest else len(s)) * m
        else:
            answer += 1
    return answer


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().strip()
    print("Answer #1:", decompress(data, False))
    print("Answer #2:", decompress(data, True))
