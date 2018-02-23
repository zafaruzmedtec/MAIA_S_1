from compute import divide
from compute import multiply

@pytest.mark.parametrize(
    'a, b, x',
    [(1, 2, 0.5),
    (4, 2, 2,)]
)

def test_divide():
    x = divide(1, 2)
    assert x == 0.5

def test_multiply():
    x = divide(2, 2)
    assert x == 4
