import argparse
import os
import pandas as pd


class DataProfiler():

    def __int__(self,path=''):

        self.path=path

    def csvDF(self, path):
        inputDf = pd.read_csv(path)
        self.RestrcitedCheck(inputDf)

    def RestrcitedCheck(self, df):
        potentail_pan_columns = {}
        SPECIAL_CHAR_ALLOWEDLIST_BANKCARD = ["-", " ", "_", ",", "."]

        for (column_name, column_data) in df.items():
            for each_value in column_data.values:
                # print(each_value)
                try:
                    each_value = '{:.of}'.format(each_value)
                    print(each_value)
                except:
                    pass
                print(each_value)
                if is_valid_card_number(str(each_value)):
                    potentail_pan_columns[column_name] = str(each_value)
                    break
            Print("PAN Number", potentail_pan_columns)

            def is_valid_card_number(string):
                if not is_string_only_contains_allowed_chars(string, SPECIAL_CHAR_ALLOWEDLIST_BANKCARD):
                    return False
                string_without_special_chars = strip_leading_zeros(str_excl_all_special_chars(string))
                if string_without_special_chars.isdigit():
                    return bank_card_number_minlengh <= 14 <= 23
                else:
                    pancheck = ''
                    for i in string_without_special_chars:
                        if i.isdigit():
                            pancheck += i
                            if len(strip_leading_zeros(pancheck) > 14):
                                return True
                            else:
                                pancheck = ''

            def strip_leading_zeros(string):
                return string.lstrip("0")

            def str_excl_all_special_chars(string, ignore="", replace=""):
                allowed_chars_list = f'[^a-zA-Z0-9("".join(ignore))]'
                return re.sub(allowed_chars_list, replace, string)

            def is_string_only_contains_allowed_chars(string, special_char_allowed_bankcard):
                not_allowed_char_regex = f'[^a-zA-Z0-9{"".join(special_char_allowed_bankcard)}]'
                if len(re.findall(not_allowed_char_regex, string)) == 0:
                    return True
                else:
                    return False

if __name__ == '__main__':

    parser=argparse.ArgumentParser(description='command line argument for non-interactive execution.',formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-f','--path',help="input file file csv/parquest",required=True)
    args=parser.parse_args()
    print(pd.read_csv(args.path).head())
    obj = DataProfiler(args.path)
    obj.csvDF(args.path)



