import collections


def decode_repetition(data):
    word_length = len(data[0].strip())
    counters = [collections.Counter() for x in range(word_length)]
    for line in data:
        for column in range(word_length):
            counters[column].update(line[column])
    most_common, least_common = "", ""
    for counter in counters:
        most_common += counter.most_common(1)[0][0]
        least_common += counter.most_common()[len(counter) - 1][0]
    print("The most common characters give the code {}".format(most_common))
    print("The least common characters give the code {}".format(least_common))


if __name__ == "__main__":
    with open('input.txt') as f:
        decode_repetition(f.readlines())
