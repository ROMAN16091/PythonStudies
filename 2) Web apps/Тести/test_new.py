import hypothesis.strategies as st
from hypothesis import given

def reverse_twice(s):
    return s[::-1][::-1]

@given(st.text())
def test_reverse_twice(s):
    assert reverse_twice(s) == s


@given(st.integers(), st.integers)
def test_add(a,b):
    assert a + b == b + a

