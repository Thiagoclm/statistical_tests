# Class for statistical tests
# TODO:
#[x] one sample test t 
#[x] wilcoxon rank sum test
#[x] paired test t
#[x] unpaired test t
#[x] Welch corrected unpaired test t
#[x] Wilcoxon matched pairs test
#[x] Mann-Whitney
#[x] one-way ANOVA
#[x] Friedman test
#[x] Kruskal-Wallis test

import numpy as np
from scipy import stats

class Stats():
    """
    References:

    https://www.biochemia-medica.com/en/journal/20/1/10.11613/BM.2010.004/fullArticle
    https://www.researchgate.net/publication/256303889_Statistical_guidelines_for_Apis_mellifera_research

    """

    def __init__(self) -> None:
        pass


    def one_samp_ttest(series):
        """
        Performs one sample test t

        Parameters:
            series: array
        Returns:
            statistic: float - t-test
            pvalue: float - p-value associated with the alternative
            df: float - degree of freedom to calculate the t-test 
        """
        return stats.ttest_1samp(series,
                                 popmean=0.5)

    def one_samp_wilcoxon(series):
        """
        Performs Wilcoxon signed-rank test

        Parameters:
            series: array
        Returns:
            statistic: float - Wilcoxon test
            pvalue: float - p-value associated with the alternative
        """
        res = stats.wilcoxon(series)
        return res.statistic, res.pvalue 

    def two_samp_ttest(series_a, series_b):
        """
        Performs t-test on two related series, a and b

        Parameters:
            series_a: array
            series_b: array
        Returns:
            statistic: float - t-test
            pvalue: float - p-value associated with the alternative
            df: float - degree of freedom to calculate the t-test 
        """
        return stats.ttest_rel(series_a, series_b)

    def two_samp_unp_ttest(series_a, series_b):
        """
        Performs t-test for two independent series, a and b

        Parameters:
            series_a: array
            series_b: array   
        Returns:
            statistic: float - t-test
            pvalue: float - p-value associated with the alternative           
        """
        return stats.ttest_ind(series_a, series_b)

    def two_samp_unp_welch(series_a, series_b):
        """
        Performs Welch's t-test for two independent series, a and b

        Parameters:
            series_a: array
            series_b: array   
        Returns:
            statistic: float - t-test
            pvalue: float - p-value associated with the alternative           
        """
        return stats.ttest_ind(series_a, series_b, equal_var=False)

    def two_samp_wilcoxon(series_a, series_b):
        """
        Performs Wilcoxon rank-sum test for two distributions

        Parameters:
            series_a: array
            series_b: array
        Returns:
            statistic: float - Wilcoxon test
            pvalue: float - p-value associated with the alternative
        """
        res = stats.ranksums(x=series_a, y=series_b)
        return res.statistic, res.pvalue 

    def two_samp_mannwhitney(series_a, series_b):
        """
        Performs the Mann-Whitney U rank test for two distributions

        Parameters:
            series_a: array
            series_b: array
        Returns:
            statistic: float - U test
            pvalue: float - p-value associated with the alternative
        """
        res = stats.mannwhitneyu(series_a, series_b)
        return res.statistic, res.pvalue

    def multi_samp_anova(*series):
        """
        Perform one-way ANOVA

        Parameters:
            series: array of multiple series
        Returns:
            statistic: float - Kruskal test
            pvalue: float - p-value associated with the alternative 
        """    
        res = stats.f_oneway(*series)
        return res.statistic, res.pvalue


    def multi_samp_friedman(*series):
        """
        Performs the Friedman test for multiple distributions

        Parameters:
            series: array of multiple series
        Returns:
            statistic: float - Kruskal test
            pvalue: float - p-value associated with the alternative
        """
        res = stats.friedmanchisquare(*series)
        return res.statistic, res.pvalue

    def multi_samp_kruskal(*series):
        """
        Performs the Kruskal-Wallis for multiple independent samples
        
        Parameters:
            series: array of multiple series
        Returns:
            statistic: float - Kruskal test
            pvalue: float - p-value associated with the alternative
        """
        res = stats.kruskal(*series)
        return res.statistic, res.pvalue
#######################################################
