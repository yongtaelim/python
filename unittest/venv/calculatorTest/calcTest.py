import redgreenunittest as unittest
import calculator.calc

class CalculatorTests(unittest.TestCase):
    def setUp(self):
        print 'setup...'
    def tearDown(self):
        print 'tear down...'


    def test_runs(self):
        calcClass = calculator.calc.Calculator()
        self.assertEqual(2, calcClass.add(1,1))

if __name__ == '__main__':
    # all test run
    # unittest.main()
    runner = unittest.TextTestRunner()
    runner.run(unittest.makeSuite(CalculatorTests, 'test'))
