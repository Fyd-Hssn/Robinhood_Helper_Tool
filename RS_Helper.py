import robin_stocks as rs
import pandas as pd
from pathlib import Path
from datetime import date, datetime
import os

from config import config

dir_path = os.path.dirname((os.path.realpath(__file__)))


class rs_helper:
    def __init__(self, config, rs):
        self.username = config["USERNAME"]
        self.password = config["PASSWORD"]
        self.rs = rs

    def login(self):
        self.rs.robinhood.authentication.login(
            username=self.username,
            password=self.password,
            expiresIn=86400,
            by_sms=True,
            store_session=True,
        )

    def get_watchlists(self):
        watchlists = []
        for watchlist in self.rs.robinhood.account.get_all_watchlists()["results"]:
            watchlists.append(watchlist["display_name"])
        return watchlists

    def get_current_stock_price(self, symbol):
        stock_price = "{:.2f}".format(float(rs.robinhood.get_latest_price([symbol])[0]))
        return stock_price

    def export_premium_ratios(self, expiration_date=None):
        data = self.export_options_history()
        symbols = [
            dict["symbol"] for dict in rs.robinhood.account.get_watchlist_by_name("Test")["results"]
        ]
        csv_dict = {}
        symbol_dict = {}
        strike_dict = {}
        ratio_dict = {}
        row_count = 0
        for symbol in symbols:
            current_price = self.get_current_stock_price(symbol)
            options = self.rs.robinhood.options.find_options_by_expiration(
                symbol, expirationDate=expiration_date
            )
            sorted_options = sorted(
                [option for option in options if option["type"] == "call"],
                key=lambda option: float(option["strike_price"]),
                reverse=True,
            )
            for option in sorted_options:
                if "adjusted_mark_price" in list(option.keys()):
                    symbol_dict[(row_count)] = option["chain_symbol"]
                    strike_dict[(row_count)] = "{:0.2f}".format(float(option["strike_price"]))
                    ratio = float(option["adjusted_mark_price"]) / float(current_price)
                    percentage = "{0}%".format("{:0.2f}".format(ratio * 100))
                    ratio_dict[(row_count)] = percentage
            csv_dict["Symbol"] = symbol_dict
            csv_dict["Strike Price"] = strike_dict
            csv_dict["Premium Ratio"] = ratio_dict
        ratio_data = pd.DataFrame.from_dict(csv_dict)
        ratio_data.to_csv(r"Robinhood_Helper_Tool\Options_Ratios.csv", index=False)

    def print_premium_ratios(self, type, watchlist, expiration_date=None):
        symbols = [
            dict["symbol"]
            for dict in rs.robinhood.account.get_watchlist_by_name(watchlist)["results"]
        ]
        premium_ratios = []
        for symbol in symbols:
            symbol_dict = {}
            strike_dict = {}
            ratio_dict = {}
            row_count = 0
            current_price = self.get_current_stock_price(symbol)
            current_price_float = float(current_price)
            options = self.rs.robinhood.options.find_options_by_expiration(
                symbol, expirationDate=expiration_date
            )
            sorted_options = sorted(
                [option for option in options if option["type"] == type],
                key=lambda option: float(option["strike_price"]),
                reverse=False,
            )
            OTM_option = None
            if type == "call":
                for option in sorted_options:
                    if float(option["strike_price"]) > current_price_float:
                        OTM_option = "{:0.2f}".format(float(option["strike_price"]))
                        result = None
                        ticker = option["chain_symbol"]
                        strike_price = "{:0.2f}".format(float(option["strike_price"]))
                        ratio = float(option["adjusted_mark_price"]) / float(current_price)
                        percentage = "{0}%".format("{:0.2f}".format(ratio * 100))

                        result = f"{ticker} | Current Price: {current_price} | OTM Strike: {OTM_option} | Ratio: {percentage}"
                        premium_ratios.append(result)
                        break
            elif type == "put":
                for option in sorted_options[::-1]:
                    if float(option["strike_price"]) < current_price_float:
                        OTM_option = "{:0.2f}".format(float(option["strike_price"]))
                        result = None
                        ticker = option["chain_symbol"]
                        strike_price = "{:0.2f}".format(float(option["strike_price"]))
                        ratio = float(option["adjusted_mark_price"]) / float(current_price)
                        percentage = "{0}%".format("{:0.2f}".format(ratio * 100))

                        result = f"{ticker} | Current Price: {current_price} | OTM Strike: {OTM_option} | Ratio: {percentage}"
                        premium_ratios.append(result)
                        break
        premium_ratio_string = ""
        for ratio in premium_ratios:
            premium_ratio_string += ratio + "\n"
        return premium_ratio_string

    def get_holdings(self):
        return self.rs.robinhood.account.build_holdings()

    def get_earnings_timeline(self, watchlist=None):
        earnings_timeline = {}
        if not watchlist:
            holdings = []
            for ticker in rs.robinhood.account.build_holdings().keys():
                holdings.append(ticker)
            for ticker in holdings:
                for period in rs.robinhood.stocks.get_earnings(ticker):
                    if period["report"]:
                        earnings_date = datetime.strptime(
                            period["report"]["date"], "%Y-%m-%d"
                        ).date()
                        if earnings_date > date.today():
                            earnings_timeline[ticker] = earnings_date
                            break
            sorted_earnings = sorted(earnings_timeline.items(), key=lambda x: x[1])
            earnings_timeline_string = "The upcoming earnings dates for your holdings are:\n"
            for reporting_date in sorted_earnings:
                earnings_timeline_string += (
                    "{0}: {1}".format(reporting_date[0], reporting_date[1])
                ) + "\n"
            return earnings_timeline_string
        else:
            tickers = [
                dict["symbol"]
                for dict in rs.robinhood.account.get_watchlist_by_name(watchlist)["results"]
            ]
            for ticker in tickers:
                for period in rs.robinhood.stocks.get_earnings(ticker):
                    if period["report"]:
                        earnings_date = datetime.strptime(
                            period["report"]["date"], "%Y-%m-%d"
                        ).date()
                        if earnings_date > date.today():
                            earnings_timeline[ticker] = earnings_date
                            break
            sorted_earnings = sorted(earnings_timeline.items(), key=lambda x: x[1])
            earnings_timeline_string = (
                f"The upcoming earnings dates for companies in {watchlist}:\n"
            )
            for reporting_date in sorted_earnings:
                earnings_timeline_string += (
                    "{0}: {1}".format(reporting_date[0], reporting_date[1])
                ) + "\n"
            return earnings_timeline_string

    def export_options_history(self):
        todays_date = str(date.today())
        filename = "OptionOrders_{0}".format(todays_date)
        filename_csv = "{0}.csv".format(filename)
        file_path = "{0}\{1}".format(dir_path, filename_csv)
        current_file = Path(file_path)
        if current_file.is_file():
            pass
        else:
            path_list = Path(dir_path).glob("**/*.csv")
            for path in path_list:
                path_str = str(path)
                if path_str[-14:-4] < str(date.today()):
                    path.unlink()
            rs.robinhood.export_completed_option_orders(dir_path, filename)
        data = pd.read_csv(file_path, header=0)
        return data

    def get_options_returns(self):
        data = self.export_options_history()
        index_counter = []
        premium_total = 0
        for row in data.drop(index=index_counter).index:
            if row in index_counter:
                continue
            if (
                type(data.iloc[row]["opening_strategy"]) == str
                and data.iloc[row]["direction"] == "credit"
            ):
                if data.iloc[row]["opening_strategy"] == "iron_condor":
                    next_row = row + 1
                    next_2_rows = row + 2
                    next_3_rows = row + 3
                    index_counter.extend([row, next_row, next_2_rows, next_3_rows])
                    premium_total += (
                        data.iloc[row]["price"] * data.iloc[row]["processed_quantity"] * 100
                    )
                elif (
                    data.iloc[row]["opening_strategy"] == "short_put_spread"
                    or data.iloc[row]["opening_strategy"] == "short_call_spread"
                ):
                    next_row = row + 1
                    index_counter.extend([row, next_row])
                    premium_total += (
                        data.iloc[row]["price"] * data.iloc[row]["processed_quantity"] * 100
                    )
                else:
                    index_counter.extend([row])
                    premium_total += (
                        data.iloc[row]["price"] * data.iloc[row]["processed_quantity"] * 100
                    )
            elif (
                type(data.iloc[row]["closing_strategy"]) == str
                and data.iloc[row]["direction"] == "debit"
            ):
                if data.iloc[row]["closing_strategy"] == "iron_condor":
                    next_row = row + 1
                    next_2_rows = row + 2
                    next_3_rows = row + 3
                    index_counter.extend([row, next_row, next_2_rows, next_3_rows])
                    premium_total -= (
                        data.iloc[row]["price"] * data.iloc[row]["processed_quantity"] * 100
                    )
                elif (
                    data.iloc[row]["closing_strategy"] == "short_put_spread"
                    or data.iloc[row]["closing_strategy"] == "short_call_spread"
                ):
                    next_row = row + 1
                    index_counter.extend([row, next_row])
                    premium_total -= (
                        data.iloc[row]["price"] * data.iloc[row]["processed_quantity"] * 100
                    )
                else:
                    index_counter.extend([row])
                    premium_total -= (
                        data.iloc[row]["price"] * data.iloc[row]["processed_quantity"] * 100
                    )
            elif (
                type(data.iloc[row]["opening_strategy"]) == str
                and data.iloc[row]["direction"] == "debit"
            ):
                index_counter.extend([row])
                premium_total -= (
                    data.iloc[row]["price"] * data.iloc[row]["processed_quantity"] * 100
                )
            elif (
                type(data.iloc[row]["closing_strategy"]) == str
                and data.iloc[row]["direction"] == "credit"
            ):
                index_counter.extend([row])
                premium_total += (
                    data.iloc[row]["price"] * data.iloc[row]["processed_quantity"] * 100
                )
        return "\nThe total accumulated profit from premiums for your Robinhood account is: \n${0}0".format(
            premium_total
        )

    def get_options_returns_by_strat(self, strat):
        data = self.export_options_history()
        index_counter = []
        premium_total = 0
        for row in data.drop(index=index_counter).index:
            if row in index_counter:
                continue
            if (
                strat == "long_call"
                or strat == "short_call"
                or strat == "long_put"
                or strat == "short_put"
            ):
                if (
                    data.iloc[row]["opening_strategy"] == strat
                    and data.iloc[row]["direction"] == "debit"
                ):
                    premium_total -= (
                        data.iloc[row]["price"] * data.iloc[row]["processed_quantity"] * 100
                    )
                elif (
                    data.iloc[row]["closing_strategy"] == strat
                    and data.iloc[row]["direction"] == "credit"
                ):
                    premium_total += (
                        data.iloc[row]["price"] * data.iloc[row]["processed_quantity"] * 100
                    )
                elif (
                    data.iloc[row]["opening_strategy"] == strat
                    and data.iloc[row]["direction"] == "credit"
                ):
                    premium_total += (
                        data.iloc[row]["price"] * data.iloc[row]["processed_quantity"] * 100
                    )
                elif (
                    data.iloc[row]["closing_strategy"] == strat
                    and data.iloc[row]["direction"] == "debit"
                ):
                    premium_total -= (
                        data.iloc[row]["price"] * data.iloc[row]["processed_quantity"] * 100
                    )
            elif strat == "short_call_spread" or strat == "short_put_spread":
                if (
                    data.iloc[row]["opening_strategy"] == strat
                    and data.iloc[row]["direction"] == "credit"
                ):
                    next_row = row + 1
                    index_counter.extend([row, next_row])
                    premium_total += (
                        data.iloc[row]["price"] * data.iloc[row]["processed_quantity"] * 100
                    )
                elif (
                    data.iloc[row]["closing_strategy"] == strat
                    and data.iloc[row]["direction"] == "debit"
                ):
                    next_row = row + 1
                    index_counter.extend([row, next_row])
                    premium_total -= (
                        data.iloc[row]["price"] * data.iloc[row]["processed_quantity"] * 100
                    )
            elif strat == "iron_condor":
                if (
                    data.iloc[row]["opening_strategy"] == strat
                    and data.iloc[row]["direction"] == "credit"
                ):
                    next_row = row + 1
                    next_2_rows = row + 2
                    next_3_rows = row + 3
                    index_counter.extend([row, next_row, next_2_rows, next_3_rows])
                    premium_total += (
                        data.iloc[row]["price"] * data.iloc[row]["processed_quantity"] * 100
                    )
                elif (
                    data.iloc[row]["closing_strategy"] == strat
                    and data.iloc[row]["direction"] == "debit"
                ):
                    next_row = row + 1
                    next_2_rows = row + 2
                    next_3_rows = row + 3
                    index_counter.extend([row, next_row, next_2_rows, next_3_rows])
                    premium_total -= (
                        data.iloc[row]["price"] * data.iloc[row]["processed_quantity"] * 100
                    )
        strat_revised = strat.replace("_", " ")
        return f"\nYour total accumulated profit from using the {strat_revised} strategy is: \n${premium_total:.2f}\n"

    def get_options_returns_by_ticker(self, ticker, strat=None):
        data = self.export_options_history()
        index_counter = []
        premium_total = 0
        if strat == None:
            for row in data.drop(index=index_counter).index:
                if data.iloc[row]["chain_symbol"] == ticker:
                    if row in index_counter:
                        continue
                    if (
                        type(data.iloc[row]["opening_strategy"]) == str
                        and data.iloc[row]["direction"] == "credit"
                    ):
                        if data.iloc[row]["opening_strategy"] == "iron_condor":
                            next_row = row + 1
                            next_2_rows = row + 2
                            next_3_rows = row + 3
                            index_counter.extend([row, next_row, next_2_rows, next_3_rows])
                            premium_total += (
                                data.iloc[row]["price"] * data.iloc[row]["processed_quantity"] * 100
                            )
                        elif (
                            data.iloc[row]["opening_strategy"] == "short_put_spread"
                            or data.iloc[row]["opening_strategy"] == "short_call_spread"
                        ):
                            next_row = row + 1
                            index_counter.extend([row, next_row])
                            premium_total += (
                                data.iloc[row]["price"] * data.iloc[row]["processed_quantity"] * 100
                            )
                        else:
                            index_counter.extend([row])
                            premium_total += (
                                data.iloc[row]["price"] * data.iloc[row]["processed_quantity"] * 100
                            )
                    elif (
                        type(data.iloc[row]["closing_strategy"]) == str
                        and data.iloc[row]["direction"] == "debit"
                    ):
                        if data.iloc[row]["closing_strategy"] == "iron_condor":
                            next_row = row + 1
                            next_2_rows = row + 2
                            next_3_rows = row + 3
                            index_counter.extend([row, next_row, next_2_rows, next_3_rows])
                            premium_total -= (
                                data.iloc[row]["price"] * data.iloc[row]["processed_quantity"] * 100
                            )
                        elif (
                            data.iloc[row]["closing_strategy"] == "short_put_spread"
                            or data.iloc[row]["closing_strategy"] == "short_call_spread"
                        ):
                            next_row = row + 1
                            index_counter.extend([row, next_row])
                            premium_total -= (
                                data.iloc[row]["price"] * data.iloc[row]["processed_quantity"] * 100
                            )
                        else:
                            index_counter.extend([row])
                            premium_total -= (
                                data.iloc[row]["price"] * data.iloc[row]["processed_quantity"] * 100
                            )
                    elif (
                        type(data.iloc[row]["opening_strategy"]) == str
                        and data.iloc[row]["direction"] == "debit"
                    ):
                        index_counter.extend([row])
                        premium_total -= (
                            data.iloc[row]["price"] * data.iloc[row]["processed_quantity"] * 100
                        )
                    elif (
                        type(data.iloc[row]["closing_strategy"]) == str
                        and data.iloc[row]["direction"] == "credit"
                    ):
                        index_counter.extend([row])
                        premium_total += (
                            data.iloc[row]["price"] * data.iloc[row]["processed_quantity"] * 100
                        )
                else:
                    continue
            # premium_total = round(premium_total, 1)
            return f"\nYour total accumulated profit from premiums for {ticker} is: \n${premium_total:.2f}0"
        elif strat != None:
            for row in data.drop(index=index_counter).index:
                if data.iloc[row]["chain_symbol"] == ticker:
                    if row in index_counter:
                        continue
                    if (
                        strat == "long_call"
                        or strat == "short_call"
                        or strat == "long_put"
                        or strat == "short_put"
                    ):
                        if (
                            data.iloc[row]["opening_strategy"] == strat
                            and data.iloc[row]["direction"] == "debit"
                        ):
                            premium_total -= (
                                data.iloc[row]["price"] * data.iloc[row]["processed_quantity"] * 100
                            )
                        elif (
                            data.iloc[row]["closing_strategy"] == strat
                            and data.iloc[row]["direction"] == "credit"
                        ):
                            premium_total += (
                                data.iloc[row]["price"] * data.iloc[row]["processed_quantity"] * 100
                            )
                        elif (
                            data.iloc[row]["opening_strategy"] == strat
                            and data.iloc[row]["direction"] == "credit"
                        ):
                            premium_total += (
                                data.iloc[row]["price"] * data.iloc[row]["processed_quantity"] * 100
                            )
                        elif (
                            data.iloc[row]["closing_strategy"] == strat
                            and data.iloc[row]["direction"] == "debit"
                        ):
                            premium_total -= (
                                data.iloc[row]["price"] * data.iloc[row]["processed_quantity"] * 100
                            )
                    elif strat == "short_call_spread" or strat == "short_put_spread":
                        if (
                            data.iloc[row]["opening_strategy"] == strat
                            and data.iloc[row]["direction"] == "credit"
                        ):
                            next_row = row + 1
                            index_counter.extend([row, next_row])
                            premium_total += (
                                data.iloc[row]["price"] * data.iloc[row]["processed_quantity"] * 100
                            )
                        elif (
                            data.iloc[row]["closing_strategy"] == strat
                            and data.iloc[row]["direction"] == "debit"
                        ):
                            next_row = row + 1
                            index_counter.extend([row, next_row])
                            premium_total -= (
                                data.iloc[row]["price"] * data.iloc[row]["processed_quantity"] * 100
                            )
                    elif strat == "iron_condor":
                        if (
                            data.iloc[row]["opening_strategy"] == strat
                            and data.iloc[row]["direction"] == "credit"
                        ):
                            next_row = row + 1
                            next_2_rows = row + 2
                            next_3_rows = row + 3
                            index_counter.extend([row, next_row, next_2_rows, next_3_rows])
                            premium_total += (
                                data.iloc[row]["price"] * data.iloc[row]["processed_quantity"] * 100
                            )
                        elif (
                            data.iloc[row]["closing_strategy"] == strat
                            and data.iloc[row]["direction"] == "debit"
                        ):
                            next_row = row + 1
                            next_2_rows = row + 2
                            next_3_rows = row + 3
                            index_counter.extend([row, next_row, next_2_rows, next_3_rows])
                            premium_total -= (
                                data.iloc[row]["price"] * data.iloc[row]["processed_quantity"] * 100
                            )
            strat_revised = strat.replace("_", " ")
            return f"Your total accumulated profit from using the {strat_revised} strategy for {ticker} is: ${premium_total:.2f}"

    def get_port_value(self):
        profile = self.rs.robinhood.account.build_user_profile()
        if profile["extended_hours_equity"]:
            equity = float(profile["extended_hours_equity"])
        else:
            equity = float(profile["equity"])
        equity_string = f'Your total equity is ${"{:.2f}".format(equity)}'
        return equity_string

    def get_underlying_return(self):
        holdings = self.get_holdings()
        total_equity_change = 0
        if not holdings:
            equity_change_string = f'You have nothing in your holdings so your return is currently ${"{:.2f}".format(total_equity_change)}'
        else:
            for symbol in holdings:
                equity_change = float(holdings[symbol]["equity_change"])
                total_equity_change += equity_change
            equity_change_string = (
                f'Your total equity return is ${"{:.2f}".format(total_equity_change)}'
            )
        return equity_change_string

    def equity_change_by_ticker(self, ticker):
        holdings = self.get_holdings()
        if not holdings:
            equity_change_string = (
                f"{ticker} is no longer in your holdings. Your equity change is $0.00"
            )
        else:
            equity_change = float(holdings[ticker]["equity_change"])
            equity_change_string = (
                f'Your equity change for {ticker} is ${"{:.2f}".format(equity_change)}'
            )
        return equity_change_string


# Use to test that rs.login works
# foo = rs_helper(config, rs)
# foo.login()