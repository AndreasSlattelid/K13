import numpy as np
from scipy.integrate import quad

genders = ["M", "F"]


def w(x: float, G: str) -> float:
    """
    x: age of insured 
    G: gender of insured 

    Coincides with the weights given by Finanstilsynet
    """
    if x < 0:
        raise ValueError("Please choose age >= 0")

    if G not in genders:
        raise ValueError("Plese choose gender equal to 'M' or 'F'")
    if G == "M":
        return min(2.671548-0.172480*x + 0.001485*x**2, 0)

    return min(1.287968-0.101090*x + 0.000814*x**2, 0)


def mu_kol_2013(x: float, G: str) -> float:
    """
    x: age of insured 
    G: gender of insured 

    coincides with mu.kol.2013 from finanstilsynet
    """

    if G not in genders:
        raise ValueError("Plese choose gender equal to 'M' or 'F'")

    if G == "M":
        return (0.241752+0.004536*10**(0.051*x))/1000
    return (0.085411+0.003114*10**(0.051*x))/1000


def mu(u, x, G, Y: int = 2022) -> float:
    """ 
    represents the "discounted" mortality
    """

    if u < 0:
        raise ValueError("Please choose u >= 0")
    if Y < 2013:
        raise ValueError("Please choose year Y >= 2013")

    return mu_kol_2013(x+u, G)*(1 + w(x+u, G)/100)**(Y+u-2013)


def p_surv(x, G, Y, t, s):
    """
    survival probability from start = t to end = s
    """
    if (t > s or t < 0):
        raise ValueError(
            "t and s must be positve and t must be smaller or equal to s")
    if (t == s):
        return 1

    integral, _ = quad(mu, t, s, args=(x, G, Y))

    return round(np.exp(-integral), 6)


if __name__ == "__main__":
    # 24 year old man in 2022, surviving the next 10 years:
    #print(p_surv(24, "M", 2022, 0, 10))
    print(p_surv(24, 'M', 2022, 10, 11))
