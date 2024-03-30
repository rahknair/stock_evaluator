import sys
import os

wrk_dir = os.path.dirname(__file__)
from utils.common_utils import CommonUtils


class RunTheAnalyzer:
    """
    This class used to run the analyzer and provide output data
    Command format : python3 analyzer.py <stick_name as stock_symbol> <Buying price> <expected price>
    """

    def __init__(self):
        """
        Initializing veriables
        """

        self.stock_name = sys.argv[1]
        self.buy_value = sys.argv[2]
        self.expect_gain = sys.argv[3]
        self.current_value = 0

        self.common_utils = CommonUtils()

    def main(self):
        """
        This function used to run the main loop
        """
        self.current_value = self.common_utils.extract_current_price(self.stock_name)

        if float(self.current_value) >= float(self.expect_gain):
            print("Gain is higher")


if __name__ == '__main__':
    instance = RunTheAnalyzer()
    instance.main()
