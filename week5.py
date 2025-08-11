# Name: Ka Yan Dreibelbis
# Course: CIS261
# Week 5, Course Project Part 2 - Using Lists and Dictionaries to Store and Retrieve Data

def get_date_range():
   
    while True:
        from_date = input("Enter FROM date (mm/dd/yyyy): ")
        to_date = input("Enter TO date (mm/dd/yyyy): ")
        if _looks_like_date(from_date) and _looks_like_date(to_date):
            return from_date, to_date
        else:
            print("Dates must be in mm/dd/yyyy. Try again.\n")

def _looks_like_date(s):
   
    return len(s) == 10 and s[2] == "/" and s[5] == "/"

def get_employee_name():
    return input("Enter employee name (or 'End' to finish): ")

def get_total_hours():
    return float(input("Enter total hours worked: "))

def get_hourly_rate():
    return float(input("Enter hourly rate: "))

def get_tax_rate():
  
    return float(input("Enter income tax rate (e.g., 0.15 for 15%): "))


def show_employee_row(frm, to, name, hours, rate, tax_rate):
    gross = hours * rate
    income_tax = gross * tax_rate
    net = gross - income_tax

    print("\n--- Employee ---")
    print("From:", frm, "  To:", to)
    print("Name:", name)
    print("Hours:", hours)
    print("Hourly Rate: $", format(rate, ".2f"))
    print("Gross Pay: $", format(gross, ".2f"))
    print("Tax Rate:", format(tax_rate * 100, ".1f"), "%")
    print("Income Tax: $", format(income_tax, ".2f"))
    print("Net Pay: $", format(net, ".2f"))

    return gross, income_tax, net

def process_and_display_all(from_dates, to_dates, names, hours_list, rates, tax_rates):
    
    totals = {
        "employees": 0,
        "total_hours": 0.0,
        "total_gross": 0.0,
        "total_tax": 0.0,
        "total_net": 0.0
    }

    for i in range(len(names)):
        gross, tax, net = show_employee_row(
            from_dates[i], to_dates[i], names[i],
            hours_list[i], rates[i], tax_rates[i]
        )

        totals["employees"] += 1
        totals["total_hours"] += hours_list[i]
        totals["total_gross"] += gross
        totals["total_tax"] += tax
        totals["total_net"] += net

    return totals

def display_totals(totals_dict):
    print("\n=== Totals ===")
    print("Employees:", totals_dict["employees"])
    print("Total Hours:", totals_dict["total_hours"])
    print("Total Gross: $", format(totals_dict["total_gross"], ".2f"))
    print("Total Tax: $", format(totals_dict["total_tax"], ".2f"))
    print("Total Net: $", format(totals_dict["total_net"], ".2f"))

def main():
    
    from_dates = []
    to_dates = []
    names = []
    hours_list = []
    rates = []
    tax_rates = []

    print("Payroll Program (enter at least 5 employees)")

    while True:
        frm, to = get_date_range()            
        name = get_employee_name()
        if name.lower() == "end":
            break
        hours = get_total_hours()
        rate = get_hourly_rate()
        tax = get_tax_rate()

        
        from_dates.append(frm)
        to_dates.append(to)
        names.append(name)
        hours_list.append(hours)
        rates.append(rate)
        tax_rates.append(tax)

        print("Saved.\n")

   
    totals = process_and_display_all(from_dates, to_dates, names, hours_list, rates, tax_rates)

    display_totals(totals)

main()
