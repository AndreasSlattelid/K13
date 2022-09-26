# k13

This is a local package named k13, this is based on the following [document](https://www.finanstilsynet.no/contentassets/fdcb5b465a1a434e9eb9579d33ef03ce/nytt-doedelighetsgrunnlag-i-kollektiv-pensjonsforsikring-k-2013.pdf) from Finanstilsynet. 

It has the following functions included:
* w(x, G): represents the mortality decrease over time, weighted by gender: \
x: age and G: gender
* mu_kol_2013(x, G): represents the mortality rate in 2013.
* mu(u, x, G, Y): represents the "discounted" mortality rate, i.e a 24 year old in 2022, does not have the same mortality as a 24 year old in 2013. It is aslo turned into a function of u, so that one can integrate it. 
* p_surv(x, G, Y, t, s): represents the survival probability, given that they are alive at time x + t for calculation year Y. For integration, scipy.quad is used. 
