import benzinga_client
import datetime
from fpdf import FPDF


class Automate_Movers:

    def __init__(self, api_token, session = None, date_from = None, date_to = None, max_results = None,
                 market_cap_gt = None, close_gt = None, sector = None, marketcap_lt = None):
        self.token = api_token
        self.session = session
        self.date_from = date_from
        self.date_to = date_to
        self.max_results = max_results
        self.market_cap_gt = market_cap_gt
        self.close_gt = close_gt
        self.sector = sector
        self.marketcap_lt = marketcap_lt
        self.initiate = benzinga_client.Benzinga(self.token)
        self.movers_output = self.initiate.movers(session = self.session, date_from = self.date_from, date_to = self.date_to,
                                             max_results = self.max_results, market_cap_gt = self.market_cap_gt,
                                             close_gt = self.close_gt, sector = self.sector,
                                             marketcap_lt = self.marketcap_lt)

        self._template_()

    def __session_type_check__(self):
        session_dict = {"PRE_MARKET": "Pre-Market", "AFTER_MARKET": "After-Market", "REGULAR": "Regular"}
        session_type = session_dict[self.session]
        return session_type

    def __time_range__(self):
        if self.date_from != None and len(self.date_from) <= 3:
            range_dict = {"-1d": "Previous Day", "-1w": "Past Week", "-1y": "Past Year", "YTD": "Year-To-Date"}
            range_type = range_dict[self.date_from]
            return range_type
        else:
            return None

    def __gainers_output__(self, company_name, change_percent, close):
        session = self.__session_type_check__()
        output = "%s, Inc. shares rose %0.1f percent to close at $%0.2f in %s trading."\
                 %(company_name, abs(change_percent), close, session.lower())
        return output

    def __losers_output__(self, company_name, change_percent, close):
        session = self.__session_type_check__()
        nonnegated_change = abs(change_percent)
        output = "%s, Inc. shares fell %0.1f percent to close at $%0.2f in %s trading."\
                 % (company_name, nonnegated_change, close, session.lower())
        return output

    def __marketcap__(self, company_ticker):
        result = self.initiate.share_class(company_tickers=company_ticker)
        cap = int(result["result"][0]["shareClass"]["marketCap"])
        comma_cap = "{:,}".format(cap)
        print(comma_cap)
        output = "The market cap stands at $%s." % (comma_cap)
        return output

    def __rating__(self, company_ticker):
        result = self.initiate.ratings(company_tickers=company_ticker)
        if not result:
            output = "Perhaps, looking into Benzinga's ratings section would be of more assistance."
            return output
        else:
            analyst = result["ratings"][0]["analyst"]
            date = result["ratings"][0]["date"]
            current_rating = result["ratings"][0]["rating_current"]
            price_target = result["ratings"][0]["pt_current"]
            if not price_target:
                output = "According to the most recent rating by %s, on %s, the current rating is at %s." % (analyst, date, current_rating)
            else:
                output = "According to the most recent rating by %s, on %s, the current rating is at %s," \
                         "with a price target of $%s." % (analyst, date, current_rating, price_target)
            return output


    def __retrieve__(self):
        output = self.movers_output
        gainers = output["result"]["gainers"]
        losers = output["result"]["losers"]
        gainers_list = []
        for companies in gainers:
            base_output = self.__gainers_output__(companies["companyName"], companies["changePercent"],
                                                  companies["close"])
            mc_statement = self.__marketcap__(companies["symbol"])
            rating_statement = self.__rating__(companies["symbol"])
            description = "%s %s %s" % (base_output, mc_statement, rating_statement)
            gainers_list.append(description)
        losers_list = []
        for comp in losers:
            base_output_l = self.__losers_output__(comp["companyName"], comp["changePercent"], comp["close"])
            mc_statement_l = self.__marketcap__(comp["symbol"])
            rating_statement_l = self.__rating__(comp["symbol"])
            description_l = "%s %s %s" % (base_output_l, mc_statement_l, rating_statement_l)
            losers_list.append(description_l)
        total_movement = len(gainers_list) + len(losers_list)
        time_check = self.__time_range__()
        if time_check == None:
            date = datetime.datetime.strptime(output["result"]["toDate"][0:10], "%Y-%m-%d")
            weekDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            day = weekDays[date.weekday()]
        else:
            day = time_check
        return gainers_list, losers_list, total_movement, day

    def _template_(self):
        session = self.__session_type_check__()
        retrieve_call = self.__retrieve__()
        sample_heading = "%s %s Stocks Moving In %s's %s Session" % (retrieve_call[2], self.sector.capitalize(),
                                                                             retrieve_call[3], session)
        pdf = FPDF(orientation='L', unit='mm', format='A4')
        pdf.add_page()
        pdf.set_font("Arial", size=16, style="B")
        pdf.cell(200, 10, txt=sample_heading, ln=1, align="C")
        pdf.set_font("Arial", size=14, style= "B")
        pdf.cell(200,10, txt = "Gainers", ln=1, align= "C")
        pdf.set_font("Arial", size = 12)
        for object in retrieve_call[0]:
            pdf.multi_cell(250,10, object)
        pdf.set_font("Arial", size=14, style="B")
        pdf.cell(200, 10, txt="Losers", ln=1, align="C")
        pdf.set_font("Arial", size=12)
        for obj in retrieve_call[1]:
            pdf.multi_cell(250, 10, obj)
        pdf.output("sampledemo.pdf")


class Automated_Ratings:

    def __init__(self, api_token):
        self.token = api_token


if __name__ == '__main__':
    token = "899efcbfda344e089b23589cbddac62b"
    api_key = "22f84f867c5746fd92ef8e13f5835c02"
    newapikey = "54b595f497164e0499409ca93342e394"
    auto = Automate_Movers(token, session= "REGULAR", date_from= "-1y", max_results="30", sector= "technology")


