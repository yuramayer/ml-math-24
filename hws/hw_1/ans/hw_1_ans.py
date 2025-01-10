import pandas as pd
import numpy as np

def check_123(your_answer, right_answer):
    assert np.array_equal(your_answer, right_answer) 


def check_4(your_answer, right_answer):
    assert your_answer == right_answer 

ans_1 = np.array([40, 33,  1,  6, 20, 16])
ans_2 = np.array([ 5, 12, 10,  3,  6, 13,  8, 21,  5])
ans_3 = np.array([13, 12, 15, 13, 17,  9, 20, 15, 25])
ans_4 = 1348