import random
from chunkerlib import chunker



def test_chunker_return_type():
    """
    Given a random list, assert the type of the chunk function is a list.

    :param items: list
    :return: list
    """

    # Generate seeded random list of strings
    random.seed(0)
    random_list = [b'x' * random.randint(1, 2 * 10 // 3) for _ in range(10)]
    
    items = chunker.Chunker(random_list)
    assert type(items.chunk()) == list

def test_chunker_batch_size():
    """
    Given a list, assert the result of the chunk method is equal.

    :param items: list
    :param max_batch_size: int

    :return: list
    """
    listing = ['ab', 'bc', 'cd', 'de', 'ef']
    max_batch_size = 4
    items = chunker.Chunker(listing, max_batch_size=max_batch_size)
    assert items.chunk() == [['ab', 'bc'], ['cd', 'de'], ['ef']]

def test_chunker_record_size():
    """
    Given a list, assert the result of the chunk method is equal.

    :param items: list
    :param max_record_size: int

    :return: list
    """
    listing = ['ab', 'bc', 'cdfsgdfgsd', 'de', 'ef']
    max_record_size = 4
    items = chunker.Chunker(listing, max_record_size=max_record_size)
    assert items.chunk() == [['ab', 'bc', 'de', 'ef']]

def test_chunker_max_records():
    """
    Given a list, assert the result of the chunk method is equal.

    :param items: list
    :param max_records: int

    :return: list
    """
    listing = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    max_records = 2
    items = chunker.Chunker(listing, max_records=max_records)
    assert items.chunk() == [['a', 'b'], ['c', 'd'], ['e', 'f'], ['g', 'h']]

