import sermacs
import pytest


# use this as object for other tests
@pytest.fixture
def num_list_3():
    return [1,2,3,4]

def test_title_case():
    test_string = 'thIs IS a TesT sTring'
    title_string = sermacs.title_case(test_string)

    assert title_string == 'This Is A Test String'

    return True

@pytest.mark.mytest
def test_type_failure():
    test_input = ['This', 'is']

    with pytest.raises(TypeError):
        sermacs.title_case(test_input)

# skip certain tests. can also have skip if
@pytest.mark.skip
def test_empty_string():
    test_input = ''

    with pytest.raises(IndexError):
        sermacs.title_case(test_input)


# test multiple outputs at once
@pytest.mark.parametrize("num_list, expected_mean", [([1,2,3], 3), ([0,2,3], 3), ([12,3,4], 24)])
def test_many(num_list, expected_mean):
    assert sermacs.mean(num_list) == expected_mean


