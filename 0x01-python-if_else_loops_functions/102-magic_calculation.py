 #!/usr/bin/python3
import dis
def magic_calculation(a, b, c):
    if (a < b):
        return (c)
    elif (c > b):
        return (a + b)
    else:
        return ((a + b) - c)
print(dis.dis(magic_calculation))
