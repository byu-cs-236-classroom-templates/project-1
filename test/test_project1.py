import pytest

from project1.project1 import project1 as compute


def test_given_badinput_when_project0_then_except():
    # givin
    input = 10

    # when
    with pytest.raises(TypeError):
        compute(input)

    # then
    pass


@pytest.mark.parametrize("input", ["who", "do", "you"])
def test_given_goodinput_when_project0_then_match_pattern(input: str):
    # given
    pass

    # when
    answer = compute(input)

    # then
    expected = "Hello World " + input
    assert expected == answer
