from dataclasses import dataclass

from src.utils.format import format_significant


@dataclass
class Data:
    value: int | float
    expected: str


def test_significant():
    test_data = [
        Data(2.235435, '2.235'),
        Data(2.235635, '2.236'),
        Data(2.23, '2.230'),
        Data(2, '2.000'),
        Data(2.0, '2.000'),
        Data(23.5465, '23.55'),
        Data(23.5445, '23.54'),
        Data(2324.4654, '2324'),
        Data(2324, '2324'),
        Data(2324.1, '2324'),
        Data(2324.0, '2324'),
        Data(2324.0, '2324'),
        Data(2324546543.546, '2324546544'),
        Data(2324546543, '2324546543'),
        Data(2324546543.0, '2324546543'),
        Data(2324546546546546546543, '2324546546546546546543'),
        Data(0.1, '0.100'),
        Data(0.001, '0.001'),
        Data(0.000001, '0.000001'),
        Data(0.00000126546, '0.000001'),
        Data(0.00000166576, '0.000002'),
        Data(0.000000023132, '2E-8'),
        Data(0, '0.000'),
        Data(0.0, '0.000'),
    ]

    for test_case in test_data:
        assert test_case.expected == format_significant(test_case.value)
        if test_case.value != 0:
            assert f'-{test_case.expected}' == format_significant(-test_case.value)
