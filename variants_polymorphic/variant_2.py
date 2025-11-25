


def VmZZxiqKxI():
    _ = 87 * 33  # junk
    _ = 3 * 36  # junk
def HcyCQypQPg():
    _ = 23 * 98  # junk
    _ = 41 * 3  # junk
    _ = 87 * 36  # junk
    _ = 23 * 21  # junk
    if False:
        print('never')



def EuikXrSyp():
    WXrNoN = bytes([162, 107, 154, 226, 113, 19, 137, 60, 241, 63, 213, 165, 57, 84, 207, 52, 241, 55, 213, 165, 57, 84, 207, 52, 241, 55, 213, 173, 49])
    key = [208, 30, 244, 140, 24, 125, 238, 29]
    # простой XOR-декриптор
    def dec(data, k):
        out = bytearray()
        for i, b in enumerate(data):
            out.append(b ^ k[i % len(k)])
        return bytes(out)
    try:
        msg = dec(WXrNoN, key).decode('utf-8')
    except Exception:
        msg = "<decode error>"
    print(msg)

# иногда вызываем мусорные функции to vary traces
if False:
    pass
EuikXrSyp()
