import numpy as np
from scipy import stats 
from Stats import Stats

rvs = [6, 8, 14, 16, 23, 24, 28, 29, 41, -48, 49, 56, 60, -67, 75]
print(np.median(rvs))
print(Stats.one_samp_wilcoxon(rvs))

# pvalue=0.0990
# Since the pvalue is lower than 0.05, the null hypothesis is rejected, hence 
# there is a difference of values in the sample (confirming the median calculated before)



