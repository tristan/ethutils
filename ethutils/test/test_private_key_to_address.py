from ethutils.keys import private_key_to_address

def test_private_key_to_address():

    tests = [
        ("0xb7ebdbb440a49fd109d3527bba46c7523e54a41306cc35a5f6141eb7d4df92fc", "0x777700f6442bdb754e0a6bef351c8e83e1e1a7ff"),
        ("0xdd9e0fe237c70a822faaa5bf33703784d7db029e745a6ec21d7eab1d7e727628", "0x7e5790eed073a68521fee742a4d59e6c21ab0ece"),
        ("0xf48c2de9ac587bac51507b04d2d9c9c99c52fac4cd1e20727dfcafdbe00e80ac", "0x12340cc443c52485a4f9a595c90fedba7331b9b3"),
        ("0xe441d1643cebdb9db6f81966782a5b592da90de0277ce8823f88281bf8ce1b36", "0x000045ad40b29f63ef6ba6e6ab2c1971cbe11935")
    ]

    for key, address in tests:
        assert private_key_to_address(key) == address
