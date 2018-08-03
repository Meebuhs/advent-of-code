import hashlib


def generate_passwords(door):
    """
    Generates the passwords for both doors by computing md5 hashes using the door ID and an iterating
    :param door: The ID of the door
    """
    first_password = ""
    second_password = ['_'] * 8
    second_password_length = 0
    index = 0
    print("Generating both passwords.")
    while second_password_length < 8:
        m = hashlib.md5((door + str(index)).encode('utf-8')).hexdigest()
        if m[:5] == "00000":
            if len(first_password) < 8:
                first_password += m[5]
                print("{} hash found for {}{}. Added character {} to first password ({})".format(m, door, index, m[5],
                                                                                                 first_password))
            if not m[5].isalpha() and 0 <= int(m[5]) <= 7 and second_password[int(m[5])] == '_':
                second_password[int(m[5])] = m[6]
                second_password_length += 1
                print("{} hash found for {}{}. Added character {} to second password in position {} ({})".format(
                                                                        m, door, index, m[6], m[5], second_password))
        index += 1
    print("\nThe password for the first door of {} is {}".format(door, first_password))
    print("The password for the second door of {} is {}".format(door, ''.join(x for x in second_password)))


if __name__ == "__main__":
    door = input().strip()
    generate_passwords(door)
