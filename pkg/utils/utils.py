UINT_256_MAX = 2**256 - 1
UINT_256_CEILING = 2**256
UINT_255_MAX = 2**255 - 1
UINT_255_CEILING = 2**255
UINT_255_NEGATIVE_ONE = -1 + UINT_256_CEILING

def unsigned_to_signed(value):
    if value <= UINT_255_MAX:
        return value
    else:
        return value - UINT_256_CEILING