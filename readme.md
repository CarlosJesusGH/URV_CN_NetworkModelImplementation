# Implementation of models of complex networks.

Implement generators of complex networks for, at least, two of the following models of complex networks (sorted by increasing difficulty), which must include at least one of the two last ones (BA or CM):
    - Erdös-Rényi (ER) networks, either G(N,K) or G(N,p)
    - Watts-Strogatz (WS) small-world model
    - Barabási & Albert (BA) preferential attachment model
    - Configuration Model (CM)
    
## Include the following:
    -Source code in text form
    -Networks generated for the selected models, with different sizes N and for different values of the parameters of the models:
        --ER: different values of "K" for G(N,K), or of "p" for G(N,p), e.g. p=0.00, 0.01, 0.02, 0.03, 0.05, 0.1
        --WS: different values of "p", including p=0, e.g. p=0.0, 0.1, 0.2, 0.5, 0.9, 1.0
        --BA: different values of "m" (number of edges that each new nodes forms with the existing nodes), e.g. m=1, 2, 4, 10
        --CM: different degree distributions: Poisson (ER), e.g. =2, 4; power-law (SF) with different exponents, e.g. gamma=2.2, 2.5, 2.7, 3.0
    -Plots of some of the small size generated networks, e.g. N=50 (ER, WS), N=100 (BA, CM)
    -Plots of the degree distributions, including the theoretical values (corresponding to the selected parameters) and the experimental ones (for the generated network)
    -Estimation of the exponent for the empirical degree distributions of BA and CM (SF)
