import helper as h
import pytest
from datetime import date, datetime, timedelta


today = date.today()
mm = f"{today.month}".zfill(2)
yy = f"{today.year}"[2:]
mmstr = today.strftime("%b")
yyyystr = today.strftime("%Y")
input_list = ["0100", "0610", "1218", f"{mm}{yy}", "100", "1320", "0130", "0000", "0120 "]
output_list = [("1 Jan, 2000", "1 Feb, 2000"),
               ("1 Jun, 2010", "1 Jul, 2010"),
               ("1 Dec, 2018", "1 Jan, 2019"),
               (f"1 {mmstr}, {yyyystr}", ""),
               ("", ""),
               ("", ""),
               ("", ""),
               ("", ""),
               ("", "")]


def test_mm_yy_date_slicer_start():
    c = 0
    result_collection = []
    for input in input_list:
        res_start, res_end = h.mm_yy_date_slicer(input)
        result_collection.append((res_start, res_end))
        c = c + 1

    assert result_collection == output_list

