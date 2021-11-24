import numpy as np
import unittest
from PyEMD.significancetest import normalize
from PyEMD.significancetest import sign_change
from PyEMD.significancetest import mean_period
from PyEMD.significancetest import energy
from PyEMD.significancetest import significance_aposteriori
from PyEMD.significancetest import significance_apriori

class TestCase(unittest.TestCase):
    def test_normalize(self):
        T = np.linspace(0, 1, 100)
        norm = normalize(T)
        self.assertEqual(len(T), len(norm), "Lengths must be equal")

    def test_sign_change(self):
        T = np.linspace(0, 2, 200)
        S = np.sin(2*2*np.pi*T)
        res = sign_change(normalize(S))
        self.assertEqual(res.dtype, int, "Default data type is int")

    def test_mean_period(self):
        T = np.linspace(0, 2, 200)
        S = np.sin(2*2*np.pi*T)
        res = mean_period(S)
        self.assertEqual(res.dtype, float, "Default data type is float")

    def test_energy(self):
        T = np.linspace(0, 2, 200)
        S = np.sin(2*2*np.pi*T)
        res = energy(S)
        self.assertEqual(res.dtype, float, "Default data type is float")

    def test_significance_apriori(self):
        T = np.linspace(0, 2, 200)
        S = np.sin(2*2*np.pi*T)
        res = significance_apriori(S)
        self.assertEqual(res.dtype, bool, "Default data type is bool")

    def test_significance_aposteriori(self):
        T = np.linspace(0, 2, 200)
        S = np.sin(2*2*np.pi*T)
        res = significance_aposteriori(S)
        self.assertEqual(res.dtype, bool, "Default data type is bool")

if __name__ == "__main__":
    unittest.main()
