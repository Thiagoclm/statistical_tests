import numpy as np
from scipy import stats 
from Stats import Stats

rvs = stats.norm.rvs(size=50, random_state=42)
print(np.mean(rvs))
print(Stats.one_samp_ttest(rvs))

# pvalue=1.39-06
# Since the pvalue is lower than 0.01, the null hypothesis is rejected, hence 
# the mean of the population is not 0.5 (confirming the mean calculated before)



