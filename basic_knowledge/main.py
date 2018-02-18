
import test
import pkgutil
import unittest
import importlib
import mod1

def run_unit_test():
    suite = unittest.TestSuite()
    for mod in pkgutil.iter_modules(test.__path__):
        testMod= test.__name__+"."+mod[1]
        importMod=importlib.import_module(testMod)
        tester=getattr(importMod,dir(importMod)[1])
        suite.addTests(unittest.TestLoader().loadTestsFromTestCase(tester))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

if __name__ == '__main__':
    run_unit_test()
    