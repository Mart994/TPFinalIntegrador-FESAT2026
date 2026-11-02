import unittest

from utils.calculos import calcular_emisiones_carbono, obtener_metricas_consumo


class TestCalculoEmisiones(unittest.TestCase):

    def test_consumo_nominal_factor_por_defecto(self):
        self.assertAlmostEqual(calcular_emisiones_carbono(100), 40.0)

    def test_consumo_con_factor_personalizado(self):
        self.assertAlmostEqual(calcular_emisiones_carbono(200, factor_emision=0.5), 100.0)

    def test_consumo_con_decimales(self):
        self.assertAlmostEqual(calcular_emisiones_carbono(250.5), 100.2)

    def test_consumo_cero_no_genera_emisiones(self):
        self.assertEqual(calcular_emisiones_carbono(0), 0)

    def test_consumo_negativo_eleva_value_error(self):
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-10)



class TestMetricasConsumo(unittest.TestCase):

    def setUp(self):
        # Norte tiene el registro individual más alto (3000),
        # pero Sur gana por consumo acumulado (4800 vs 4500)
        self.registros = [
            {"planta": "Planta Norte", "consumo_kwh": 1500},
            {"planta": "Planta Sur", "consumo_kwh": 2300},
            {"planta": "Planta Norte", "consumo_kwh": 3000},
            {"planta": "Planta Sur", "consumo_kwh": 2500},
        ]

    def test_planta_mayor_consumo_por_total_acumulado(self):
        resultado = obtener_metricas_consumo(self.registros)
        self.assertEqual(resultado["planta_maxima"], "Planta Sur")
        self.assertEqual(resultado["consumo_maximo"], 4800)

    def test_total_global_de_emisiones(self):
        resultado = obtener_metricas_consumo(self.registros)
        self.assertAlmostEqual(resultado["total_emisiones"], 3720.0)

    def test_acumulado_por_planta(self):
        resultado = obtener_metricas_consumo(self.registros)
        self.assertEqual(resultado["metricas_por_planta"]["Planta Norte"]["consumo_kwh"], 4500)

    def test_registros_vacios(self):
        resultado = obtener_metricas_consumo([])
        self.assertIsNone(resultado["planta_maxima"])
        self.assertEqual(resultado["total_emisiones"], 0)

    def test_consumo_negativo_propaga_value_error(self):
        with self.assertRaises(ValueError):
            obtener_metricas_consumo([{"planta": "Planta Este", "consumo_kwh": -100}])

if __name__ == "__main__":
    unittest.main()