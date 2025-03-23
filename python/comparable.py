from typing import Any, Protocol


class Comparable(Protocol):

    def __lt__(self, other: Any) -> bool:
        pass

    def __eq__(self, other: Any) -> bool:
        pass

    def __gt__(self, other: Any) -> bool:
        pass

    def __le__(self, other: Any) -> bool:
        pass

    def __ge__(self, other: Any) -> bool:
        pass
