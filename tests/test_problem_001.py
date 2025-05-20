from problems.problem_1._1.py import MultipleSummer

def test_sum_multiples_of_3_and_5():
    summer = MultipleSummer(10, [3, 5])
    assert summer.calculate_sum() == 23

def test_sum_up_to_1000():
    summer = MultipleSummer(1000, [3, 5])
    assert summer.calculate_sum() == 233168  # known correct answer