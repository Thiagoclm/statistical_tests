import numpy as np
from scipy import stats 
from Stats import Stats

rvs1 = stats.norm.rvs(loc=5, scale=10, size=500, random_state=42)
rvs2 = stats.norm.rvs(loc=8, scale=20, size=250, random_state=42)
print(np.var(rvs1))
print(np.var(rvs2))
print(Stats.two_samp_unp_welch(rvs1,rvs2))

# pvalue=0.00686
# Since the pvalue is lower than 0.05, the null hypothesis is rejected, hence 
# there is difference between the variances of the samples
# (confirming the variance calculated before)


