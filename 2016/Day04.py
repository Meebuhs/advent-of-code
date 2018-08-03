import re, collections


def find_real_rooms(rooms):
    """
    Calculates each room's checksum to verify if it is real. Any real room's name is then decoded.
    :param rooms: the list of rooms
    """
    sector_sum = 0
    regex = r'([a-z-]+)(\d+)\[(\w+)\]'
    for room in rooms:
        for name, sector, checksum in re.findall(regex, room):
            counter = collections.Counter(name.replace('-', ''))
            counts = [(-n, c) for c, n in counter.most_common()]
            most_common = "".join(c for n, c in sorted(counts))
            if most_common[:5] == checksum:
                sector_sum += int(sector)
            decoded_name = decode(name, sector)
            if "northpole" in decoded_name:
                print("The decoded name of the storage room is {}and its sector ID is {}".format(decoded_name, sector))
    print("The sum of sector IDs for all real rooms  is {}".format(sector_sum))


def decode(name, sector):
    """
    Decodes the string name using a caeser cipher with a key defined by the sector ID.
    :param name: the room name to decode
    :param sector: the room's sector ID
    :return: the decoded name
    """
    key = int(sector) % 26
    decoded_name = ""
    for character in name:
        if character == '-':
            decoded_name += ' '
        else:
            letter = ord(character) + key
            if letter > ord('z'):
                letter -= 26
            decoded_name += chr(letter)
    return decoded_name


if __name__ == "__main__":
    with open("input.txt") as f:
        find_real_rooms(f.readlines())
