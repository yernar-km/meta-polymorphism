


def dhGfXqXtqs():
    _ = 29 * 100  # junk
    _ = 63 * 80  # junk
def kkBngofVdg():
    _ = 58 * 16  # junk
    _ = 20 * 78  # junk
    _ = 89 * 19  # junk
    _ = 15 * 51  # junk


def UIEaTZWAk():
    TJJzCx = bytes([129, 162, 0, 103, 240, 53, 95, 198, 112, 210, 246, 71, 40, 176, 122, 17, 198, 120, 210, 254, 79, 32, 184, 114, 25, 206, 112, 210, 254])
    key = [243, 215, 110, 9, 153, 91, 56, 231, 81]
    # простой XOR-декриптор
    def dec(data, k):
        out = bytearray()
        for i, b in enumerate(data):
            out.append(b ^ k[i % len(k)])
        return bytes(out)
    try:
        msg = dec(TJJzCx, key).decode('utf-8')
    except Exception:
        msg = "<decode error>"
    print(msg)

# иногда вызываем мусорные функции to vary traces
if True:
    pass
UIEaTZWAk()
