import robin_stocks as rs
from tkinter import *
from RS_Helper import rs_helper
from config import config


def main():
    acc = rs_helper(config, rs)
    acc.login()
    return acc


def export_returns(entry):
    entry.delete(0, "end")
    output = main().export_options_history()
    entry.insert(0, "Exported!")


def options_returns(entry, strat=None):
    entry.delete(0, "end")
    if strat != None:
        output = main().get_options_returns_by_strat(strat)
        entry.insert(0, output)
    else:
        output = main().get_options_returns()
        entry.insert(0, output)


def ticker_label(entry, ticker_entry):
    ticker = ticker_entry.get()
    if len(ticker) > 4 or len(ticker) == 0:
        ticker_entry.delete(0, "end")
        ticker_entry.insert(0, "You forgot to enter a Ticker Symbol! Please type it with ALL CAPS!")
    else:
        entry.delete(20, "end")
        entry.insert(20, ticker)


def ticker_option_returns(entry, ticker_entry, strat=None, menu=None):
    parent_name = str(entry.winfo_parent())
    if parent_name != ".!frame4":
        entry.delete(0, "end")
        ticker = ticker_entry.get()
        if len(ticker) > 4 or len(ticker) == 0:
            entry.insert(0, "Enter a Ticker Symbol first!")
        else:
            output = main().get_options_returns_by_ticker(ticker, strat)
            entry.insert(0, output)
    else:
        entry.delete(0, "end")
        ticker = ticker_entry.get()
        if not ticker:
            entry.insert(0, "Enter a Ticker Symbol first!")
        else:
            strategy = menu.get()
            if strategy != "All Strategies":
                strategy_rs = strategy.lower().replace(" ", "_")
                output = main().get_options_returns_by_ticker(ticker, strategy_rs)
                entry.insert(0, output)
            else:
                output = main().get_options_returns_by_ticker(ticker, strat)
                entry.insert(0, output)


def print_equity(entry):
    entry.delete(0, "end")
    output = main().get_port_value()
    entry.insert(0, output)


def print_equity_change(entry):
    entry.delete(0, "end")
    output = main().get_underlying_return()
    entry.insert(0, output)


def print_ticker_equity_change(entry, ticker_entry):
    entry.delete(0, "end")
    if not ticker_entry.get():
        entry.insert(0, "Enter a Ticker Symbol first!")
    else:
        ticker = ticker_entry.get()
        output = main().equity_change_by_ticker(ticker)
        entry.insert(0, output)


def print_breakeven_equity(entry):
    entry.delete(0, "end")
    underlying_index_pointer = main().get_underlying_return().index("$") + 1
    port_index_pointer = main().get_port_value().index("$") + 1
    if float(main().get_underlying_return()[underlying_index_pointer:]) < 0:
        output = abs(float(main().get_underlying_return()[underlying_index_pointer:])) + float(
            main().get_port_value()[port_index_pointer:]
        )
        output_string = f'Your break-even equity value is ${"{:.2f}".format(output)}'
        entry.insert(0, output_string)
    elif float(main().get_underlying_return()[underlying_index_pointer:]) > 0:
        output = float(main().get_port_value()[port_index_pointer:]) - abs(
            float(main().get_underlying_return()[underlying_index_pointer:])
        )
        output_string = f'You are over your break-even! Your break-even equity value was ${"{:.2f}".format(output)}'
        entry.insert(0, output_string)


def print_combined_ticker_return(entry, ticker_entry, equity_change_result, options_return_result):
    entry.delete(0, "end")
    ticker = ticker_entry.get()
    if not ticker:
        entry.insert(0, "You forgot to enter a ticker symbol!")
    else:
        equity_index_pointer = equity_change_result.get().index("$") + 1
        options_index_pointer = options_return_result.get().index("$") + 1
        equity_change = float(equity_change_result.get()[equity_index_pointer:])
        options_return = float(options_return_result.get()[options_index_pointer:])
        total = "{:.2f}".format(options_return + equity_change)
        output = f"Your combined return from options and equity for {ticker} is ${total}"
        entry.insert(0, output)


def print_ratios(menu, date, widget):
    parent_name = str(widget.winfo_parent())
    widget.delete("1.0", "end")
    exp_date = date.get()
    watchlist = menu.get()
    if not watchlist or not date:
        widget.insert("1.0", "You forgot to select a watchlist AND enter a date!")
    elif parent_name == ".!frame5":
        output = main().print_premium_ratios("call", watchlist, exp_date)
        widget.insert("1.0", output)
    elif parent_name == ".!frame6":
        output = main().print_premium_ratios("put", watchlist, exp_date)
        widget.insert("1.0", output)


def print_earnings(widget, menu=None):
    parent_name = str(widget.winfo_parent())
    if parent_name != ".!frame8":
        widget.delete("1.0", "end")
        output = main().get_earnings_timeline()
        widget.insert("1.0", output)
    else:
        widget.delete("1.0", "end")
        watchlist = menu.get()
        if not watchlist:
            widget.insert("1.0", "Select a Watchlist first!")
        else:
            output = main().get_earnings_timeline(watchlist)
            widget.insert("1.0", output)


def raise_frame(frame):
    frame.tkraise()
