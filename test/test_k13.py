import pytest
import k13
from contextlib import nullcontext as does_not_raise


@pytest.mark.parametrize("gender, raises", [("K", pytest.raises(ValueError)), ("F", does_not_raise()), ("m", pytest.raises(ValueError))])
def test_w_gender(gender, raises):
    with raises:
        k13.w(x=24, G=gender)


def test_w_invalid_age_input():
    with pytest.raises(ValueError):
        k13.w(x=-2, G="M")


def test_mu_invalid_year_input():
    with pytest.raises(ValueError):
        k13.mu(20, 24, G="M", Y=2011)


def test_mu_invalid_u_input():
    with pytest.raises(ValueError):
        k13.mu(u=-2, x=24, G="M", Y=2022)


@pytest.mark.parametrize("t,s,expected", [(0, 0, 1), (10, 10, 1), (2, 2, 1)])
def test_immidiate_survival(t, s, expected):
    calculated = k13.p_surv(x=24, G="M", Y=2022, t=t, s=s)

    assert calculated == expected


@pytest.mark.parametrize("year, raises", [(2012, pytest.raises(ValueError)), (2013, does_not_raise()), (2014, does_not_raise())])
def test_p_surv_year_input(year, raises):
    with raises:
        k13.p_surv(x=24, G="M", Y=year, t=0, s=10)
