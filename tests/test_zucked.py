import zucked as zd

def test_words():
    top_words = [('hi', 3), ('lol', 2), ('one', 1)]
    ms = zd.read_messages
    assert ms.top_50_words('Jordan Milne') == top_words
