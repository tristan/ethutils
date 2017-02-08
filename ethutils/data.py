import binascii

def data_decoder(data):
    """Decode `data` representing unformatted data."""
    if not data.startswith('0x'):
        data = '0x' + data

    if len(data) % 2 != 0:
        data = '0x0' + data[2:]

    return binascii.unhexlify(data[2:])

def data_encoder(data, length=None):
    """Encode unformatted binary `data`.

    If `length` is given, the result will be padded like this: ``data_encoder('\xff', 3) ==
    '0x0000ff'``.
    """
    s = binascii.hexlify(data).decode('ascii')
    if length is None:
        return '0x' + s
    else:
        return '0x' + s.rjust(length * 2, '0')
