# Description: A program for One Stop Insurance company to input new insurance policy information and perform pertinent calculations therein.
# Author: Chris Morrison
# Dates: July 22, 2024 to July 24, 2024
# Version: 1.0



# Required libraries
from datetime import date
import sys
import time

from functions import is_valid_alpha_input, is_valid_alphanumeric_input, is_valid_province, is_valid_postal_code, is_valid_phone_number
from functions import is_valid_down_payment, write_claim_to_file, first_day_of_next_month, print_formatted_claims


# Program constants

constant_file = open("const.dat", "r")
line = constant_file.readline().strip()
constant = line.split(",")

constant_file.close()

POLICY_NUMBER = int(constant[0])
BASIC_PREMIUM = float(constant[1])
ADDITIONAL_CAR_DISCOUNT = float(constant[2])
LIABILITY_COVERAGE_COST = float(constant[3])
GLASS_COVERAGE_COST = float(constant[4])
LOANER_CAR_COVERAGE_COST = float(constant[5])
HST_RATE = float(constant[6])
MONTHLY_PAYMENT_PROCESSING_FEE = float(constant[7])



# Program functions

def ProgressBar(iteration, total, prefix='', suffix='', length=30, fill='█'):
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
    sys.stdout.flush()


# Main program
while True:

    # Test variables

    """
    customer_name = "Chris Morrison"
    address = "198 Pleasant St."
    city = "St. John's"
    province = "NL"
    formatted_postal = "A1E 1L8"
    formatted_phone = "(709) 725-6520"
    number_of_cars = 3
    extra_liability = "Y"
    glass_coverage = "Y"
    loaner_car = "Y"
    payment_option = "Down Pay"
    payment_option_formatted = 700.00
    """



    # User inputs

    # Customer name input 
    # Validated via alpha input validation function; can also return error message from function. Return split into is_valid and error_message tuple
    print()
    while True:
        customer_name = input("Enter customer name (or QUIT to end): ").strip()
        if customer_name.upper() == "QUIT":
            break
        is_valid, error_message = is_valid_alpha_input(customer_name)
        if is_valid:
            customer_name = customer_name.title()
            break
        else:
            print(error_message)

    if customer_name.upper() == "QUIT":
        break

    # Address input
    # Validated via alphanumeric input validation function; can also return error message from function. Return split into is_valid and error_message tuple
    while True:
        address = input("Enter customer address: ")
        is_valid, error_message = is_valid_alphanumeric_input(address)
        if is_valid:
            address = address.title()
            break
        else:
            print(error_message)

    # City input 
    # Validated via alpha input validation function; can also return error message from function. Return split into is_valid and error_message tuple
    while True:
        city = input("Enter customer city: ")
        is_valid, error_message = is_valid_alpha_input(city)
        if is_valid:
            city = city.title()
            break
        else:
            print(error_message)      

    # Province input      
    while True:
        province = input("Enter customer province: ")
        is_valid, error_message, abbreviation = is_valid_province(province)
        if is_valid:
            province = abbreviation
            break
        else:
            print(error_message)

    # Postal code input
    while True:
        postal_code = input("Enter customer postal code: ")
        is_valid, error_message, formatted_postal = is_valid_postal_code(postal_code)
        if is_valid:
            break
        else:
            print(error_message)
    
    # Phone number input
    while True:
        phone_number = input("Enter customer phone number: ")
        is_valid, error_message, formatted_phone = is_valid_phone_number(phone_number)
        if is_valid:
            break
        else:
            print(error_message)

    # Number of cars being insured
    while True:
        number_of_cars = input("Enter the number of cars being insured: ")
        try:
            number_of_cars = int(number_of_cars)
            if number_of_cars >= 1 and number_of_cars < 1000:
                break
            else:
                print("Number of cars outside range")
        except ValueError:
            print("Invalid number entry")

    # Extra liability option
    while True:
        extra_liability = input("Extra liability selection (Y or N): ").upper()
        if extra_liability in ("Y", "N"):
            break
        else:
            print("Invalid entry")

    # Glass coverage option
    while True:
        glass_coverage = input("Glass coverage selection (Y or N): ").upper()
        if glass_coverage in ("Y", "N"):
            break
        else:
            print("Invalid entry")

    # Loaner car option
    while True:
        loaner_car = input("Loaner car selection (Y or N): ").upper()
        if loaner_car in ("Y", "N"):
            break
        else:
            print("Invalid entry")

    # Payment option
    while True:
        payment_option = input("Payment option selection: ").title()
        if payment_option in ["Full", "Monthly", "Down Pay"]:
            if payment_option == "Down Pay":
                down_payment_amount = input("Enter down payment amount: ")
                is_valid, error_message, payment_option_formatted = is_valid_down_payment(down_payment_amount)
                if is_valid:
                    break
                else:
                    print(error_message)
            else:
                payment_option_formatted = 0.00
                break
        else:
            print("Invalid entry")    
    
    # Customer's previous claims (write to claims.dat)
    while True:
        claim_number = input("Enter previous claim number: ")
        claim_date = input("Enter previous claim date (YYYY-MM-DD): ")
        claim_amount = input("Enter previous claim amount: ")

        write_claim_to_file(claim_number, claim_date, claim_amount)

        another_claim = input("Do you want to enter another claim? (Y or N): ").upper()
        if another_claim == "N":
            break
    


    # Calculations

    # Insurance premiums
    if number_of_cars > 1:
        cars_less_first = number_of_cars - 1
        discount_rate = 1 - ADDITIONAL_CAR_DISCOUNT
        insurance_premium = BASIC_PREMIUM + (BASIC_PREMIUM * discount_rate) * cars_less_first
    else:
        insurance_premium = BASIC_PREMIUM

    # Total extra costs
    liability_cost = LIABILITY_COVERAGE_COST * number_of_cars if extra_liability == "Y" else 0
    glass_cost = GLASS_COVERAGE_COST * number_of_cars if glass_coverage == "Y" else 0
    loaner_cost = LOANER_CAR_COVERAGE_COST * number_of_cars if loaner_car == "Y" else 0
    total_extra_costs = liability_cost + glass_cost + loaner_cost

    # Total insurance premium
    total_insurance_premium = insurance_premium + total_extra_costs

    # HST amount
    HST_amount = total_insurance_premium * HST_RATE

    # Total cost
    total_cost = total_insurance_premium + HST_amount

    # Monthly payment
    if payment_option == "Down Pay":
        reduced_payment = (total_cost - float(down_payment_amount)) + MONTHLY_PAYMENT_PROCESSING_FEE
        monthly_payment = reduced_payment / 8
    elif payment_option == "Monthly":
        monthly_payment = (total_cost + MONTHLY_PAYMENT_PROCESSING_FEE) / 8
    else:
        monthly_payment = 0

    # Determine current date
    current_date = date.today()

    # Determine first payment date
    first_payment_date = first_day_of_next_month(current_date)



    # Display results
    
    residence_DSP = f"{address}, {city}, {province}, {formatted_postal}"
    down_payment_DSP = f"${payment_option_formatted:,.2f}"
    insurance_premium_DSP = f"${insurance_premium:,.2f}"
    extra_costs_DSP = f"${total_extra_costs:,.2f}"
    total_premium_DSP = f"${total_insurance_premium:,.2f}"
    HST_DSP = f"${HST_amount:,.2f}"
    total_cost_DSP = f"${total_cost:,.2f}"
    monthly_payment_DSP = f"${monthly_payment:,.2f}"
    payment_date_DSP = first_payment_date
    liability_cost_DSP = f"${liability_cost:,.2f}"
    glass_cost_DSP = f"${glass_cost:,.2f}"
    loaner_cost_DSP = f"${loaner_cost:,.2f}"

    print()
    print(f"+==============================================================================+")
    print(f"|                                                                              |")
    print(f"|                            ONE STOP INSURANCE CO.                            |")
    print(f"|                                                                              |")
    print(f"|                     Customer Insurance Policy Information                    |")
    print(f"|                                                                              |")
    print(f"|  Policy No:  {POLICY_NUMBER:<6}                               Invoice Date:  {current_date}  |")
    print(f"+==============================================================================+")
    print(f"|                                                                              |")
    print(f"|  CUSTOMER INFORMATION                                                        |")
    print(f"|                                                                              |")
    print(f"|------------------------------------------------------------------------------|")
    print(f"|                                                                              |")
    print(f"|  Name:     {customer_name:<50s}                |")       
    print(f"|  Address:  {residence_DSP:<50s}                |")
    print(f"|  Phone:    {formatted_phone:<50s}                |")    
    print(f"|                                                                              |")
    print(f"|------------------------------------------------------------------------------|")
    print(f"|                                                                              |")
    print(f"|  POLICY DETAILS                                                              |")
    print(f"|                                                                              |")
    print(f"|------------------------------------------------------------------------------|")
    print(f"|                                                                              |")
    print(f"|  Number of Cars:  {number_of_cars:<3d}                                                        |")
    print(f"|  Extra Liability: {extra_liability}          Glass Coverage: {glass_coverage}         Loaner Car: {loaner_car}         |")
    print(f"|  Payment Option:  {payment_option:<8s}                                                   |")  
    print(f"|  Down Payment:    {down_payment_DSP:<10s}                                                 |")
    print(f"|                                                                              |")
    print(f"|  Insurance Premium:                                       {insurance_premium_DSP:>10s}         |")
    print(f"|                                                                              |")
    print(f"|  Extra Costs                                                                 |")
    print(f"|         -  Liability:      {liability_cost_DSP:>10}                                        |")
    print(f"|         -      Glass:      {glass_cost_DSP:>10}                                        |")    
    print(f"|         - Loaner Car:      {loaner_cost_DSP:>10}                                        |")
    print(f"|  Total Extra Costs:                                       {extra_costs_DSP:>10s}         |")    
    print(f"|  Premium Total:                                           {total_premium_DSP:>10s}         |")
    print(f"|  HST:                                                     {HST_DSP:>10s}         |")
    print(f"|  Total Cost:                                              {total_cost_DSP:>10s}         |")
    print(f"|                                                                              |")
    print(f"|  Monthly Payment:                                         {monthly_payment_DSP:>10s}         |")
    print(f"|  First Payment Date:                                      {payment_date_DSP}         |")
    print(f"|                                                                              |")
    print(f"+==============================================================================+")
    print(f"|                                                                              |")
    print(f"|  PREVIOUS CLAIMS                                                             |")
    print(f"|                                                                              |")
    print(f"|------------------------------------------------------------------------------|")
    print(f"|                                                                              |")    

    formatted_claims = print_formatted_claims()
    print(f"|  Claim #   Claim Date   Amount                                               |")
    for formatted_claim in formatted_claims:
        print(formatted_claim)
    
    print(f"|                                                                              |")
    print(f"+==============================================================================+")
    print()



    # Write data to file

    policy_data = (
        f"{POLICY_NUMBER}, "
        f"{current_date}, "
        f"{customer_name}, "
        f"{address}, "
        f"{city}, "
        f"{province}, "
        f"{formatted_postal}, "
        f"{formatted_phone}, "
        f"{number_of_cars}, "
        f"{extra_liability}, "
        f"{glass_coverage}, "
        f"{loaner_car}, "
        f"{payment_option}, "
        f"{payment_option_formatted}, "
        f"{total_insurance_premium} "
    )
    
    with open("policies.dat", "a") as policies_file:
        policies_file.write(policy_data)

    total_iterations = 19
    message = "Saving Policy Data ..."
    for i in range(total_iterations + 1):
        time.sleep(0.1)  
        ProgressBar(i, total_iterations, prefix=message, suffix='Complete', length=39)
    print()

    # Increment values

    POLICY_NUMBER += 1

    

# Additional requirements

print()
print("Program ended")
print()