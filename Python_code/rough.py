
SPECIAL_CHAR_ALLOWEDLIST_BANKCARD=["-"," ","_",",","."]
not_allowed_char_regex = f'[^a-zA-Z0-9{"".join(SPECIAL_CHAR_ALLOWEDLIST_BANKCARD)}]'
print(not_allowed_char_regex)