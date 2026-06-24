from textchunk import do_chunking


def test_do_chunking_returns_list():

    text = "This is a sample text. It has multiple sentences. We want to see if it gets chunked properly."

    result = do_chunking(text)

    assert isinstance(result, list)


def test_do_chunking_returns_chunks():
    # this checks that the function actually splits text into more than one chunk
    # repeat 50 times to make it long enough to split
    text = "This is sentence one. " * 50
    result = do_chunking(text)
    assert len(result) > 1


def test_do_chunking_empty_text():
    # this checks what happens when we pass empty text
    result = do_chunking("")
    assert result == []
