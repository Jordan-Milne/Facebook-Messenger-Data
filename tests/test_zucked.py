import zucked as zd

def test_top_words():
    top_words = [('hi', 3), ('lol', 2), ('one', 1)]
    ms = zd.read_messages
    assert ms.top_words('Jordan Milne') == top_words


def test_top_convos():
    top_convo = [('Zark Muckerberg', 1)]
    ms = zd.read_messages
    assert ms.top_convos('Jordan Milne') == top_convo

# this test below passed locally but failed a lot on travis. I finally realized that the virtual machine travis-ci
# uses to test code is in a different timezone setting and was reading the timestamp_ms as a different time, failing the test.
def test_search_messages():
    search = [{'Message': 'hi hi hi lol lol one',
               'Sent to': 'Zark Muckerberg',
               'Date': '2020-05-11 15:59:15'}]
    ms = zd.read_messages
    assert ms.search_messages('Jordan Milne','one') == search
