from typing import Any
import numpy as np
from dataclasses import dataclass

import pytest

from src.utils.numpy_dict import NumpyDict


nd1 = NumpyDict({
    's': np.array([1, 2, 3]),
    'k': np.array([5, 10]),
    'v': np.array([7, 8, 9, 10]),
})

nd2 = NumpyDict({
    's': np.array([4, 5, 6]),
    'v': np.array([1, 1, 1, 1]),
    'x': np.array([5]),
})

nd3 = NumpyDict({
    'x': np.array([5]),
})


@dataclass
class Data:
    left: NumpyDict | int | float
    right: NumpyDict | int | float
    expected: Any


def test_addition_of_numpy_dicts():
    test_cases: list[Data] = [
        Data(
            left=nd1,
            right=nd2,
            expected=NumpyDict({
                's': np.array([5, 7, 9]),
                'v': np.array([8, 9, 10, 11]),
            }),
        ),
        Data(
            left=nd1,
            right=nd3,
            expected=NumpyDict(),
        ),
        Data(
            left=nd2,
            right=nd3,
            expected=NumpyDict({
                'x': np.array([10])
            })
        ),
        Data(
            left=NumpyDict({
                'a': np.array([1, 2]),
            }),
            right=NumpyDict({
                'a': 5,
            }),
            expected=NumpyDict({
                'a': np.array([1+5, 2+5])
            })
        ),
        Data(
            left=NumpyDict({
                'a': 5,
            }),
            right=NumpyDict({
                'a': np.array([1, 2]),
            }),
            expected=NumpyDict({
                'a': np.array([5+1, 5+2])
            })
        ),
    ]

    for test_case in test_cases:
        actual = test_case.left + test_case.right
        assert actual == test_case.expected


def test_left_addition():
    test_cases: list[Data] = [
        Data(
            left=nd1,
            right=5,
            expected=NumpyDict({
                's': np.array([6, 7, 8]),
                'k': np.array([10, 15]),
                'v': np.array([12, 13, 14, 15]),
            }),
        ),
        Data(
            left=nd2,
            right=5,
            expected=NumpyDict({
                's': np.array([9, 10, 11]),
                'v': np.array([6, 6, 6, 6]),
                'x': np.array([10]),
            }),
        ),
        Data(
            left=nd3,
            right=5,
            expected=NumpyDict({
                'x': np.array([10]),
            })
        ),
    ]

    for test_case in test_cases:
        actual = test_case.left + test_case.right
        assert actual == test_case.expected


def test_right_addition():
    test_cases: list[Data] = [
        Data(
            left=5,
            right=nd1,
            expected=NumpyDict({
                's': np.array([6, 7, 8]),
                'k': np.array([10, 15]),
                'v': np.array([12, 13, 14, 15]),
            }),
        ),
        Data(
            left=5,
            right=nd2,
            expected=NumpyDict({
                's': np.array([9, 10, 11]),
                'v': np.array([6, 6, 6, 6]),
                'x': np.array([10]),
            }),
        ),
        Data(
            left=5,
            right=nd3,
            expected=NumpyDict({
                'x': np.array([10]),
            })
        )
    ]

    for test_case in test_cases:
        actual = test_case.left + test_case.right
        assert actual == test_case.expected


def test_subtraction_of_numpy_dicts():
    test_cases: list[Data] = [
        Data(
            left=nd1,
            right=nd2,
            expected=NumpyDict({
                's': np.array([-3, -3, -3]),
                'v': np.array([6, 7, 8, 9]),
            }),
        ),
        Data(
            left=nd1,
            right=nd3,
            expected=NumpyDict(),
        ),
        Data(
            left=nd2,
            right=nd3,
            expected=NumpyDict({
                'x': np.array([0])
            })
        ),
        Data(
            left=NumpyDict({
                'a': np.array([1, 2]),
            }),
            right=NumpyDict({
                'a': 5,
            }),
            expected=NumpyDict({
                'a': np.array([1-5, 2-5])
            })
        ),
        Data(
            left=NumpyDict({
                'a': 5,
            }),
            right=NumpyDict({
                'a': np.array([1, 2]),
            }),
            expected=NumpyDict({
                'a': np.array([5-1, 5-2])
            })
        ),
    ]

    for test_case in test_cases:
        actual = test_case.left - test_case.right
        assert actual == test_case.expected


def test_left_subtraction():
    test_cases: list[Data] = [
        Data(
            left=nd1,
            right=5,
            expected=NumpyDict({
                's': np.array([-4, -3, -2]),
                'k': np.array([0, 5]),
                'v': np.array([2, 3, 4, 5]),
            }),
        ),
        Data(
            left=nd2,
            right=5,
            expected=NumpyDict({
                's': np.array([-1, 0, 1]),
                'v': np.array([-4, -4, -4, -4]),
                'x': np.array([0]),
            }),
        ),
        Data(
            left=nd3,
            right=5,
            expected=NumpyDict({
                'x': np.array([0]),
            })
        )
    ]

    for test_case in test_cases:
        actual = test_case.left - test_case.right
        assert actual == test_case.expected


def test_right_subtraction():
    test_cases: list[Data] = [
        Data(
            left=5,
            right=nd1,
            expected=NumpyDict({
                's': np.array([4, 3, 2]),
                'k': np.array([0, -5]),
                'v': np.array([-2, -3, -4, -5]),
            }),
        ),
        Data(
            left=5,
            right=nd2,
            expected=NumpyDict({
                's': np.array([1, 0, -1]),
                'v': np.array([4, 4, 4, 4]),
                'x': np.array([0]),
            }),
        ),
        Data(
            left=5,
            right=nd3,
            expected=NumpyDict({
                'x': np.array([0]),
            })
        )
    ]

    for test_case in test_cases:
        actual = test_case.left - test_case.right
        assert actual == test_case.expected


def test_multiplication_of_numpy_dicts():
    test_cases: list[Data] = [
        Data(
            left=nd1,
            right=nd2,
            expected=NumpyDict({
                's': np.array([4, 10, 18]),
                'v': np.array([7, 8, 9, 10]),
            }),
        ),
        Data(
            left=nd1,
            right=nd3,
            expected=NumpyDict(),
        ),
        Data(
            left=nd2,
            right=nd3,
            expected=NumpyDict({
                'x': np.array([25])
            })
        ),
        Data(
            left=NumpyDict({
                'a': np.array([1, 2]),
            }),
            right=NumpyDict({
                'a': 5,
            }),
            expected=NumpyDict({
                'a': np.array([1*5, 2*5])
            })
        ),
        Data(
            left=NumpyDict({
                'a': 5,
            }),
            right=NumpyDict({
                'a': np.array([1, 2]),
            }),
            expected=NumpyDict({
                'a': np.array([5*1, 5*2])
            })
        ),
    ]

    for test_case in test_cases:
        actual = test_case.left * test_case.right
        assert actual == test_case.expected


def test_left_multiplication():
    test_cases: list[Data] = [
        Data(
            left=nd1,
            right=5,
            expected=NumpyDict({
                's': np.array([5, 10, 15]),
                'k': np.array([25, 50]),
                'v': np.array([35, 40, 45, 50]),
            }),
        ),
        Data(
            left=nd2,
            right=5,
            expected=NumpyDict({
                's': np.array([20, 25, 30]),
                'v': np.array([5, 5, 5, 5]),
                'x': np.array([25]),
            }),
        ),
        Data(
            left=nd3,
            right=5,
            expected=NumpyDict({
                'x': np.array([25]),
            })
        )
    ]

    for test_case in test_cases:
        actual = test_case.left * test_case.right
        assert actual == test_case.expected


def test_right_multiplication():
    test_cases: list[Data] = [
        Data(
            left=5,
            right=nd1,
            expected=NumpyDict({
                's': np.array([5, 10, 15]),
                'k': np.array([25, 50]),
                'v': np.array([35, 40, 45, 50]),
            }),
        ),
        Data(
            left=5,
            right=nd2,
            expected=NumpyDict({
                's': np.array([20, 25, 30]),
                'v': np.array([5, 5, 5, 5]),
                'x': np.array([25]),
            }),
        ),
        Data(
            left=5,
            right=nd3,
            expected=NumpyDict({
                'x': np.array([25]),
            })
        )
    ]

    for test_case in test_cases:
        actual = test_case.left * test_case.right
        assert actual == test_case.expected


def test_division_of_numpy_dicts():
    test_cases: list[Data] = [
        Data(
            left=nd1,
            right=nd2,
            expected=NumpyDict({
                's': np.array([1/4, 2/5, 3/6]),
                'v': np.array([7/1, 8/1, 9/1, 10/1]),
            }),
        ),
        Data(
            left=nd1,
            right=nd3,
            expected=NumpyDict(),
        ),
        Data(
            left=nd2,
            right=nd3,
            expected=NumpyDict({
                'x': np.array([5/5])
            })
        ),
        Data(
            left=NumpyDict({
                'a': np.array([1, 2]),
            }),
            right=NumpyDict({
                'a': 5,
            }),
            expected=NumpyDict({
                'a': np.array([1/5, 2/5])
            })
        ),
        Data(
            left=NumpyDict({
                'a': 5,
            }),
            right=NumpyDict({
                'a': np.array([1, 2]),
            }),
            expected=NumpyDict({
                'a': np.array([5/1, 5/2])
            })
        ),
    ]

    for test_case in test_cases:
        actual = test_case.left / test_case.right
        for key, arr in actual.items():
            assert key in test_case.expected
            assert arr == pytest.approx(test_case.expected[key])


def test_left_division():
    test_cases: list[Data] = [
        Data(
            left=nd1,
            right=5,
            expected=NumpyDict({
                's': np.array([1/5, 2/5, 3/5]),
                'k': np.array([5/5, 10/5]),
                'v': np.array([7/5, 8/5, 9/5, 10/5]),
            }),
        ),
        Data(
            left=nd2,
            right=5,
            expected=NumpyDict({
                's': np.array([4/5, 5/5, 6/5]),
                'v': np.array([1/5, 1/5, 1/5, 1/5]),
                'x': np.array([5/5]),
            }),
        ),
        Data(
            left=nd3,
            right=5,
            expected=NumpyDict({
                'x': np.array([5/5]),
            })
        )
    ]

    for test_case in test_cases:
        actual = test_case.left / test_case.right
        for key, arr in actual.items():
            assert key in test_case.expected
            assert arr == pytest.approx(test_case.expected[key])


def test_right_division():
    test_cases: list[Data] = [
        Data(
            left=5,
            right=nd1,
            expected=NumpyDict({
                's': np.array([5/1, 5/2, 5/3]),
                'k': np.array([5/5, 5/10]),
                'v': np.array([5/7, 5/8, 5/9, 5/10]),
            }),
        ),
        Data(
            left=5,
            right=nd2,
            expected=NumpyDict({
                's': np.array([5/4, 5/5, 5/6]),
                'v': np.array([5/1, 5/1, 5/1, 5/1]),
                'x': np.array([5/5]),
            }),
        ),
        Data(
            left=5,
            right=nd3,
            expected=NumpyDict({
                'x': np.array([5/5]),
            })
        )
    ]

    for test_case in test_cases:
        actual = test_case.left / test_case.right
        for key, arr in actual.items():
            assert key in test_case.expected
            assert arr == pytest.approx(test_case.expected[key])


def test_exponentiation_of_numpy_dicts():
    test_cases: list[Data] = [
        Data(
            left=nd1,
            right=nd2,
            expected=NumpyDict({
                's': np.array([1**4, 2**5, 3**6]),
                'v': np.array([7**1, 8**1, 9**1, 10**1]),
            }),
        ),
        Data(
            left=nd1,
            right=nd3,
            expected=NumpyDict(),
        ),
        Data(
            left=nd2,
            right=nd3,
            expected=NumpyDict({
                'x': np.array([5**5])
            })
        ),
        Data(
            left=NumpyDict({
                'a': np.array([1, 2]),
            }),
            right=NumpyDict({
                'a': 5,
            }),
            expected=NumpyDict({
                'a': np.array([1**5, 2**5])
            })
        ),
        Data(
            left=NumpyDict({
                'a': 5,
            }),
            right=NumpyDict({
                'a': np.array([1, 2]),
            }),
            expected=NumpyDict({
                'a': np.array([5**1, 5**2])
            })
        ),
    ]

    for test_case in test_cases:
        actual = test_case.left ** test_case.right
        assert actual == test_case.expected


def test_left_exponentiation():
    test_cases: list[Data] = [
        Data(
            left=nd1,
            right=5,
            expected=NumpyDict({
                's': np.array([1**5, 2**5, 3**5]),
                'k': np.array([5**5, 10**5]),
                'v': np.array([7**5, 8**5, 9**5, 10**5]),
            }),
        ),
        Data(
            left=nd2,
            right=5,
            expected=NumpyDict({
                's': np.array([4**5, 5**5, 6**5]),
                'v': np.array([1**5, 1**5, 1**5, 1**5]),
                'x': np.array([5**5]),
            }),
        ),
        Data(
            left=nd3,
            right=5,
            expected=NumpyDict({
                'x': np.array([5**5]),
            })
        )
    ]

    for test_case in test_cases:
        actual = test_case.left ** test_case.right
        assert actual == test_case.expected


def test_right_exponentiation():
    test_cases: list[Data] = [
        Data(
            left=5,
            right=nd1,
            expected=NumpyDict({
                's': np.array([5**1, 5**2, 5**3]),
                'k': np.array([5**5, 5**10]),
                'v': np.array([5**7, 5**8, 5**9, 5**10]),
            }),
        ),
        Data(
            left=5,
            right=nd2,
            expected=NumpyDict({
                's': np.array([5**4, 5**5, 5**6]),
                'v': np.array([5**1, 5**1, 5**1, 5**1]),
                'x': np.array([5**5]),
            }),
        ),
        Data(
            left=5,
            right=nd3,
            expected=NumpyDict({
                'x': np.array([5**5]),
            })
        )
    ]

    for test_case in test_cases:
        actual = test_case.left ** test_case.right
        assert actual == test_case.expected


def test_complex_case():
    def func(x, y): return 2018 + 2 * x + y ** (x / 2 - 1)

    x = NumpyDict({
        'a': np.array([1, 2]),
        'b': np.array([1, 2, 3]),
    })

    y = NumpyDict({
        'a': np.array([3, 4]),
        'b': np.array([4, 5, 6]),
    })

    actual = func(x, y)
    for key in actual:
        assert func(x[key], y[key]) == pytest.approx(actual[key])


def test_sqrt():
    actual = np.sqrt(nd1)
    expected = nd1 ** 0.5
    for key in actual:
        assert key in expected
        assert actual[key] == pytest.approx(expected[key])


# def test_getitem():
#     d = NumpyDict({

#     })
