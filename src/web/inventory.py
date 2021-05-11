
import typing


class Inventory:
    '''Object for tracking what files are available for download.'''

    def __init__(self):
        self.contents: typing.Dict[int, str] = {}
        # the next id to use
        self.next_id: int = 0

    def add(self, file_path: str) -> int:
        '''
        Add a new file path to the Inventory. Returns the file id.
        '''
        file_id = self.next_id
        self.contents[file_id] = file_path
        self.next_id += 1
        return file_id

    def get(self, file_id: int) -> str:
        '''
        Get the associated file path for this file id, or None if it
        does not already exist.
        '''
        return self.contents[file_id] if file_id in self.contents else None

    def contains(self, file_id: int) -> bool:
        '''
        Get whether or not the given file id is currently mapped to a file path.
        '''
        return file_id in self.contents

    def size(self) -> int:
        '''Get the number of file paths in the Inventory.'''
        return len(self.contents)

    def remove(self, file_id: int) -> bool:
        '''
        Remove the file path corresponding to the given file id. Returns false
        if the id does not correspond to an actual value.
        '''
        if not self.contains(file_id):
            return False

        del self.contents[file_id]

        return True

    def items(self):
        return self.contents.items()
