import ipaddress

def format_binary_with_underline(binary_str, underline_length):
    underlined = ''.join(
        char + ('\u0332' if i < underline_length else '') 
        for i, char in enumerate(binary_str.replace('.', ''))
    )
    result = ''
    for i in range(32):
        result += underlined[i]
        if (i + 1) % 8 == 0 and i != 31:
            result += '.'
    return result

def ip_to_bin_str(ip):
    return '.'.join(f'{int(octet):08b}' for octet in ip.split('.'))

def analyze_subnet(ip_str, mask_str):
    network = ipaddress.ip_network(f"{ip_str}/{mask_str}", strict=False)
    mask_bin = ip_to_bin_str(mask_str)
    mask_bits = mask_bin.replace('.', '')
    leading_ones = mask_bits.find('0') if '0' in mask_bits else 32
    ip_bin = ip_to_bin_str(ip_str)
    ip_bin_underline = format_binary_with_underline(ip_bin, leading_ones)

    hosts = list(network.hosts())

    print(f"\nIP-адрес хоста: {ip_str}")
    print(f"Маска подсети: {mask_str}\n")
    print(f"IP в двоичном виде:    {ip_bin}")
    print(f"Маска в двоичном виде: {mask_bin}\n")
    print(f"IP с подчёркнутой сетевой частью (кол-во подчеркнутых бит / {leading_ones}):\n")

    if hosts:
        print("Диапазон доступных IP-адресов (двоичный):")
        print(f"От {ip_to_bin_str(str(hosts[0]))}")
        print(f"До {ip_to_bin_str(str(hosts[-1]))}\n")
        host_count = len(hosts)
        blocks_256 = host_count // 256
        adjusted_count = host_count - blocks_256 * 2
        print(f"Диапазон доступных IP-адресов (десятичный): от {hosts[0]} до {hosts[-1]}")
        print(f"Количество доступных адресов для хостов (без вычета): {host_count}")
        print(f"Количество доступных адресов для хостов (с вычетом): {adjusted_count}\n")
    else:
        print("Нет доступных IP-адресов в подсети.")

    print(f"Адрес подсети: {network.network_address}(/ {leading_ones})")
    print(f"Широковещательный адрес: {network.broadcast_address}")    
    print(f"Тип подсети: {'частная' if network.is_private else 'внешняя (публичная)'}\n")

ip = "217.65.4.113"
mask = "255.255.254.0"
analyze_subnet(ip, mask)