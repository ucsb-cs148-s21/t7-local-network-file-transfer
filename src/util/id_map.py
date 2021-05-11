
import typing

T = typing.TypeVar('T')


class IdMap(typing.Generic[T]):
    '''Object for tracking what files are available for download.'''

    def __init__(self):
        self.contents: typing.Dict[int, T] = {}
        # the next id to use
        self.next_id: int = 0

    def add(self, val: T) -> int:
        '''
        Add a new value to the IdMap. Returns the value id.
        '''
        val_id = self.next_id
        self.contents[val_id] = val
        self.next_id += 1
        return val_id

    def get(self, val_id: int) -> T:
        '''
        Get the associated value for this value id, or None if it
        does not already exist.
        '''
        return self.contents[val_id] if val_id in self.contents else None

    def contains(self, val_id: int) -> bool:
        '''
        Get whether or not the given value id is currently mapped to a value.
        '''
        return val_id in self.contents

    def size(self) -> int:
        '''Get the number of values in the IdMap.'''
        return len(self.contents)

    def remove(self, val_id: int) -> bool:
        '''
        Remove the value corresponding to the given value id. Returns false
        if the id does not correspond to an actual value.
        '''
        if not self.contains(val_id):
            return False

        del self.contents[val_id]

        return True

    def items(self) -> typing.ItemsView[int, T]:
        return self.contents.items()
