import numpy as np
from scipy import stats 
from Stats import Stats

rvs1 = [19, 22, 16, 29, 24]
rvs2 = [20, 11, 17, 12]

print(Stats.two_samp_mannwhitney(rvs1,rvs2))

# pvalue=0.11
# Since the pvalue is greater than 0.05, the null hypothesis is not rejected, hence 
# the two samples are drawn from the same distribution


