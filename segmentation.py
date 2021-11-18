import sys


def is_valid_ipv4(ipv4: str) -> bool:
    """Vérifie que l'adresse IPv4 est valide"""
    values = [int(e) for e in ipv4.split('.')]

    if len(values) != 4:
        return False

    for e in values:
        if int(e) < 0 or int(e) > 255:
            return False

    return True


def ipv4_to_binary(ipv4) -> str:
    """Retourne la représentation binaire d'une adresse IPv4"""
    if not is_valid_ipv4(ipv4):
        print("Error: bad IPv4 format :", ipv4)
        sys.exit()

    result = ''
    values = [int(e) for e in ipv4.split('.')]

    for e in values:
        result += f'{e:08b}' + '.'

    return result.rstrip('.')


def cidr(snmask) -> str:
    """Retourne le CIDR (Classless Inter-Domain Routing)"""
    mask = ipv4_to_binary(snmask).replace('.', '', 3)
    bit_num = 0

    for i in range(0, 32):
        if mask[i] == '1':
            bit_num += 1
        else:
            break

    return bit_num


def max_ip_count(snmask) -> int:
    """Retourne le nombre maxi d'adresse(s) utilisable(s)"""
    return 2**(32 - cidr(snmask)) - 2


def subnet_ID(ipv4, snmask) -> str:
    """Retourne l'identifiant sous-réseau (IDSR)"""
    ip = [int(e) for e in ipv4.split('.')]
    mask = [int(e) for e in snmask.split('.')]

    return f'{ip[0] & mask[0]}.{ip[1] & mask[1]}.{ip[2] & mask[2]}.{ip[3] & mask[3]}'


def broadcast_ip(ipv4, snmask) -> str:
    """Retourne l'adresse de broadcast (BRD)"""
    ip = [int(e) for e in ipv4.split('.')]
    mask = [255 - int(e) for e in snmask.split('.')]

    return f'{ip[0] | mask[0]}.{ip[1] | mask[1]}.{ip[2] | mask[2]}.{ip[3] | mask[3]}'


ip_address = input('Adresse IP         : ')
subnet_mask = input('Masque sous-réseau : ')

print()
print('IP    :', ipv4_to_binary(ip_address), f'({ip_address})')
print('MSR   :', ipv4_to_binary(subnet_mask), f'({subnet_mask})')
print('CIDR  :', cidr(subnet_mask))
print('Nb IP :', max_ip_count(subnet_mask))
print('IDSR  :', subnet_ID(ip_address, subnet_mask))
print('BRD   :', broadcast_ip(ip_address, subnet_mask))
