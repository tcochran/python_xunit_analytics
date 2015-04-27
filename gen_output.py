import datetime
import xunitparser
import os
import re
from collections import namedtuple
from collections import OrderedDict

PyramidSuite = namedtuple('PyramidSuite', ['name', 'time', 'count'])

class PyramidLayer():

    def __init__(self, suites, name):
        self.suites = suites
        self.name = name

    @property
    def count(self):
        return sum([suite.count for suite in self.suites])

    @property
    def time(self):
        return sum([suite.time for suite in self.suites], datetime.timedelta())


    def __repr__(self):
        return "PyramidLayer name: %s count:%s time:%s" % (self.name, self.count, self.time)

class XUnitReport():

    def __init__(self, path, config):
        self.path = path

    def __get_reports__(self):
        files = [f for f in os.listdir(self.path) if os.path.isfile(os.path.join(self.path,f)) ]
        return [xunitparser.parse(open(self.path + f))[0] for f in files if re.match(".*xml$", f)] 

    def __get_suite_stats__(self, report):
        test_times = [test.time for test in report._tests]
        return PyramidSuite(report.name, sum(test_times, datetime.timedelta()), len(report._tests))

    def gen(self):
        reports = self.__get_reports__()

        layers = OrderedDict([('e2e', PyramidLayer(suites=[], name='e2e')), ('service', PyramidLayer(suites=[], name='service')), ('unit', PyramidLayer(suites=[], name='unit'))])

        for report in reports:
            layers[config[report.name]].suites.append(self.__get_suite_stats__(report))
        return layers

class TextFormatter():


    def __init__(self):
        self.width = 60

    def format(self, layers):

        report = "Testing Pyramid: Num of Tests\n\n"
        layer_format = "{name}: {count} tests in {time}s"
        largest_count = max(layers.values(), key=lambda x: x.count )

        for layer in layers.values():
            layer_width = float(layer.count) / largest_count.count * self.width
            pyramid_layer = "".center(int(layer_width), "*")

            desc = layer_format.format(name = layer.name, 
                count = str(layer.count), 
                time= layer.time.total_seconds())

            report += desc.ljust(30)  
            report += pyramid_layer.center(self.width, " ")
            report += "\n"

        
        return report





# os.system('python run_tests.py')

config = {
    
    'unit_suite': 'unit',
    'e2e_suite': 'e2e',
    'service_suite': 'service'
}

output = XUnitReport('reports/', config).gen()
print TextFormatter().format(output)

