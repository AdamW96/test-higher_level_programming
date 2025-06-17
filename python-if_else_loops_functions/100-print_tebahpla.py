#!/usr/bin/python3
print("".join(chr(122 - i).lower() if i % 2 == 0 else chr(122 - i).upper() for i in range(26)), end="")
