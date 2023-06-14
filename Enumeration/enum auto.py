from enum import Enum, auto

class State(Enum):
    PENDING = auto()
    FULLFILLED = auto()
    REJECTED = auto()

    def __str__(self):
        return f'{self.name(self.value)}'

for state in State:
    print(state.name, state.value)

