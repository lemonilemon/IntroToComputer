with open("bin.txt", "r") as f:
    with open("code.txt", "w") as out:
        for r in range(256):
            line = f.readline()
            for c in range(32): # 512 / 16
                cnt = r * 32 + c
                s = line[c * 16 : (c + 1) * 16]
                s = s[::-1]
                if s == "0000000000000000":
                    continue
                out.write(f"let screenLocation[{cnt}] = ")
                if s == "1000000000000000":
                    out.write(f"(~32767);\n")
                elif s[0] == '0':
                    out.write(f"{int(s[1:], 2)};\n")
                else:
                    out.write(f"-{32768 - int(s[1:], 2)};\n")
