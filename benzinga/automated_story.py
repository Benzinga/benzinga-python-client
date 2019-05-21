import benzinga_client
import datetime
from fpdf import FPDF


class Automate:

    def __init__(self, api_token):
        self.token = api_token
        self._template_()

    def __gainers_output__(self, company_name, change_percent, close):
        output = "%s, Inc. shares rose %0.1f percent to close at $%0.2f in pre-market trading."\
                 %(company_name, abs(change_percent), close)
        return output

    def __losers_output__(self, company_name, change_percent, close):
        nonnegated_change = abs(change_percent)
        output = "%s, Inc. shares fell %0.1f percent to close at $%0.2f in pre-market trading."\
                 % (company_name, nonnegated_change, close)
        return output

    def __retrieve__(self):
        initiate = benzinga_client.Benzinga(self.token)
        output = initiate.movers()
        print(output)
        gainers = output["result"]["gainers"]
        losers = output["result"]["losers"]
        gainers_list = []
        for companies in gainers:
            gainers_list.append(self.__gainers_output__(companies["companyName"],
                                                        companies["changePercent"], companies["close"]))
        losers_list = []
        for comp in losers:
            losers_list.append(self.__losers_output__(comp["companyName"],
                                                        comp["changePercent"], comp["close"]))
        total_movement = len(gainers_list) + len(losers_list)
        date = datetime.datetime.strptime(output["result"]["toDate"][0:10], "%Y-%m-%d")
        weekDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        day = weekDays[date.weekday()]
        return gainers_list, losers_list, total_movement, day

    def _template_(self):
        retrieve_call = self.__retrieve__()
        sample_heading = "%s Stocks Moving In %s's Pre-Market Session" % (retrieve_call[2], retrieve_call[3])
        pdf = FPDF(orientation='L', unit='mm', format='A4')
        pdf.add_page()
        pdf.set_font("Arial", size=16, style="B")
        pdf.cell(200, 10, txt=sample_heading, ln=1, align="C")
        pdf.set_font("Arial", size=14, style= "B")
        pdf.cell(200,10, txt = "Gainers", ln=1, align= "C")
        pdf.set_font("Arial", size = 12)
        for object in retrieve_call[0]:
            pdf.cell(200, 10, txt = object, ln=1, align= "C")
        pdf.set_font("Arial", size=14, style="B")
        pdf.cell(200, 10, txt="Losers", ln=1, align="C")
        pdf.set_font("Arial", size=12)
        for obj in retrieve_call[1]:
            pdf.cell(200, 10, txt=obj, ln=1, align="C")
        pdf.output("sampledemo.pdf")









if __name__ == '__main__':
    api_token = "54b595f497164e0499409ca93342e394"
    auto = Automate(api_token)


