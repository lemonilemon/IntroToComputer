width = 64//16
height = 48 

def toIntStr(s):
    if s == "1000000000000000":
        return "(~32767)"
    if s[0] == '0':
        return f"{int(s[1:], 2)}"
    return f"-{32768 - int(s[1:], 2)}"

mux = input("Mux or not(y/n):")
with open("bin.txt", "r") as f1:
    with open("bian.txt", "r") as f2:
        with open("code.txt", "w") as out:
            for r in range(height):
                line1 = f1.readline()
                line2 = f2.readline()
                for c in range(width): # 512 / 16
                    cnt = r * 32 + c
                    s1 = line1[c * 16 : (c + 1) * 16]
                    s1 = s1[::-1]
                    s2 = line2[c * 16 : (c + 1) * 16]
                    s2 = s2[::-1]
                    print(f"s1 = {s1}")
                    print(f"s2 = {s2}")
                    if(mux == "y"):
                        if s2 == "0000000000000000":
                            continue;
                        out.write(f"let screenLocation[{cnt}] = Lib.mux(screenLocation[{cnt}], ")
                        out.write(toIntStr(s1)); 
                        out.write(", ");
                        out.write(toIntStr(s2));
                        out.write(");\n");
                    else:
                        if s1 == "0000000000000000":
                            continue;
                        out.write(f"let screenLocation[{cnt}] = ")
                        out.write(toIntStr(s1)); 
                        out.write(";\n");

