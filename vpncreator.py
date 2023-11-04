import os

# Generate a private key
privatekey = os.popen("wg genkey").read().strip()

# Specify the address for the WireGuard interface
address = "10.0.0.1/24"  # Change this to your desired address and subnet

# Write the configuration to a file
with open("vpn.conf", "w") as vpn:
    vpn.write(
        f'''
[Interface]
Address = {address}
PrivateKey = {privatekey}
DNS = 1.1.1.1
'''
    )
