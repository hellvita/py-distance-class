from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, int | float):
            return Distance(self.km + other)
        elif isinstance(other, Distance):
            return Distance(self.km + other.km)
        else:
            raise TypeError("other must be a Distance object or an integer")

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, int | float):
            self.km += other
        elif isinstance(other, Distance):
            self.km += other.km
        else:
            raise TypeError("other must be a Distance object or an integer")
        return self

    def __mul__(self, other: int | float) -> Distance:
        if isinstance(other, int | float):
            return Distance(self.km * other)
        else:
            raise TypeError("other must be a Distance object or an integer")

    def __truediv__(self, other: int | float) -> Distance:
        if isinstance(other, int | float):
            return Distance(round(self.km / other, 2))
        else:
            raise TypeError("other must be a Distance object or an integer")

    def __lt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, int | float):
            return self.km < other
        elif isinstance(other, Distance):
            return self.km < other.km
        else:
            raise TypeError("other must be a Distance object or an integer")

    def __gt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, int | float):
            return self.km > other
        elif isinstance(other, Distance):
            return self.km > other.km
        else:
            raise TypeError("other must be a Distance object or an integer")

    def __eq__(self, other: Distance | int | float) -> bool:
        if isinstance(other, int | float):
            return self.km == other
        elif isinstance(other, Distance):
            return self.km == other.km
        else:
            raise TypeError("other must be a Distance object or an integer")

    def __le__(self, other: Distance | int | float) -> bool:
        if isinstance(other, int | float):
            return self.km <= other
        elif isinstance(other, Distance):
            return self.km <= other.km
        else:
            raise TypeError("other must be a Distance object or an integer")

    def __ge__(self, other: Distance | int | float) -> bool:
        if isinstance(other, int | float):
            return self.km >= other
        elif isinstance(other, Distance):
            return self.km >= other.km
        else:
            raise TypeError("other must be a Distance object or an integer")
