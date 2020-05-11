import zucked as zd

def test_top_words():
    top_words = [('hi', 3), ('lol', 2), ('one', 1)]
    ms = zd.read_messages
    assert ms.top_words('Jordan Milne') == top_words


def test_top_convos():
    top_convo = [('Zark Muckerberg', 1)]
    ms = zd.read_messages
    assert ms.top_convos('Jordan Milne') == top_convo


def test_search_messages():
    search = [{'Message': 'hi hi hi lol lol one',
               'Sent to': 'Zark Muckerberg',
               'Date': '2016-06-09 11:46:54'}]
    ms = zd.read_messages
    assert ms.search_messages('Jordan Milne','one') == search
