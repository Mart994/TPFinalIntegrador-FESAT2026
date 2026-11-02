from unittest.mock import patch

from django.test import TestCase
from django.urls import reverse

REGISTROS_PRUEBA = [
    {"planta": "Planta Norte", "consumo_kwh": 1500},
    {"planta": "Planta Sur", "consumo_kwh": 2300},
    {"planta": "Planta Norte", "consumo_kwh": 3000},
    {"planta": "Planta Sur", "consumo_kwh": 2500},
]


class TestVistaPanelSustentabilidad(TestCase):

    def setUp(self):
        parche = patch("sustentabilidad.views.registros", REGISTROS_PRUEBA)
        parche.start()
        self.addCleanup(parche.stop)
        self.respuesta = self.client.get(reverse("panel_sustentabilidad"))

    def test_responde_ok(self):
        self.assertEqual(self.respuesta.status_code, 200)

    def test_usa_plantilla_del_panel(self):
        self.assertTemplateUsed(self.respuesta, "sustentabilidad/panel.html")

    def test_contexto_contiene_metricas_calculadas(self):
        metricas = self.respuesta.context["metricas"]
        self.assertEqual(metricas["planta_maxima"], "Planta Sur")
        self.assertAlmostEqual(metricas["total_emisiones"], 3720.0)

    def test_html_muestra_resumen_y_detalle(self):
        self.assertContains(self.respuesta, "3720.00")
        self.assertContains(self.respuesta, "Planta Norte")
        self.assertContains(self.respuesta, "4500")