import zucked

def test_words():
    d = [{
      "participants": [
        {
          "name": "User2"
        },
        {
          "name": "User1"
        }
      ],
      "messages": [
        {
          "sender_name": "User2",
          "timestamp_ms": 1502384278819,
          "content": "hey this is a silly test",
          "type": "Generic"
        },
        {
          "sender_name": "User1",
          "timestamp_ms": 1502383930331,
          "content": "yeah it is, yeah haha",
          "type": "Generic"
        },
      ],
      "title": "User2",
      "is_still_participant": True,
      "thread_type": "Regular",
      "thread_path": "inbox/User2"
    }]
    top_words = [('yeah', 2), ('it', 1), ('is', 1), ('haha', 1)]
    assert zucked.top_50_words(d,'User1') == top_words
