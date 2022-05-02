import math

def hex_to_binary(hex_str):
    # zfill ensures that leading zeros are kept
    return ''.join([bin(int(char,16))[2:].zfill(4) for char in hex_str])

def binary_to_int(binary_num):
    return int(binary_num,2)

def get_literal_value(p,i):
    binary_literal = []
    while p[i] != '0':
        i += 1
        binary_literal += p[i:i+4]
        i += 4
    i += 1
    binary_literal += p[i:i+4]
    i += 4
    literal = binary_to_int(''.join(binary_literal))    
    return literal, i

def packet_operation(packet_type,subpacket_values):
    if packet_type == 0:
        return sum(subpacket_values)
    if packet_type == 1:
        return math.prod(subpacket_values)
    if packet_type == 2:
        return min(subpacket_values)
    if packet_type == 3:
        return max(subpacket_values)
    if packet_type == 5:
        if subpacket_values[0] > subpacket_values[1]:
            return 1
        else:
            return 0
    if packet_type == 6:
        if subpacket_values[0] < subpacket_values[1]:
            return 1
        else:
            return 0
    if packet_type == 7:
        if subpacket_values[0] == subpacket_values[1]:
            return 1
        else:
            return 0

def parse_packet(p):    
    stack = []
    # Get the standard header: packet version and type ID
    i = 0
    packet_version = binary_to_int(p[i:i+3])
    version_sum = packet_version
    i += 3
    packet_type_id = binary_to_int(p[i:i+3])
    i += 3
    # Parse literal value packets
    if packet_type_id == 4:
        return get_literal_value(p,i)
    else:
        # Parse operator packets
        length_type_id = int(p[i])
        i += 1
        if length_type_id == 0:
            stack.append([packet_version, packet_type_id, i + 15 + binary_to_int(p[i:i+15]),-1, []])
            i += 15
        else:
            stack.append([packet_version, packet_type_id, -1, binary_to_int(p[i:i+11]), []])
            i += 11
            
    literal_val = None      
    
    while stack:
        s = stack[-1]
        if literal_val is not None:
            s[4].append(literal_val)
        # Cehck if the subpacket total length (s[2]) or number of subpackets (s[3]) has been reached
        if i == s[2] or s[3] == 0:
            literal_val = packet_operation(s[1],s[4])
            stack.pop()
            continue
            
        # If tracking number of packets, decrease by one each new packet
        if s[3] != -1:
            s[3] -= 1
        # Get standard header
        packet_version = binary_to_int(p[i:i+3])
        version_sum += packet_version
        i += 3
        packet_type_id = binary_to_int(p[i:i+3])
        i += 3
        # Parse literal value packets
        if packet_type_id == 4:
            literal_val,i = get_literal_value(p,i)
        # Parse operator packets  
        else:
            literal_val = None
            length_type_id = int(p[i])
            i += 1
            if length_type_id == 0:
                stack.append([packet_version, packet_type_id, i + 15 + binary_to_int(p[i:i+15]),-1, []])
                i += 15
            if length_type_id == 1:
                stack.append([packet_version, packet_type_id, -1, binary_to_int(p[i:i+11]), []])
                i += 11
    return literal_val

with open('../data/packet_decoder') as f:
    packet = f.read().strip()
    p = hex_to_binary(packet)
    
print(parse_packet(p))

