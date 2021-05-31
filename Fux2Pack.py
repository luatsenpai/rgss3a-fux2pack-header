#!/usr/bin/env python3

import sys
import struct

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Loi, khong tim thay goi ma hoa')
        sys.exit(1)
    hdr = struct.Struct('<8sI')
    with open(sys.argv[1], 'rb+') as f:
        header = hdr.unpack_from(f.read(12))
        if header[0] != b'Fux2Pack':
            print('Goi Fux2Pack that bai, hay thu “Rgss_Extract V1.3.exe”')
            sys.exit(1)
        # Old and good number theory
        metadata_key = ((header[1] - 3) * 0x38E38E39) & 0xffffffff
        print(hex(header[1]), '->', hex(metadata_key))
        f.seek(0)
        f.write(hdr.pack(b'RGSSAD\x00\x03', metadata_key))
    print('Tep “Game.rgss3a” da duoc giai ma, hay dung “Rgss_Extract V1.3.exe” de giai ra')