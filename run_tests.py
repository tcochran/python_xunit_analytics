import os

os.system('nosetests tests/unit/ --xunit-testsuite-name=unit --with-xunit --xunit-file=reports/unit_report.xml')
os.system('nosetests tests/service/ --xunit-testsuite-name=service --with-xunit --xunit-file=reports/service.xml')
os.system('nosetests tests/e2e/ --xunit-testsuite-name=e2e --with-xunit --xunit-file=reports/e2e.xml')

