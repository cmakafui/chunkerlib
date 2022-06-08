import random
from chunkerlib import chunker



def test_chunker_return_type():
    # Generate seeded random list of strings
    random.seed(0)
    random_list = [b'x' * random.randint(1, 2 * 10 // 3) for _ in range(10)]
    
    items = chunker.Chunker(random_list)
    assert type(items.chunk()) == list

def test_chunker_batch_size():
    max_batch_size = 10
    number_of_elements = 15

    # Generate seeded random list of strings
    random.seed(0)
    random_list = [b'x' * random.randint(1, 2 * max_batch_size // 3) for _ in range(number_of_elements)]
    
    items = chunker.Chunker(random_list, max_batch_size=max_batch_size)
    assert items.chunk() == [[b'xxxx', b'xxxx', b'x'], [b'xxx', b'xxxxx'], [b'xxxx', b'xxxx'], [b'xxx', b'xxxx', b'xxx'], [b'xxxxx', b'xx'], [b'xxxxx', b'xx', b'xxx']]


