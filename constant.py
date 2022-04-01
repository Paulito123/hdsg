### CONSTANTS
BINSIZES = {"1m": 1, "5m": 5, "1h": 60, "4h": 240, "1d": 1440}

if __name__ == '__main__':
    input_list = ["0100", "0610", "1218"]
    start_list = ["1 Jan, 2000", "1 Jun, 2010", "1 Dec, 2018"]
    end_list = ["1 Feb, 2000", "1 Jul, 2010", "1 Jan, 2019"]

    c = 0
    for input in input_list:
        print(f"res_start == start_list[c] {input}>{start_list[c]} where c = {c}")
        print(f"res_start == start_list[c] {input}>{end_list[c]} where c = {c}")
        c = c + 1



