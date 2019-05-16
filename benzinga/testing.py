import unittest
import client


class Benzinga_Testing(unittest.TestCase):

    token = "899efcbfda344e089b23589cbddac62b"
    sn = client.Benzinga(token)
    company_ticker = "AAPL"
    end_point_list = [sn.dividends(), sn.earnings(), sn.splits(), sn.economics(), sn.guidance(), sn.ipo()\
                      , sn.ratings(), sn.economics(), sn.conference_calls(), sn.financials(), sn.valuation_ratios()\
                      ,sn.operation_ratios(company_ticker), sn.operation_ratios(company_ticker)]

    def test_json(self):
        for endpoint in self.end_point_list:
            self.assertEqual(type(endpoint), type({}), "Some Error: Returned object not a dict")


if __name__ == "__main__":
    unittest.main()


