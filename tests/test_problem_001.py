from problems.problem_1._1 import MultipleSummer
import pytest

@pytest.mark.parametrize(
    "limit, multiples, expected_sum",
    [
        (10, [3, 5], 23),        # 3,5,6,9 sum to 23
        (15, [3, 5], 45),        # 3,5,6,9,10,12
        (1,  [3, 5], 0),         # no multiples below 1
        (16, [3, 5], 60),        # same as 15, but with 15 includer
        (20, [3, 5], 78),        # 3,5,6,9,10,12,15,18 sum to 78
    ]
)
def test_multiple_sums(limit, multiples, expected_sum):
    summer = MultipleSummer(limit, multiples)
    assert summer.calculate_sum() == expected_sum