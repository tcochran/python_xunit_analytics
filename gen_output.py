from pyra_viz import XUnitReport, TextFormatter

config = {
    'unit_suite': 'unit',
    'e2e_suite': 'e2e',
    'service_suite': 'service'
}

output = XUnitReport('reports/', config).load_pyramid()
print TextFormatter().format(output)