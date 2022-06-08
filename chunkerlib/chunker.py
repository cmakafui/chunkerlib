from typing import Any, List, Optional

class Chunker(object):

    """
    A class representing the chunking functionality.
    :ivar List[str] items: The array of records of variable sizes.
    :ivar int max_record_size: The max output record size: Optional.
    :ivar int max_batch_size: The max output batch size: Optional.
    :ivar int max_records: The maximum number of records in output batch: Optional.
    
    """

    __slots__ = ("items", "max_record_size", "max_batch_size", "max_records")

    # Constants
    MAX_RECORD_SIZE = 1048576 # Maximum output record size (1MB in bytes)
    MAX_BATCH_SIZE = 5 * 1048576 # Maximum output batch size (5MB in bytes)
    MAX_RECORDS = 500 # Maximum number of records

    def __init__(self, items: List[str], max_record_size: Optional[int] = MAX_RECORD_SIZE, max_batch_size: Optional[int] = MAX_BATCH_SIZE, max_records: Optional[int] = MAX_RECORDS) -> None:
        """
        :param items: The array of records.
        :type items: List[str]
        :param max_record_size: The max output record size.
        :type max_record_size: Optional[int]
        :param max_batch_size: The max output batch size.
        :type max_batch_size: Optional[int]
        :param max_records: The maximum number of records in output batch.
        :type max_records: Optional[int]
        """
        self.items = items
        self.max_record_size = max_record_size
        self.max_batch_size = max_batch_size
        self.max_records = max_records


    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} object containing {len(self.items)} items.>"

    def chunk(self, get_size=len) -> List:
        """
        Splits the input to batches of records.
        :param items: The records to split.
        :type items: List[str]
        :return: The chunked list.
        :rtype: List[List[str]]
        """
        result = []
        item_counter = 0

        size = Chunker.MAX_BATCH_SIZE + 1
        
        for item in self.items:
            # Returns if maximum number of records exceeded
            if item_counter == self.max_records:
                return result
            item_counter += 1


            item_size = get_size(item)
            #  larger records should be discarded
            if item_size > self.max_record_size:
                continue

            size += item_size
            if size > self.max_batch_size:
                result.append([])
                size = item_size
            result[-1].append(item)

        return result