from config import config
import robin_stocks as rs
from RS_Helper import rs_helper
from tkinter import *
import os

dir_path = os.path.dirname((os.path.realpath(__file__)))


def main():
    acc = rs_helper(config, rs)
    acc.login()
    return acc


def export_returns():
    export_result.delete(0, "end")
    output = main().export_options_history()
    export_result.insert(0, "Exported!")


def options_returns(entry, strat=None):
    entry.delete(0, "end")
    if strat != None:
        output = main().get_options_returns_by_strat(strat)
        entry.insert(0, output)
    else:
        output = main().get_options_returns()
        entry.insert(0, output)


def ticker_option_returns(entry, strat=None):
    entry.delete(0, "end")
    ticker = ticker_result.get()
    output = main().get_options_returns_by_ticker(ticker, strat)
    entry.insert(0, output)


def print_call_ratios():
    call_ratios_screen.delete("1.0", "end")
    date = call_expiration_input.get()
    output = main().print_premium_ratios("call", date)
    call_ratios_screen.insert("1.0", output)


def print_put_ratios():
    put_ratios_screen.delete("1.0", "end")
    date = call_expiration_input.get()
    output = main().print_premium_ratios("put", date)
    put_ratios_screen.insert("1.0", output)


def print_earnings():
    earnings_result.delete("1.0", "end")
    output = main().get_earnings_timeline()
    earnings_result.insert("1.0", output)


def raise_frame(frame):
    frame.tkraise()


root = Tk()
root.iconbitmap(f"{dir_path}\Robinhood_Logo.ico")
root.title("Robinhood Helper Tool")

main_frame = Frame(root, bg="LightSteelBlue4")
option_frame = Frame(root, bg="LightSteelBlue4")
ticker_option_frame = Frame(root, bg="LightSteelBlue4")
call_ratios_frame = Frame(root, bg="LightSteelBlue4")
put_ratios_frame = Frame(root, bg="LightSteelBlue4")
earnings_frame = Frame(root, bg="LightSteelBlue4")
frame_list = [
    main_frame,
    option_frame,
    ticker_option_frame,
    call_ratios_frame,
    put_ratios_frame,
    earnings_frame,
]

for frame in frame_list:
    frame.grid(row=0, column=0, sticky="news")

# Main Page
main_label = Label(main_frame,
                   text="Robinhood Helper Tool",
                   width=50,
                   bg="LightSteelBlue4",
                   fg="white")
main_label.config(font=("Courier", 20))

main_buffer1 = Label(main_frame, bg='LightSteelBlue4')
main_buffer2 = Label(main_frame, bg='LightSteelBlue4')

options_button = Button(
    main_frame,
    text="Options Returns Tracker",
    command=lambda: raise_frame(option_frame),
    width=20,
    bg="SeaGreen2",
)

ticker_options_button = Button(
    main_frame,
    text="Option Returns By Ticker",
    command=lambda: raise_frame(ticker_option_frame),
    width=20,
    bg="SeaGreen2",
)

call_ratios_button = Button(
    main_frame,
    text="Call Premium Ratios",
    command=lambda: raise_frame(call_ratios_frame),
    width=20,
    bg="SeaGreen2",
)

put_ratios_button = Button(
    main_frame,
    text="Put Premium Ratios",
    command=lambda: raise_frame(put_ratios_frame),
    width=20,
    bg="SeaGreen2",
)

earnings_button = Button(
    main_frame,
    text="Get Earnings Dates",
    command=lambda: raise_frame(earnings_frame),
    width=20,
    bg="SeaGreen2",
)

main_label.grid(row=0, column=1)
main_buffer1.grid(row=1, column=1)
main_buffer2.grid(row=2, column=1)
options_button.grid(row=3, column=1)
ticker_options_button.grid(row=4, column=1)
call_ratios_button.grid(row=5, column=1)
put_ratios_button.grid(row=6, column=1)
earnings_button.grid(row=7, column=1)

# Options Page
export_button = Button(
    option_frame,
    text="Export Options",
    command=export_returns,
    bg="DodgerBlue3",
    fg="white",
    width=20,
)

export_result = Entry(option_frame, width=100)

buffer_label = Label(
    option_frame,
    text="Options Returns",
    font=("Helvetica", 9, "bold"),
    bg="LightSteelBlue4",
    fg="white",
)

options_short_call_button = Button(
    option_frame,
    text="Short Calls",
    command=lambda: options_returns(options_short_call_result, 'short_call'),
    bg="SeaGreen3",
    width=20,
)

options_long_call_button = Button(
    option_frame,
    text="Long Calls",
    command=lambda: options_returns(options_long_call_result, 'long_call'),
    bg="SeaGreen3",
    width=20)

options_short_put_button = Button(
    option_frame,
    text="Short Puts",
    command=lambda: options_returns(options_short_put_result, 'short_put'),
    bg="SeaGreen3",
    width=20)

options_long_put_button = Button(
    option_frame,
    text="Long Puts",
    command=lambda: options_returns(options_long_put_result, 'long_put'),
    bg="SeaGreen3",
    width=20)

options_short_call_spread_button = Button(
    option_frame,
    text="Short Call Spreads",
    command=lambda: options_returns(options_short_call_spread_result,
                                    'short_call_spread'),
    bg="SeaGreen3",
    width=20,
)

options_short_put_spread_button = Button(
    option_frame,
    text="Short Put Spreads",
    command=lambda: options_returns(options_short_put_spread_result,
                                    'short_put_spread'),
    bg="SeaGreen3",
    width=20,
)

options_iron_condor_button = Button(
    option_frame,
    text="Iron Condors",
    command=lambda: options_returns(options_iron_condor_result, 'iron_condor'),
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
    bg="RosyBrown3",
    fg="white",
)

export_result = Entry(option_frame, width=112)
options_short_call_result = Entry(option_frame, width=112)
options_long_call_result = Entry(option_frame, width=112)
options_short_put_result = Entry(option_frame, width=112)
options_long_put_result = Entry(option_frame, width=112)
options_short_call_spread_result = Entry(option_frame, width=112)
options_short_put_spread_result = Entry(option_frame, width=112)
options_iron_condor_result = Entry(option_frame, width=112)
options_total_result = Entry(option_frame, width=112)

export_button.grid(row=0)
buffer_label.grid(row=1, columnspan=2)
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
    command=lambda: buffer_entry.insert(20, f"{ticker_result.get()}"),
    bg="DodgerBlue3",
    fg="white",
    width=20,
)

ticker_result = Entry(ticker_option_frame, width=112)
ticker_result.insert(
    0,
    "Delete this line and type the ticker symbol (ALL CAPS). Click 'Submit Ticker Symbol'"
)

buffer_entry = Entry(
    ticker_option_frame,
    width=25,
    bg="LightSteelBlue4",
    fg="white",
    justify=CENTER,
    relief=FLAT,
)

buffer_entry.insert(0, "Options Returns for ")

ticker_options_short_call_button = Button(
    ticker_option_frame,
    text="Short Calls",
    command=lambda: ticker_option_returns(ticker_short_call_result,
                                          "short_call"),
    bg="SeaGreen3",
    width=20,
)

ticker_long_call_button = Button(
    ticker_option_frame,
    text="Long Calls",
    command=lambda: ticker_option_returns(ticker_long_call_result, "long_call"
                                          ),
    bg="SeaGreen3",
    width=20,
)

ticker_short_put_button = Button(
    ticker_option_frame,
    text="Short Puts",
    command=lambda: ticker_option_returns(ticker_short_put_result, "short_put"
                                          ),
    bg="SeaGreen3",
    width=20,
)

ticker_long_put_button = Button(
    ticker_option_frame,
    text="Long Puts",
    command=lambda: ticker_option_returns(ticker_long_put_result, "long_put"),
    bg="SeaGreen3",
    width=20,
)

ticker_short_call_spread_button = Button(
    ticker_option_frame,
    text="Short Call Spreads",
    command=lambda: ticker_option_returns(ticker_short_call_spread_result,
                                          "short_call_spread"),
    bg="SeaGreen3",
    width=20,
)

ticker_short_put_spread_button = Button(
    ticker_option_frame,
    text="Short Put Spreads",
    command=lambda: ticker_option_returns(ticker_short_put_spread_result,
                                          "short_put_spread"),
    bg="SeaGreen3",
    width=20,
)

ticker_iron_condor_button = Button(
    ticker_option_frame,
    text="Iron Condors",
    command=lambda: ticker_option_returns(ticker_iron_condor_result,
                                          "iron_condor"),
    bg="SeaGreen3",
    width=20,
)

ticker_total_button = Button(
    ticker_option_frame,
    text="Total Returns",
    command=lambda: ticker_option_returns(ticker_total_result),
    bg="SeaGreen3",
    width=20,
)

ticker_back_button = Button(
    ticker_option_frame,
    text="BACK",
    command=lambda: raise_frame(main_frame),
    width=20,
    bg="RosyBrown3",
    fg="white",
)

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

# Call Ratios Page
call_expiration_date = Label(
    call_ratios_frame,
    text="Exp. Date (yyyy-mm-dd)",
    width=20,
    bg="LightSteelBlue4",
    fg="white",
)

call_expiration_input = Entry(call_ratios_frame, width=20)

call_date_submit = Button(
    call_ratios_frame,
    text="Submit Date",
    command=print_call_ratios,
    bg="DodgerBLue3",
    fg="white",
    width=21,
)

call_label = Label(
    call_ratios_frame,
    text="Calls",
    font=("Helvetica", 18, "bold"),
    bg="LightSteelBlue4",
    fg="white",
)

call_ratios_screen = Text(call_ratios_frame, width=65, height=14)

call_ratio_back_button = Button(
    call_ratios_frame,
    text="BACK",
    bg="RosyBrown3",
    fg="white",
    command=lambda: raise_frame(main_frame),
    width=20,
)

call_expiration_date.grid(row=0)
call_expiration_input.grid(row=0, column=1)
call_date_submit.grid(row=0, column=2)
call_label.grid(row=2, column=0)
call_ratios_screen.grid(row=2, column=1)
call_ratio_back_button.grid(row=3, column=1)

# Put Ratios Page
put_expiration_date = Label(
    put_ratios_frame,
    text="Exp. Date (yyyy-mm-dd)",
    width=20,
    bg="LightSteelBlue4",
    fg="white",
)

put_expiration_input = Entry(put_ratios_frame, width=20)

put_date_submit = Button(
    put_ratios_frame,
    text="Submit Date",
    command=print_put_ratios,
    bg="DodgerBLue3",
    fg="white",
    width=21,
)

put_label = Label(
    put_ratios_frame,
    text="Puts",
    font=("Helvetica", 18, "bold"),
    bg="LightSteelBlue4",
    fg="white",
)

put_ratios_screen = Text(put_ratios_frame, width=65, height=14)

put_ratio_back_button = Button(
    put_ratios_frame,
    text="BACK",
    bg="RosyBrown3",
    fg="white",
    command=lambda: raise_frame(main_frame),
    width=20,
)

put_expiration_date.grid(row=0)
put_expiration_input.grid(row=0, column=1)
put_date_submit.grid(row=0, column=2)
put_label.grid(row=2, column=0)
put_ratios_screen.grid(row=2, column=1)
put_ratio_back_button.grid(row=3, column=1)
# Earnings Page
show_earnings_button = Button(
    earnings_frame,
    text="Show Earnings For Companies Within Your Portfolio",
    command=print_earnings,
    bg="DodgerBLue3",
    fg="white",
    width=117,
)

earnings_result = Text(earnings_frame, width=60, height=14)

earnings_back_button = Button(
    earnings_frame,
    text="BACK",
    command=lambda: raise_frame(main_frame),
    bg="RosyBrown3",
    fg="white",
    width=20,
)

show_earnings_button.grid(row=0, column=0, columnspan=2)
earnings_result.grid(row=2, column=0, columnspan=2)
earnings_back_button.grid(row=3, column=0, columnspan=2)
# Execution
raise_frame(main_frame)
root.mainloop()
