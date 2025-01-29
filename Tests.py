import unittest
import Ncomplejos as nc

class TestNumerosComplejos(unittest.TestCase):
    
    def test_suma(self):
        self.assertEqual(nc.Suma((1, 2), (3, 4)), (4, 6))
        self.assertEqual(nc.Suma((-1, -2), (3, 4)), (2, 2))
        self.assertEqual(nc.Suma((0, 0), (0, 0)), (0, 0))
        self.assertEqual(nc.Suma((2.5, 1.5), (-1.5, -0.5)), (1, 1))

    def test_multiplicacion(self):
        self.assertEqual(nc.multiplicacion((1, 2), (3, 4)), (-5, 10))
        self.assertEqual(nc.multiplicacion((-1, -2), (3, 4)), (5, -10))
        self.assertEqual(nc.multiplicacion((0, 0), (3, 4)), (0, 0))
        self.assertEqual(nc.multiplicacion((1, 1), (1, -1)), (2, 0))

    def test_division(self):
        result = nc.division((1, 2), (3, 4))
        self.assertAlmostEqual(result[0], 0.44, places=2)
        self.assertAlmostEqual(result[1], 0.08, places=2)
        with self.assertRaises(ZeroDivisionError):
            nc.division((1, 2), (0, 0))

    def test_resta(self):
        self.assertEqual(nc.resta((1, 2), (3, 4)), (-2, -2))
        self.assertEqual(nc.resta((-1, -2), (3, 4)), (-4, -6))
        self.assertEqual(nc.resta((5, 5), (5, 5)), (0, 0))
        self.assertEqual(nc.resta((2.5, 1.5), (1.5, 0.5)), (1, 1))

    def test_modulo(self):
        self.assertAlmostEqual(nc.modulo((2, 2)), 2.83, places=2)
        self.assertAlmostEqual(nc.modulo((10, 10)), 14.14, places=2)
        self.assertEqual(nc.modulo((0, 0)), 0)
        self.assertEqual(nc.modulo((1, 0)), 1)

    def test_conjugado(self):
        self.assertEqual(nc.conjugado((1, 5)), (1, -5))
        self.assertEqual(nc.conjugado((4, -9)), (4, 9))
        self.assertEqual(nc.conjugado((0, 0)), (0, 0))
        self.assertEqual(nc.conjugado((3, 0)), (3, 0))

    def test_fase(self):
        pi_medio = nc.Fase((0, 1))
        self.assertAlmostEqual(nc.Fase((5, 5)), 0.79, places=2)
        self.assertAlmostEqual(nc.Fase((0, 8)), pi_medio, places=2)
        self.assertAlmostEqual(nc.Fase((1, 0)), 0, places=2)
        self.assertAlmostEqual(nc.Fase((-1, 0)), nc.Fase((-1, 0)), places=2)
        with self.assertRaises(ZeroDivisionError):
            nc.Fase((0, 0))

    def test_CardToPolar(self):
        result1 = nc.CardToPolar((1, 1))
        self.assertAlmostEqual(result1[0], 1.41, places=2)
        self.assertAlmostEqual(result1[1], 0.79, places=2) 
        result2 = nc.CardToPolar((5, 0))
        self.assertAlmostEqual(result2[0], 5.0, places=2)
        self.assertAlmostEqual(result2[1], 0.0, places=2)
        result3 = nc.CardToPolar((0, 5))
        self.assertAlmostEqual(result3[0], 5.0, places=2)
        self.assertAlmostEqual(result3[1], nc.Fase((0, 1)), places=2)

    def test_PolarToCard(self):
        result2 = nc.PolarToCard([5.0, 0.0])
        self.assertAlmostEqual(result2[0], 5.0, places=2)
        self.assertAlmostEqual(result2[1], 0.0, places=2)
        pi_medio = nc.Fase((0, 1))
        result3 = nc.PolarToCard([5.0, pi_medio])
        self.assertAlmostEqual(result3[0], 0.0, places=2)
        self.assertAlmostEqual(result3[1], 5.0, places=2)

if __name__ == '__main__':
    unittest.main()