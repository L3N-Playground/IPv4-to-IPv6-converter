#idea: [YT:Florian Dalwigk] - https://www.youtube.com/watch?v=OjBJvXcuE-I


def decimal_to_binary(decimal, bits):
    binary = ''
    while bits != 0:
        bits -= 1
        if decimal - (2 ** bits) >= 0:
            binary += '1'
            decimal -= (2 ** bits)
        else:
            binary += '0'
    return binary


def binary_to_decimal(binary):
    base = len(binary)
    decimal = 0
    bits = 0
    while bits != base:
        if binary[base - 1 - bits] == '1':
            decimal += (2 ** bits)
        else:
            pass
        bits += 1
    return decimal


def decimal_to_hexadecimal(ipv4_address):

    ipv6_address = '0000:0000:0000:0000:0000:ffff:'
    hexadecimal_index = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                         'a', 'b', 'c', 'd', 'e', 'f']

    ipv4_address_block = ipv4_address.split('.', 3)
    ipv4_address_block_length = len(ipv4_address_block)

    for i in range(ipv4_address_block_length):

        block_decimal = ipv4_address_block[i]
        block_binary = decimal_to_binary(int(block_decimal), 8)

        block_binary_p1 = block_binary[:4]
        block_binary_p2 = block_binary[4:]

        block_decimal_p1 = binary_to_decimal(block_binary_p1)
        block_decimal_p2 = binary_to_decimal(block_binary_p2)

        block_hexadecimal_p1 = hexadecimal_index[block_decimal_p1]
        block_hexadecimal_p2 = hexadecimal_index[block_decimal_p2]

        ipv6_address += block_hexadecimal_p1
        ipv6_address += block_hexadecimal_p2

        if i == 1:
            ipv6_address += ':'

    return ipv6_address


input_ipv4_address = input("IPv4 address input:")
print("IPv4 address:", input_ipv4_address)

output_ipv6_address = decimal_to_hexadecimal(input_ipv4_address)
print("IPv6 address:", output_ipv6_address)
