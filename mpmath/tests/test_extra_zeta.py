import pytest

from mpmath import zetazero

@pytest.mark.parametrize("n,v",
    [(399999999, 156762524.6750591511),
     (241389216, 97490234.2276711795),
     (526196239, 202950727.691229534),
     (542964976, 209039046.578535272),
     (1048449112, 388858885.231056486),
     (1048449113, 388858885.384337406),
     (1048449114, 388858886.002285122),
     (1048449115, 388858886.00239369),
     (1048449116, 388858886.690745053),
     # Huge zeros (this may take hours):
#    (8637740722917, 2124447368584.39296466152),
#    (8637740722918, 2124447368584.39298170604),
     ])
def test_zetazero(n, v):
    assert zetazero(n).ae(complex(0.5,v))
