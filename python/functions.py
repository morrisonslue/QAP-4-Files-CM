# Input alpha validation function

ALPHA_SET = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ. -'")

def is_valid_alpha_input(input_string):
    for character in input_string:
        if character not in ALPHA_SET:
            return False, "Input contains invalid alpha characters"
    return True, ""

# Input alphanumeric validation function

ALPHANUMERIC_SET = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789. -'")

def is_valid_alphanumeric_input(input_string):
    for character in input_string:
        if character not in ALPHANUMERIC_SET:
            return False, "Input contains invalid alphanumeric characters"
    return True, ""

# Input provincial validation function

PROVINCE_LIST = [
    "ALBERTA", "ALTA", "AB", "A.L.T.A.", "A.L.T.A", "A.B",
    "BRITISH COLUMBIA", "BC", "B.C.", "B.C",
    "MANITOBA", "MAN", "MB", "M.B.", "M.B",
    "NEW BRUNSWICK", "NB", "N.B.", "N.B", 
    "NEWFOUNDLAND", "NEWFOUNDLAND AND LABRADOR", "NEWFOUNDLAND & LABRADOR", "NL", "NFLD", "LAB", "LABRADOR", "N.F.L.D.", "N.F.L.D", "N.L", "N.L.",
    "NOVA SCOTIA", "NS", "N.S.", "N.S", 
    "ONTARIO", "ONT", "ON", "O.N.T.", "O.N.T", "O.N",
    "PRINCE EDWARD ISLAND", "PEI", "P.E.I.", "P.E.I", "PE", "P.E.",
    "QUEBEC", "QC", "QUE", "Q.C.", "Q.C", "Q.C.",
    "SASKATCHEWAN", "SASK", "SK", "S.K.", "S.K"
]

PROVINCE_ABBREVIATION = {
    "ALBERTA": "AB",
    "ALTA": "AB",
    "AB": "AB",
    "A.L.T.A.": "AB",
    "A.L.T.A": "AB",
    "A.B": "AB",
    "BRITISH COLUMBIA": "BC",
    "BC": "BC",
    "B.C.": "BC",
    "B.C": "BC",
    "MANITOBA": "MB",
    "MAN": "MB",
    "MB": "MB",
    "M.B.": "MB",
    "M.B": "MB",
    "NEW BRUNSWICK": "NB",
    "NB": "NB",
    "N.B.": "NB",
    "N.B": "NB",
    "NEWFOUNDLAND": "NL",
    "NEWFOUNDLAND AND LABRADOR": "NL",
    "NEWFOUNDLAND & LABRADOR": "NL",
    "NL": "NL",
    "NFLD": "NL",
    "LAB": "NL",
    "LABRADOR": "NL",
    "N.F.L.D.": "NL",
    "N.F.L.D": "NL",
    "N.L": "NL",
    "N.L.": "NL",
    "NOVA SCOTIA": "NS",
    "NS": "NS",
    "N.S.": "NS",
    "N.S": "NS",
    "ONTARIO": "ON",
    "ONT": "ON",
    "ON": "ON",
    "O.N.T.": "ON",
    "O.N.T": "ON",
    "O.N": "ON",
    "PRINCE EDWARD ISLAND": "PE",
    "PEI": "PE",
    "P.E.I.": "PE",
    "P.E.I": "PE",
    "PE": "PE",
    "P.E.": "PE",
    "QUEBEC": "QC",
    "QC": "QC",
    "QUE": "QC",
    "Q.C.": "QC",
    "Q.C": "QC",
    "SASKATCHEWAN": "SK",
    "SASK": "SK",
    "SK": "SK",
    "S.K.": "SK",
    "S.K": "SK",
}

def is_valid_province(province_input):
    province_upper = province_input.upper()
    if province_upper in PROVINCE_LIST:
        return True, "", PROVINCE_ABBREVIATION[province_upper]
    else:
        return False, "Invalid province entry", None
    
# Input postal code validation function. Was reading about re module and match and sub...wanted to try it as an alternative to set

import re

def is_valid_postal_code(postal_input):
    postal_input = postal_input.upper()
    if not re.match(r'^[A-Za-z0-9\s-]+$', postal_input):
        return False, "Postal code contains invalid characters", None
    postal_input = re.sub(r'[\s-]', '', postal_input)
    if re.match(r'^[A-Z][0-9][A-Z][0-9][A-Z][0-9]$', postal_input):
        postal_formatted = f"{postal_input[0:3]} {postal_input[3:]}"
        return True, "", postal_formatted
    else:
        return False, "Postal code format is invalid", None
    
# Input phone number validation function, again testing re with match and sub in lieu of set and returning multiple values

def is_valid_phone_number(phone_input):
    if not re.match(r'^[0-9\s\(\)\-]+$', phone_input):
        return False, "Phone number contains invalid characters", None
    phone_input = re.sub(r'[\s\(\)\-]', '', phone_input)
    if len(phone_input) == 10:
        phone_formatted = f"({phone_input[0:3]}) {phone_input[3:6]}-{phone_input[6:]}"
        return True, "", phone_input
    else:
        return False, "Phone number format is invalid", None

# Down payment input validation function

PAYMENT_SET = set("0123456789.,$")

def is_valid_down_payment(amount):
    for character in amount:
        if character not in PAYMENT_SET:
            return False, "Input contains invalid characters", None
    try:
        amount_formatted = amount.replace("$", "").replace(",", "")
        amount_converted = float(amount_formatted)
        return True, "", amount_converted
    except ValueError:
        return False, "Invalid amount format", None
    
# Previous claim functions

def write_claim_to_file(claim_number, claim_date, claim_amount):
    file = open('claims.dat', 'a')
    file.write(f"{claim_number},{claim_date},{claim_amount}\n")
    file.close()

def print_formatted_claims():
    claims_file = open("claims.dat", "r")
    lines = claims_file.readlines()
    claims_file.close()

    formatted_entries = []

    for line in lines:
        entry = line.strip().split(",")

        claim_number = entry[0]
        claim_date = entry[1]
        claim_amount = float(entry[2])
        formatted_claim_amount = f"{claim_amount:,.2f}"

        formatted_entry = f"|  {claim_number:<8}  {claim_date:<10}   ${formatted_claim_amount:<10}                                          |"
        formatted_entries.append(formatted_entry)
    return formatted_entries

# Determine first day of next month

from datetime import date

def first_day_of_next_month(current_date):
    if current_date.month == 12:
        next_month = 1
        next_year = current_date.year + 1
    else:
        next_month = current_date.month + 1
        next_year = current_date.year
    return date(next_year, next_month, 1)




