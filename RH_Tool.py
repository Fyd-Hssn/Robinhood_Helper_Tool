from app_functions import *
from tkinter import *
from tkinter import ttk as ttk
import os

dir_path = os.path.dirname((os.path.realpath(__file__)))

root = Tk()
root.resizable(width=False, height=False)
root.iconbitmap(f"{dir_path}\Robinhood_Logo.ico")
root.title("Robinhood Helper Tool")

main_frame = Frame(root, bg="LightSteelBlue4")
option_frame = Frame(root, bg="LightSteelBlue4")
ticker_option_frame = Frame(root, bg="LightSteelBlue4")
underlying_frame = Frame(root, bg="LightSteelBlue4")
call_ratios_frame = Frame(root, bg="LightSteelBlue4")
put_ratios_frame = Frame(root, bg="LightSteelBlue4")
port_earnings_frame = Frame(root, bg="LightSteelBlue4")
list_earnings_frame = Frame(root, bg="LightSteelBlue4")

frame_list = [
    main_frame,
    option_frame,
    ticker_option_frame,
    underlying_frame,
    call_ratios_frame,
    put_ratios_frame,
    port_earnings_frame,
    list_earnings_frame,
]

for frame in frame_list:
    frame.grid(row=0, column=0, sticky="news")

# Main Page
options_button = Button(
    main_frame,
    text="Options Returns Tracker",
    command=lambda: raise_frame(option_frame),
    width=20,
    bg="lime green",
)
ticker_options_button = Button(
    main_frame,
    text="Option Returns By Ticker",
    command=lambda: raise_frame(ticker_option_frame),
    width=20,
    bg="lime green",
)
underlying_button = Button(
    main_frame,
    text="Underlying Asset Return",
    command=lambda: raise_frame(underlying_frame),
    width=20,
    bg="lime green",
)
call_ratios_button = Button(
    main_frame,
    text="Call Premium Ratios",
    command=lambda: raise_frame(call_ratios_frame),
    width=20,
    bg="lime green",
)
put_ratios_button = Button(
    main_frame,
    text="Put Premium Ratios",
    command=lambda: raise_frame(put_ratios_frame),
    width=20,
    bg="lime green",
)
port_earnings_button = Button(
    main_frame,
    text="Portfolio Earnings Dates",
    command=lambda: raise_frame(port_earnings_frame),
    width=20,
    bg="lime green",
)
list_earnings_button = Button(
    main_frame,
    text="Watchlist Earnings Dates",
    command=lambda: raise_frame(list_earnings_frame),
    width=20,
    bg="lime green",
)

main_label = Label(
    main_frame,
    text="Robinhood Helper Tool",
    width=50,
    bg="LightSteelBlue4",
    fg="white",
)
main_buffer = Label(main_frame, bg="LightSteelBlue4")

main_label.config(font=("Courier", 20))

main_label.grid(row=0, column=1)
main_buffer.grid(row=1, column=1)
options_button.grid(row=3, column=1)
ticker_options_button.grid(row=4, column=1)
underlying_button.grid(row=5, column=1)
call_ratios_button.grid(row=6, column=1)
put_ratios_button.grid(row=7, column=1)
port_earnings_button.grid(row=8, column=1)
list_earnings_button.grid(row=9, column=1)

# Options Page
options_export_button = Button(
    option_frame,
    text="Export Options",
    command=lambda: export_returns(export_result),
    bg="DodgerBlue3",
    fg="white",
    width=20,
)
options_short_call_button = Button(
    option_frame,
    text="Short Calls",
    command=lambda: options_returns(options_short_call_result, "short_call"),
    bg="SeaGreen3",
    width=20,
)
options_long_call_button = Button(
    option_frame,
    text="Long Calls",
    command=lambda: options_returns(options_long_call_result, "long_call"),
    bg="SeaGreen3",
    width=20,
)
options_short_put_button = Button(
    option_frame,
    text="Short Puts",
    command=lambda: options_returns(options_short_put_result, "short_put"),
    bg="SeaGreen3",
    width=20,
)
options_long_put_button = Button(
    option_frame,
    text="Long Puts",
    command=lambda: options_returns(options_long_put_result, "long_put"),
    bg="SeaGreen3",
    width=20,
)
options_short_call_spread_button = Button(
    option_frame,
    text="Short Call Spreads",
    command=lambda: options_returns(options_short_call_spread_result, "short_call_spread"),
    bg="SeaGreen3",
    width=20,
)
options_short_put_spread_button = Button(
    option_frame,
    text="Short Put Spreads",
    command=lambda: options_returns(options_short_put_spread_result, "short_put_spread"),
    bg="SeaGreen3",
    width=20,
)
options_iron_condor_button = Button(
    option_frame,
    text="Iron Condors",
    command=lambda: options_returns(options_iron_condor_result, "iron_condor"),
    bg="SeaGreen3",
    width=20,
)
options_total_button = Button(
    option_frame,
    text="Total Returns",
    command=lambda: options_returns(options_total_result),
    bg="SeaGreen3",
    width=20,
)
options_back_button = Button(
    option_frame,
    text="BACK",
    command=lambda: raise_frame(main_frame),
    width=20,
    bg="indian red",
    fg="white",
)

options_buffer_label = Label(
    option_frame,
    text="Options Returns",
    font=("Helvetica", 9, "bold"),
    bg="LightSteelBlue4",
    fg="white",
)

export_result = Entry(option_frame, width=112)
export_result.insert(0, "This may take a while if not already exported!")
options_short_call_result = Entry(option_frame, width=112)
options_long_call_result = Entry(option_frame, width=112)
options_short_put_result = Entry(option_frame, width=112)
options_long_put_result = Entry(option_frame, width=112)
options_short_call_spread_result = Entry(option_frame, width=112)
options_short_put_spread_result = Entry(option_frame, width=112)
options_iron_condor_result = Entry(option_frame, width=112)
options_total_result = Entry(option_frame, width=112)

options_export_button.grid(row=0)
options_buffer_label.grid(row=1, columnspan=2)
options_short_call_button.grid(row=2)
options_long_call_button.grid(row=3)
options_short_put_button.grid(row=4)
options_long_put_button.grid(row=5)
options_short_call_spread_button.grid(row=6)
options_short_put_spread_button.grid(row=7)
options_iron_condor_button.grid(row=8)
options_total_button.grid(row=9)
options_back_button.grid(row=11, columnspan=2)
export_result.grid(row=0, column=1)
options_short_call_result.grid(row=2, column=1)
options_long_call_result.grid(row=3, column=1)
options_short_put_result.grid(row=4, column=1)
options_long_put_result.grid(row=5, column=1)
options_short_call_spread_result.grid(row=6, column=1)
options_short_put_spread_result.grid(row=7, column=1)
options_iron_condor_result.grid(row=8, column=1)
options_total_result.grid(row=9, column=1)

# Ticker Options Page
ticker_button = Button(
    ticker_option_frame,
    text="Submit Ticker Symbol",
    command=lambda: ticker_label(buffer_entry, ticker_result),
    bg="DodgerBlue3",
    fg="white",
    width=20,
)
ticker_options_short_call_button = Button(
    ticker_option_frame,
    text="Short Calls",
    command=lambda: ticker_option_returns(ticker_short_call_result, ticker_result, "short_call"),
    bg="SeaGreen3",
    width=20,
)
ticker_long_call_button = Button(
    ticker_option_frame,
    text="Long Calls",
    command=lambda: ticker_option_returns(ticker_long_call_result, ticker_result, "long_call"),
    bg="SeaGreen3",
    width=20,
)
ticker_short_put_button = Button(
    ticker_option_frame,
    text="Short Puts",
    command=lambda: ticker_option_returns(ticker_short_put_result, ticker_result, "short_put"),
    bg="SeaGreen3",
    width=20,
)
ticker_long_put_button = Button(
    ticker_option_frame,
    text="Long Puts",
    command=lambda: ticker_option_returns(ticker_long_put_result, ticker_result, "long_put"),
    bg="SeaGreen3",
    width=20,
)
ticker_short_call_spread_button = Button(
    ticker_option_frame,
    text="Short Call Spreads",
    command=lambda: ticker_option_returns(
        ticker_short_call_spread_result, ticker_result, "short_call_spread"
    ),
    bg="SeaGreen3",
    width=20,
)
ticker_short_put_spread_button = Button(
    ticker_option_frame,
    text="Short Put Spreads",
    command=lambda: ticker_option_returns(
        ticker_short_put_spread_result, ticker_result, "short_put_spread"
    ),
    bg="SeaGreen3",
    width=20,
)
ticker_iron_condor_button = Button(
    ticker_option_frame,
    text="Iron Condors",
    command=lambda: ticker_option_returns(ticker_iron_condor_result, ticker_result, "iron_condor"),
    bg="SeaGreen3",
    width=20,
)
ticker_total_button = Button(
    ticker_option_frame,
    text="Total Returns",
    command=lambda: ticker_option_returns(ticker_total_result, ticker_result),
    bg="SeaGreen3",
    width=20,
)
ticker_back_button = Button(
    ticker_option_frame,
    text="BACK",
    command=lambda: raise_frame(main_frame),
    width=20,
    bg="indian red",
    fg="white",
)

ticker_result = Entry(ticker_option_frame, width=112)
buffer_entry = Entry(
    ticker_option_frame,
    width=25,
    font=("Helvetica", 9, "bold"),
    bg="LightSteelBlue4",
    fg="white",
    justify=CENTER,
    relief=FLAT,
)

ticker_result.insert(
    0,
    "Delete this line and type the ticker symbol (ALL CAPS). Click 'Submit Ticker Symbol'",
)
buffer_entry.insert(0, "Options Returns for ")

ticker_short_call_result = Entry(ticker_option_frame, width=112)
ticker_long_call_result = Entry(ticker_option_frame, width=112)
ticker_short_put_result = Entry(ticker_option_frame, width=112)
ticker_long_put_result = Entry(ticker_option_frame, width=112)
ticker_short_call_spread_result = Entry(ticker_option_frame, width=112)
ticker_short_put_spread_result = Entry(ticker_option_frame, width=112)
ticker_iron_condor_result = Entry(ticker_option_frame, width=112)
ticker_total_result = Entry(ticker_option_frame, width=112)

ticker_button.grid(row=0)
ticker_options_short_call_button.grid(row=2)
ticker_long_call_button.grid(row=3)
ticker_short_put_button.grid(row=4)
ticker_long_put_button.grid(row=5)
ticker_short_call_spread_button.grid(row=6)
ticker_short_put_spread_button.grid(row=7)
ticker_iron_condor_button.grid(row=8)
ticker_total_button.grid(row=9)
ticker_back_button.grid(row=11, columnspan=2)
ticker_result.grid(row=0, column=1)
buffer_entry.grid(row=1, columnspan=2)
ticker_short_call_result.grid(row=2, column=1)
ticker_long_call_result.grid(row=3, column=1)
ticker_short_put_result.grid(row=4, column=1)
ticker_long_put_result.grid(row=5, column=1)
ticker_short_call_spread_result.grid(row=6, column=1)
ticker_short_put_spread_result.grid(row=7, column=1)
ticker_iron_condor_result.grid(row=8, column=1)
ticker_total_result.grid(row=9, column=1)

# Underlying Asset Return Page
underlying_equity_button = Button(
    underlying_frame,
    text="Current Equity Value",
    command=lambda: print_equity(underlying_equity_result),
    bg="DodgerBlue3",
    fg="white",
    width=20,
)

underlying_breakeven_equity_button = Button(
    underlying_frame,
    text="Break-Even Equity",
    command=lambda: print_breakeven_equity(underlying_breakeven_result),
    bg="SeaGreen3",
    width=20,
)

underlying_equity_change_button = Button(
    underlying_frame,
    text="Total Equity Return",
    command=lambda: print_equity_change(underlying_equity_change_result),
    bg="SeaGreen3",
    width=20,
)

underlying_ticker_equity_change_button = Button(
    underlying_frame,
    text="Ticker Equity Change",
    command=lambda: print_ticker_equity_change(
        underlying_ticker_equity_change_result, underlying_ticker_entry
    ),
    bg="light sea green",
    width=20,
)

underlying_ticker_option_return_button = Button(
    underlying_frame,
    text="Ticker Options Return",
    command=lambda: ticker_option_returns(
        underlying_ticker_options_result,
        underlying_ticker_entry,
        menu=underlying_strat_menu,
    ),
    bg="light sea green",
    width=20,
)

underlying_combined_return_button = Button(
    underlying_frame,
    text="Ticker Combined",
    command=lambda: print_combined_ticker_return(
        underlying_combined_return_result,
        underlying_ticker_entry,
        underlying_ticker_equity_change_result,
        underlying_ticker_options_result,
    ),
    bg="light sea green",
    width=20,
)

underlying_back_button = Button(
    underlying_frame,
    text="BACK",
    command=lambda: raise_frame(main_frame),
    width=20,
    bg="indian red",
    fg="white",
)

underlying_options_buffer_label = Label(
    underlying_frame,
    text="Return Statistics",
    bg="LightSteelBlue4",
    fg="white",
    font=("Helvetica", 7, "bold"),
    relief=FLAT,
)

underlying_options_buffer_label2 = Label(
    underlying_frame,
    text="Ticker Return Statistics",
    bg="LightSteelBlue4",
    fg="white",
    font=("Helvetica", 7, "bold"),
    relief=FLAT,
)

underlying_ticker_label = Label(
    underlying_frame,
    text="Enter Ticker Symbol",
    bg="LightSteelBlue4",
    fg="white",
    font=("Helvetica", 9, "bold"),
    relief=FLAT,
)

underlying_ticker_strat = Label(
    underlying_frame,
    text="Select Options Strategy",
    bg="LightSteelBlue4",
    fg="white",
    font=("Helvetica", 9, "bold"),
    relief=FLAT,
)

underlying_options_buffer_label3 = Label(underlying_frame, bg="LightSteelBlue4")

underlying_equity_result = Entry(underlying_frame, width=112)
underlying_equity_change_result = Entry(underlying_frame, width=112)
underlying_breakeven_result = Entry(underlying_frame, width=112)
underlying_ticker_entry = Entry(underlying_frame, width=112)
underlying_ticker_equity_change_result = Entry(underlying_frame, width=112)
underlying_ticker_options_result = Entry(underlying_frame, width=112)
underlying_combined_return_result = Entry(underlying_frame, width=112)

strat_list = [
    "All Strategies",
    "Short Call",
    "Long Call",
    "Short Put",
    "Long Put",
    "Short Call Spread",
    "Short Put Spread",
    "Iron Condor",
]
underlying_strat_menu = ttk.Combobox(underlying_frame, values=strat_list, width=109)
underlying_strat_menu.current(0)

underlying_equity_button.grid(row=0, column=0)
underlying_options_buffer_label.grid(row=1, columnspan=2)
underlying_equity_change_button.grid(row=2, column=0)
underlying_breakeven_equity_button.grid(row=3, column=0)
underlying_equity_result.grid(row=0, column=1)
underlying_equity_change_result.grid(row=2, column=1)
underlying_breakeven_result.grid(row=3, column=1)
underlying_options_buffer_label3.grid(row=4)
underlying_options_buffer_label2.grid(row=5, columnspan=2)
underlying_ticker_label.grid(row=6, column=0)
underlying_ticker_entry.grid(row=6, column=1)
underlying_ticker_strat.grid(row=7, column=0)
underlying_strat_menu.grid(row=7, column=1)
underlying_ticker_equity_change_button.grid(row=8, column=0)
underlying_ticker_equity_change_result.grid(row=8, column=1)
underlying_ticker_option_return_button.grid(row=9, column=0)
underlying_ticker_options_result.grid(row=9, column=1)
underlying_combined_return_button.grid(row=10, column=0)
underlying_combined_return_result.grid(row=10, column=1)
underlying_back_button.grid(row=11, columnspan=2)

# Call Ratios Page
call_date_submit = Button(
    call_ratios_frame,
    text="SUBMIT",
    command=lambda: print_ratios(call_watchlist_menu, call_expiration_input, call_ratios_screen),
    bg="DodgerBLue3",
    fg="white",
    width=21,
    height=2,
)
call_ratio_back_button = Button(
    call_ratios_frame,
    text="BACK",
    bg="indian red",
    fg="white",
    command=lambda: raise_frame(main_frame),
    width=20,
)

call_watchlist = Label(
    call_ratios_frame,
    text="Choose a Watchlist",
    width=20,
    bg="LightSteelBlue4",
    fg="white",
)
call_expiration_date = Label(
    call_ratios_frame,
    text="Exp. Date (yyyy-mm-dd)",
    width=20,
    bg="LightSteelBlue4",
    fg="white",
)
call_label = Label(
    call_ratios_frame,
    text="Calls",
    font=("Helvetica", 18, "bold"),
    bg="LightSteelBlue4",
    fg="white",
)

call_expiration_input = Entry(call_ratios_frame, width=20)

call_ratios_screen = Text(call_ratios_frame, width=65, height=13)
call_ratios_screen.insert("1.0", "This will take a while depending on how big your list is!")

call_watchlist_menu = ttk.Combobox(call_ratios_frame, values=main().get_watchlists(), width=17)

call_watchlist.grid(row=0)
call_watchlist_menu.grid(row=0, column=1)
call_expiration_date.grid(row=1)
call_expiration_input.grid(row=1, column=1)
call_date_submit.grid(row=0, rowspan=2, column=2)
call_label.grid(row=3, column=0)
call_ratios_screen.grid(row=3, column=1)
call_ratio_back_button.grid(row=4, column=1)

# Put Ratios Page
put_date_submit = Button(
    put_ratios_frame,
    text="SUBMIT",
    command=lambda: print_ratios(put_watchlist_menu, put_expiration_input, put_ratios_screen),
    bg="DodgerBLue3",
    fg="white",
    width=21,
    height=2,
)
put_ratio_back_button = Button(
    put_ratios_frame,
    text="BACK",
    bg="indian red",
    fg="white",
    command=lambda: raise_frame(main_frame),
    width=20,
)

put_watchlist = Label(
    put_ratios_frame,
    text="Choose a Watchlist",
    width=20,
    bg="LightSteelBlue4",
    fg="white",
)
put_expiration_date = Label(
    put_ratios_frame,
    text="Exp. Date (yyyy-mm-dd)",
    width=20,
    bg="LightSteelBlue4",
    fg="white",
)
put_label = Label(
    put_ratios_frame,
    text="Puts",
    font=("Helvetica", 18, "bold"),
    bg="LightSteelBlue4",
    fg="white",
)

put_expiration_input = Entry(put_ratios_frame, width=20)

put_ratios_screen = Text(put_ratios_frame, width=65, height=13)
put_ratios_screen.insert("1.0", "This will take a while depending on how big your list is!")

put_watchlist_menu = ttk.Combobox(put_ratios_frame, values=main().get_watchlists(), width=17)

put_watchlist.grid(row=0)
put_watchlist_menu.grid(row=0, column=1)
put_expiration_date.grid(row=1)
put_expiration_input.grid(row=1, column=1)
put_date_submit.grid(row=0, rowspan=2, column=2)
put_label.grid(row=3, column=0)
put_ratios_screen.grid(row=3, column=1)
put_ratio_back_button.grid(row=4, column=1)

# Portfolio Earnings Page
port_show_earnings_button = Button(
    port_earnings_frame,
    text="Show Earnings For Companies Within Your Portfolio",
    command=lambda: print_earnings(port_earnings_result),
    bg="DodgerBLue3",
    fg="white",
    width=117,
)
port_earnings_back_button = Button(
    port_earnings_frame,
    text="BACK",
    command=lambda: raise_frame(main_frame),
    bg="indian red",
    fg="white",
    width=20,
)

port_earnings_result = Text(port_earnings_frame, width=60, height=14)

port_show_earnings_button.grid(row=0, column=0, columnspan=2)
port_earnings_result.grid(row=2, column=0, columnspan=2)
port_earnings_back_button.grid(row=3, column=0, columnspan=2)

# List Earnings Page
list_show_earnings_button = Button(
    list_earnings_frame,
    text="Show Earnings",
    command=lambda: print_earnings(list_earnings_result, list_watchlist_menu),
    bg="DodgerBLue3",
    fg="white",
    width=24,
)
list_earnings_back_button = Button(
    list_earnings_frame,
    text="BACK",
    command=lambda: raise_frame(main_frame),
    bg="indian red",
    fg="white",
    width=20,
)
list_watchlist_label = Label(
    list_earnings_frame,
    text="Choose A Watchlist",
    bg="LightSteelBlue4",
    fg="white",
    width=23,
)

list_earnings_result = Text(list_earnings_frame, width=60, height=14)

list_watchlist_menu = ttk.Combobox(list_earnings_frame, values=main().get_watchlists(), width=25)

list_watchlist_label.grid(row=0, column=0)
list_watchlist_menu.grid(row=0, column=1, columnspan=2)
list_show_earnings_button.grid(row=0, column=3)
list_earnings_result.grid(row=2, column=1, columnspan=2)
list_earnings_back_button.grid(row=3, column=1, columnspan=2)

# Execution
if __name__ == "__main__":
    raise_frame(main_frame)
    root.mainloop()
