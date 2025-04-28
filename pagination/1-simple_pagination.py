import csv
import math
from typing import List

def index_range(page: int, page_size: int) -> tuple:
    """
    Return a tuple of (start index, end index) for the given page and page_size
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header row
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns the data for a specific page and page_size"""
        # Assert that page and page_size are integers greater than 0
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        # Get the indexes for the requested page using index_range
        start_index, end_index = index_range(page, page_size)

        # Retrieve the dataset
        dataset = self.dataset()

        # If the range is out of bounds, return an empty list
        if start_index >= len(dataset):
            return []

        # Slice the dataset to return the correct page
        return dataset[start_index:end_index]
