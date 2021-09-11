from itertools import islice
from polygon import polygon_vertices, get_polygon_vertices


def float_cmp(a: float, b: float):
    return abs(a - b) <= 0.001


def test_simmetry_even():
    n_vert = 1_000_000
    quarter = n_vert // 4
    megagon = polygon_vertices(n_vert, n_vert)
    m_0 = megagon[0]
    m_middle = megagon[n_vert // 2]
    assert m_0 == (m_middle[0], -m_middle[1])
    m_cw_quart = megagon[n_vert // 4]
    m_ccw_quart = megagon[n_vert // 4 * 3]
    assert m_cw_quart == (-m_ccw_quart[0], m_ccw_quart[1])
    octern = n_vert // 8
    m_oct = (
        megagon[octern],
        megagon[octern + quarter],
        megagon[octern + quarter * 2],
        megagon[octern + quarter * 3],
            )
    assert m_oct[0] == (m_oct[1][0], -m_oct[1][1])
    assert m_oct[0] == (-m_oct[2][0], -m_oct[2][1])
    assert m_oct[0] == (-m_oct[3][0], m_oct[3][1])


def test_simmetry_odd():
    unomilleniagon = polygon_vertices(1001, 1000)
    m_1 = unomilleniagon[1]
    m_1000 = unomilleniagon[1000]
    assert m_1 == (-m_1000[0], m_1000[1])
    m_500 = unomilleniagon[500]
    m_501 = unomilleniagon[501]
    assert m_500 == (-m_501[0], m_501[1])


def test_hexagon():
    expected = [
        (0.0, 3.0),
        (2.598076211353316, 1.5),
        (2.598076211353316, -1.4999999999999996),
        (8.498308346471969e-16, -3.0),
        (-2.5980762113533156, -1.5000000000000009),
        (-2.598076211353317, 1.4999999999999982),
    ]

    hexagon = polygon_vertices(6)

    assert len(hexagon) == len(expected)

    for (x1, y1), (x2, y2) in zip(hexagon, expected):
        assert float_cmp(x1, x2)
        assert float_cmp(y1, y2)


def test_decagon():
    expected = [
        (0.0, 3.0),
        (1.7633557568774194, 2.4270509831248424),
        (2.8531695488854605, 0.9270509831248421),
        (2.8531695488854605, -0.9270509831248421),
        (1.7633557568774194, -2.4270509831248424),
        (1.8369701987210297e-16, -3.0),
        (-1.7633557568774192, -2.4270509831248424),
        (-2.8531695488854605, -0.9270509831248426),
        (-2.853169548885461, 0.9270509831248419),
        (-1.7633557568774196, 2.427050983124842),
    ]

    decagon = polygon_vertices(10)

    assert len(decagon) == len(expected)

    for (x1, y1), (x2, y2) in zip(decagon, expected):
        assert float_cmp(x1, x2)
        assert float_cmp(y1, y2)
