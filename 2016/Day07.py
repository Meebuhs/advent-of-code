import re


def process_ips(ips):
    """
    Counts the number of IP addresses which support TLS and SSL.
    :param ips: the list of IP addresses to check.
    """
    tls_count, ssl_count = 0, 0
    for ip in ips:
        parts = re.split('[\[\]]', ip)
        outside, inside = ' '.join(parts[::2]), ' '.join(parts[1::2])
        if find_abba(outside) and not find_abba(inside):
            tls_count += 1
        if find_ssl(outside, inside):
            ssl_count += 1
    print(tls_count)
    print(ssl_count)


def find_abba(block):
    """
    Returns true if the specified block contains an autonomous bridge bypass annotation. An ABBA is defined as a
    substring of length four of the form abba. For example 'poop' or 'boob'.
    :param block: the block to check.
    """
    return True if any(a == d and b == c and a != b in block for a, b, c, d in
                       zip(block, block[1:], block[2:], block[3:])) else False


def find_ssl(outside, inside):
    """
    Returns true if the two specified blocks contain a compliant area-broadcast accessor. An ABA is defined as compliant
    if in the outside block, there exists a substring of length three of the form aba and in the inside block a
    corresponding substring bab exists.
    :param outside: the outside block to check.
    :param inside: the inside block to check.
    """
    return True if any(a != b and a == c and b+a+b in inside for a, b, c in
                       zip(outside, outside[1:], outside[2:])) else False


if __name__ == "__main__":
    with open("input.txt") as f:
        process_ips(f.readlines())
