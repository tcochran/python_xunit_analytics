from pyra_viz import XUnitReport
from nose.tools import *
from datetime import timedelta

class TestXunitReport():

	def test_loads_pyramid_layers(self):

		pyramid_layers = XUnitReport('reports/', {'e2e_suite': 'e2e', 'service_suite': 'service', 'unit_suite': 'unit'}).load_pyramid()
		e2e_layer = pyramid_layers['e2e']

		assert_equals(['e2e', 'service', 'unit'], [l.name for l in pyramid_layers.values()])

	def test_loads_pyramid_layer_with_suites(self):

		pyramid_layers = XUnitReport('reports/', {'e2e_suite': 'e2e', 'service_suite': 'service', 'unit_suite': 'unit'}).load_pyramid()
		e2e_layer = pyramid_layers['e2e']

		assert_equals(e2e_layer.name, 'e2e')
		assert_equals(e2e_layer.count, 3)		

