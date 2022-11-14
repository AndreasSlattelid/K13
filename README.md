# Overview

k13 is a package, based on the following [document](https://www.finanstilsynet.no/contentassets/fdcb5b465a1a434e9eb9579d33ef03ce/nytt-doedelighetsgrunnlag-i-kollektiv-pensjonsforsikring-k-2013.pdf) from Finanstilsynet. 

## Installation
    pip install git+https://github.com/AndreasSlattelid/k13

##  Features
It has the following functions included:
* w(x, G): represents the mortality decrease over time, weighted by gender: \
x: age and G: gender
* mu_kol_2013(x, G): Mortality rate in 2013.
* mu(u, x, G, Y): The "discounted" mortality rate, i.e a 24 year old in 2022, does not have the same mortality as a 24 year old in 2013. 
* p_surv(x, G, Y, t, s): Probability that the insured will survive until x + s, given that they are alive at x + t and are aged x in calculation year Y. \
Integration method: scipy.quad 