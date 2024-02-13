import numpy as np

class NumpyDict(dict):
    """Numpy dict is a dict with overloaded mathimatical operations.
    It allows you to calculate different layers with certan names and apply
    to them single equation to describe how to calculate values on every level.
    
    For example:
    
    ```
    >>> a = NumpyDict({
    ...    'layer1': np.array([1, 2]),
    ...    'layer2': np.array([4, 5, 6]),
    ... })
    >>> b = NumpyDict({
    ...    'layer1': np.array([0, 9]),
    ...    'layer2': np.array([10, 11, 12]),
    ... })
    >>> a + b
    NumpyDict({
        'layer1': np.array([1, 11]),
        'layer2': np.array([14, 16, 18]),
    })
    ```"""
    def __add__(self, other):
        result = NumpyDict()
        if isinstance(other, (int, float, np.ndarray)):
            for key in self:
                result[key] = self[key] + other
        elif isinstance(other, dict):
            for key in self:
                if key in other:
                    result[key] = self[key] + other[key]
        else:
            raise NotImplementedError("Unsupported type for addition")
        return result

    def __radd__(self, other):
        result = NumpyDict()
        if isinstance(other, (int, float, np.ndarray)):
            for key in self:
                result[key] = other + self[key]
            return result
        elif isinstance(other, dict):
            for key in self:
                if key in other:
                    result[key] = other[key] + self[key]
        else:
            raise NotImplementedError("Unsupported type for addition")
        return result

    def __sub__(self, other):
        result = NumpyDict()
        if isinstance(other, (int, float, np.ndarray)):
            for key in self:
                result[key] = self[key] - other
        elif isinstance(other, dict):
            for key in self:
                if key in other:
                    result[key] = self[key] - other[key]
        else:
            raise NotImplementedError("Unsupported type for subtraction")
        return result

    def __rsub__(self, other):
        result = NumpyDict()
        if isinstance(other, (int, float, np.ndarray)):
            for key in self:
                result[key] = other - self[key]
        elif isinstance(other, dict):
            for key in self:
                if key in other:
                    result[key] = other[key] - self[key]
        else:
            raise NotImplementedError("Unsupported type for subtraction")
        return result

    def __mul__(self, other):
        result = NumpyDict()
        if isinstance(other, (int, float, np.ndarray)):
            for key in self:
                result[key] = self[key] * other
        elif isinstance(other, dict):
            for key in self:
                if key in other:
                    result[key] = self[key] * other[key]
        else:
            raise NotImplementedError("Unsupported type for multiplication")
        return result

    def __rmul__(self, other):
        result = NumpyDict()
        if isinstance(other, (int, float, np.ndarray)):
            for key in self:
                result[key] = other * self[key]
        elif isinstance(other, dict):
            for key in self:
                if key in other:
                    result[key] = other[key] * self[key]
        else:
            raise NotImplementedError("Unsupported type for multiplication")
        return result

    def __truediv__(self, other):
        result = NumpyDict()
        if isinstance(other, (int, float, np.ndarray)):
            for key in self:
                result[key] = self[key] / other
        elif isinstance(other, dict):
            for key in self:
                if key in other:
                    result[key] = self[key] / other[key]
        else:
            raise NotImplementedError("Unsupported type for division")
        return result

    def __rtruediv__(self, other):
        result = NumpyDict()
        if isinstance(other, (int, float, np.ndarray)):
            for key in self:
                result[key] = other / self[key]
        elif isinstance(other, dict):
            for key in self:
                if key in other:
                    result[key] = other[key] / self[key]
        else:
            raise NotImplementedError("Unsupported type for division")
        return result

    def __pow__(self, other):
        result = NumpyDict()
        if isinstance(other, (int, float, np.ndarray)):
            for key in self:
                result[key] = self[key] ** other
        elif isinstance(other, dict):
            for key in self:
                if key in other:
                    result[key] = self[key] ** other[key]
        else:
            raise NotImplementedError("Unsupported type for exponentiation")
        return result

    def __rpow__(self, other):
        result = NumpyDict()
        if isinstance(other, (int, float, np.ndarray)):
            for key in self:
                result[key] = other ** self[key]
        elif isinstance(other, dict):
            for key in self:
                if key in other:
                    result[key] = other[key] ** self[key]
        else:
            raise NotImplementedError("Unsupported type for exponentiation")
        return result

    def __eq__(self, other):
        if not isinstance(other, dict):
            return False
        if set(self.keys()) != set(other.keys()):
            return False
        for key in self:
            if key not in other or not np.array_equal(self[key], other[key]):
                return False
        return True
    
    def sqrt(self):
        result = NumpyDict()
        for key in self:
            result[key] = np.sqrt(self[key])
        return result
    
    def sum(self):
        result = 0
        for key in self:
            if isinstance(self[key], np.ndarray):
                result += np.sum(self[key])
            elif isinstance(self[key], (int, float)):
                result += self[key]
        return result
