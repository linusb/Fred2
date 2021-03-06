__author__ = 'schubert'
import unittest


from Fred2.Core.Peptide import Peptide
from Fred2.CleavagePrediction import CleavageSitePredictorFactory
from Fred2.EpitopeAssembly.EpitopeAssembly import EpitopeAssembly


class EpitopeAssemblyTestCase(unittest.TestCase):

    def setUp(self):
        self.peptides = [Peptide("KLLPRLPGV"), Peptide("YLYDHLAPM"), Peptide("ALYDVVSTL")]

    def test_simple_assembly(self):
        """
        Simple test if everything works. Solution manually tested for optimality.

        :return:
        """
        pred = CleavageSitePredictorFactory("PCM")
        assembler = EpitopeAssembly(self.peptides, pred, solver="glpk", verbosity=0)
        r = assembler.solve()
        self.assertEqual(r, [Peptide("YLYDHLAPM"), Peptide("ALYDVVSTL"), Peptide("KLLPRLPGV")])