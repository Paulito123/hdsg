import helper as h
import pytest
from datetime import date, datetime, timedelta


today = date.today()
mm = f"{today.month}".zfill(2)
yy = f"{today.year}"[2:]
mmstr = today.strftime("%b")
yyyystr = today.strftime("%Y")

iterative_mmyy_list = ['0100', '0200', '0300', '0400', '0500', '0600', '0700', '0800', '0900', '1000', '1100', '1200',
                       '0101', '0201', '0301', '0401', '0501', '0601', '0701', '0801', '0901', '1001', '1101', '1201',
                       '0102', '0202', '0302', '0402', '0502', '0602', '0702', '0802', '0902', '1002', '1102', '1202',
                       '0103', '0203', '0303', '0403', '0503', '0603', '0703', '0803', '0903', '1003', '1103', '1203',
                       '0104', '0204', '0304', '0404', '0504', '0604', '0704', '0804', '0904', '1004', '1104', '1204',
                       '0105', '0205', '0305', '0405', '0505', '0605', '0705', '0805', '0905', '1005', '1105', '1205',
                       '0106', '0206', '0306', '0406', '0506', '0606', '0706', '0806', '0906', '1006', '1106', '1206',
                       '0107', '0207', '0307', '0407', '0507', '0607', '0707', '0807', '0907', '1007', '1107', '1207',
                       '0108', '0208', '0308', '0408', '0508', '0608', '0708', '0808', '0908', '1008', '1108', '1208',
                       '0109', '0209', '0309', '0409', '0509', '0609', '0709', '0809', '0909', '1009', '1109', '1209',
                       '0110', '0210', '0310', '0410', '0510', '0610', '0710', '0810', '0910', '1010', '1110', '1210',
                       '0111', '0211', '0311', '0411', '0511', '0611', '0711', '0811', '0911', '1011', '1111', '1211',
                       '0112', '0212', '0312', '0412', '0512', '0612', '0712', '0812', '0912', '1012', '1112', '1212',
                       '0113', '0213', '0313', '0413', '0513', '0613', '0713', '0813', '0913', '1013', '1113', '1213',
                       '0114', '0214', '0314', '0414', '0514', '0614', '0714', '0814', '0914', '1014', '1114', '1214',
                       '0115', '0215', '0315', '0415', '0515', '0615', '0715', '0815', '0915', '1015', '1115', '1215',
                       '0116', '0216', '0316', '0416', '0516', '0616', '0716', '0816', '0916', '1016', '1116', '1216',
                       '0117', '0217', '0317', '0417', '0517', '0617', '0717', '0817', '0917', '1017', '1117', '1217',
                       '0118', '0218', '0318', '0418', '0518', '0618', '0718', '0818', '0918', '1018', '1118', '1218',
                       '0119', '0219', '0319', '0419', '0519', '0619', '0719', '0819', '0919', '1019', '1119', '1219',
                       '0120', '0220', '0320', '0420', '0520', '0620', '0720', '0820', '0920', '1020', '1120', '1220',
                       '0121', '0221', '0321', '0421', '0521', '0621', '0721', '0821', '0921', '1021', '1121', '1221',
                       '0122', '0222', '0322', '0422']


def test_mmyy_date_slicer_start():
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
    c = 0
    result_collection = []
    for input in input_list:
        res_start, res_end = h.mmyy_date_slicer(input)
        result_collection.append((res_start, res_end))
        c = c + 1

    assert result_collection == output_list


def test_mmyy_make_iterable_from_to():
    input_list = [("0100", "0200"),
                  ("1121", "0222"),
                  # Relative...
                  ("0422", None),
                  (f"{mm}{yy}", f"{mm}{yy}"),
                  ("0322", ""),
                  # Errors...
                  ("0000", "0100"),
                  ("100", None),
                  ("1120", "0920"),
                  ("0122 ", "")]
    result_list = [['0100','0200'],
                   ['1121','1221','0122','0222'],
                   # Relative...
                   ['0422'],
                   [f"{mm}{yy}"],
                   ["0322","0422"],
                   # Errors...
                   [],
                   [],
                   [],
                   []]

    result_collection = []
    for input in input_list:
        result = h.mmyy_make_iterable_from_to(input[0], input[1])
        result_collection.append(result)

    assert result_collection == result_list