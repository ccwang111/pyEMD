"""Tests for checks.py."""
import numpy as np
import unittest
from PyEMD.checks import mean_period
from PyEMD.checks import energy
from PyEMD.checks import significance_apriori
from PyEMD.checks import significance_aposteriori
from PyEMD.checks import whitenoise_check

class TestCase(unittest.TestCase):
    '''Test cases.'''
    def test_mean_period(self):
        '''Test to check if mean period output is correct.'''
        T = np.linspace(0, 2, 100)
        S = np.sin(2*np.pi*T)
        res = mean_period(S)
        self.assertEqual(type(res), float, "Default data type is float")
        self.assertTrue(res > 0, "mean-period cannot be zero")

    def test_mean_period_zero_peaks(self):
        '''Tect to check if mean period function can handle zero peaks.'''
        T = np.linspace(0, 2, 100)
        res = mean_period(T)
        self.assertEqual(res, len(T), "mean-period is same as signal length in case of monotonic curve")

    def test_energy(self):
        '''Test to check if energy of signal is being computed properly.'''
        T = np.linspace(0, 2, 200)
        S = np.sin(2*2*np.pi*T)
        res = energy(S)
        self.assertEqual(type(res), np.float64, "Default data type is float")

    def test_significance_apriori(self):
        '''a priori significance test.'''
        T = np.linspace(0, 2, 200)
        S = np.sin(2*2*np.pi*T)
        energy_density = energy(S)/len(S)
        res = significance_apriori(energy_density, 2, len(S), 0.9)
        self.assertEqual(type(res), bool, "Default data type is bool")

    def test_significance_aposteriori(self):
        '''a posteriori significance test.'''
        T = np.linspace(0, 2, 200)
        S = np.sin(2*2*np.pi*T)
        energy_density = energy(S)/len(S)
        res = significance_aposteriori(energy_density, 2, len(S), 0.9)
        self.assertEqual(type(res), bool, "Default data type is bool")

    def test_whitenoise_check_apriori(self):
        '''a priori whitenoise_check.'''
        T = [np.linspace(0, i, 200) for i in range(5,0,-1)]
        S = np.array([list(np.sin(2*2*np.pi*i)) for i in T])
        res = whitenoise_check(S, test='apriori')
        self.assertEqual(type(res), dict or None, "Default data type is dict")
    
    def test_whitenoise_check_apriori_alpha(self):
        '''a priori whitenoise_check with custom alpha'''
        T = [np.linspace(0, i, 200) for i in range(5,0,-1)]
        S = np.array([list(np.sin(2*2*np.pi*i)) for i in T])
        res = whitenoise_check(S, test='apriori', alpha = 0.99)
        self.assertEqual(type(res), dict or None, "Default data type is dict")

    def test_whitenoise_check_alpha(self):
        '''a posteriori whitenoise check with custom alpha value.'''
        T = [np.linspace(0, i, 200) for i in range(5,0,-1)]
        S = np.array([list(np.sin(2*2*np.pi*i)) for i in T])
        res = whitenoise_check(S, alpha=0.9)
        self.assertEqual(type(res), dict or None, "Default data type is dict")

    def test_whitenoise_check_rescaling_imf(self):
        '''a posteriori whitenoise check with custom rescaling imf.'''
        T = [np.linspace(0, i, 200) for i in range(5,0,-1)]
        S = np.array([list(np.sin(2*2*np.pi*i)) for i in T])
        res = whitenoise_check(S, rescaling_imf=2)
        self.assertEqual(type(res), dict or None, "Default data type is dict")

    def test_whitenoise_check_nan_values(self):
        '''whitenoise check with nan in IMF.'''
        S = np.array([np.full(100, np.NaN) for i in range(5,0,-1)])
        res = whitenoise_check(S)
        self.assertEqual(res, None, "Input NaN return None")


if __name__ == "__main__":
    unittest.main()
