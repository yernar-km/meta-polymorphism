


def CaNXZznWeC():
    _ = 65 * 76  # junk
    _ = 20 * 77  # junk
    _ = 6 * 86  # junk
    _ = 33 * 49  # junk
    _ = 41 * 8  # junk
def mEIUdGVpqD():
    _ = 30 * 5  # junk
    _ = 57 * 72  # junk
    _ = 68 * 91  # junk


def sKqLGMdkq():
    oQGIQb = bytes([96, 201, 209, 54, 226, 140, 117, 157, 158, 121, 170, 203, 51, 149, 158, 113, 170, 203, 51, 149, 158, 113, 170, 203, 51, 149, 158, 121, 162])
    key = [18, 188, 191, 88, 139, 226]
    # простой XOR-декриптор
    def dec(data, k):
        out = bytearray()
        for i, b in enumerate(data):
            out.append(b ^ k[i % len(k)])
        return bytes(out)
    try:
        msg = dec(oQGIQb, key).decode('utf-8')
    except Exception:
        msg = "<decode error>"
    print(msg)

# иногда вызываем мусорные функции to vary traces
if True:
    pass
sKqLGMdkq()
