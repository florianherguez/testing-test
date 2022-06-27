# https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Importing%20Notebooks.html
# https://stackoverflow.com/questions/40172281/unit-tests-for-functions-in-a-jupyter-notebook
# https://ipynb.readthedocs.io/en/stable/
# https://docs.python.org/3/library/unittest.html
# https://www.digitalocean.com/community/tutorials/how-to-use-unittest-to-write-a-test-case-for-a-function-in-python
# https://stackoverflow.com/questions/49807449/how-to-check-if-a-function-was-called-in-a-unit-test-using-pytest-mock

from ipynb.fs.defs.test_code import add2
from ipynb.fs.defs.test_code import printGraph

import matplotlib.pyplot as plt
import unittest
from unittest.mock import patch

class TestMethodes(unittest.TestCase):
    def testAdd2With2(self):
        '''Test if the methode add 2 at the initial value which is 2'''
        self.assertEqual(add2(2), 4)

    def testAdd2With10(self):
        '''Test if the methode add 2 at the initial value which is 10'''
        self.assertEqual(add2(10), 12)

    @patch('__main__.plt.plot')
    def testPlot(self, mock):
        '''Test if plot is done'''
        x = [10, 20, 30, 40]
        y = [20, 30, 40, 50]
        printGraph(x, y)
        plt.close('all')
        self.assertTrue(mock.called)

    @patch('__main__.plt.scatter')
    def testScatter(self, mock):
        '''Test if scatter plot isn't done'''
        x = [10, 20, 30, 40]
        y = [20, 30, 40, 50]
        printGraph(x, y)
        plt.close('all')
        self.assertFalse(mock.called)

    @patch('__main__.plt.plot')
    def testPlotAdvanced(self, mock):
        '''Test if plot is done with the apropriate data'''
        # TO DO
        x = [10, 20, 30, 40]
        y = [20, 30, 40, 50]
        printGraph(x, y)
        plt.close('all')
        self.assertTrue(mock.called)
    

if __name__ == '__main__':
    unittest.main(verbosity=2)
