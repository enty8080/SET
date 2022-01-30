#!/usr/bin/env python3

import struct

from hatasm import HatAsm
from hatvenom import HatVenom

hatasm = HatAsm()
hatvenom = HatVenom()

message = "Hasta la vista, baby!"

data = (
    b"\xe8" + struct.pack("<I", len(message.encode() + b"\x00") + 0xd) +
    b"/usr/bin/say\x00" +
    message.encode() + b"\x00"
)

print("[*] Assembling shellcode...")
shellcode = hatasm.assemble('x64',
    """
    start:
        xor rax, rax
        mov eax, 0x200003b
    """
) + data + hatasm.assemble('x64',
    """
    end:
        mov rdi, [rsp]
        lea r10, [rdi+0xd]
        xor rdx, rdx
        push rdx
        push r10
        push rdi
        mov rsi, rsp
        syscall
    """
)

print("[i] Generated shellcode:")
for line in hatasm.hexdump(shellcode):
    print(line)

print("[*] Writing shellcode to Mach-O...")
hatvenom.generate_to('macho', 'x64', shellcode)
