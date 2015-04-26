import xunitparser
import os
import re


class XUnitReport():

    def __init__(self, path):
        self.path = path

    def __get_reports__(self):
        files = [f for f in os.listdir(self.path) if os.path.isfile(os.path.join(self.path,f)) ]
        return [xunitparser.parse(open(self.path + f))[0] for f in files if re.match(".*xml$", f)] 

    def gen(self):
        return self.__get_reports__()


print XUnitReport('reports/').gen()
