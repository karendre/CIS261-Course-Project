# Name:  Ka Yan Dreibelbis
# Course: CIS261
# Week 5, Course Project Part 2 - Using Lists and Dictionaries to Store and Retrieve Data

FILENAME = "employee.txt"   # from|to|name|hours|rate|tax

def get_dates():
    while True:
        frm = input("Enter FROM date (mm/dd/yyyy) (or 'End' to finish): ")
        if frm.lower() == "end":
            return None, None, True

        to = input("Enter TO date (mm/dd/yyyy): ")
        if to.lower() == "end":
            return None, None, True

        ok = (len(frm) == 10 and frm[2] == "/" and frm[5] == "/"
              and len(to) == 10 and to[2] == "/" and to[5] == "/")
        if ok:
            return frm, to, False
        else:
            print("Dates must be in mm/dd/yyyy. Try again.\n")

def show_emp(frm, to, name, hrs, rate, tax):
    gross = hrs * rate
    inc_tax = gross * tax
    net = gross - inc_tax

    print("\n--- Employee ---")
    print("From:", frm, " To:", to)
    print("Name:", name)
    print("Hours:", hrs)
    print("Hourly Rate: $", format(rate, ".2f"))
    print("Gross Pay: $", format(gross, ".2f"))
    print("Tax Rate:", format(tax * 100, ".1f"), "%")
    print("Income Tax: $", format(inc_tax, ".2f"))
    print("Net Pay: $", format(net, ".2f"))
    return gross, inc_tax, net

def show_totals(tot):
    print("\n=== Totals ===")
    print("Employees:", tot["employees"])
    print("Total Hours:", tot["total_hours"])
    print("Total Gross: $", format(tot["total_gross"], ".2f"))
    print("Total Tax: $", format(tot["total_tax"], ".2f"))
    print("Total Net: $", format(tot["total_net"], ".2f"))

def main():
    # parallel lists for this run
    from_dates, to_dates = [], []
    names, hours, rates, taxes = [], [], [], []

    print("Payroll Program (enter at least 2 employees)\n")

    while True:
        frm, to, stop = get_dates()  # must be first call in loop
        if stop:
            break

        name = input("Enter employee name (or 'End' to finish): ")
        if name.lower() == "end":
            break

        try:
            hrs = float(input("Enter total hours worked: "))
            rate = float(input("Enter hourly rate: "))
            tax = float(input("Enter income tax rate (e.g., 0.15 for 15%): "))
        except ValueError:
            print("Invalid number entered. Start this employee over.\n")
            continue

        from_dates.append(frm)
        to_dates.append(to)
        names.append(name)
        hours.append(hrs)
        rates.append(rate)
        taxes.append(tax)
        print("Saved.\n")

        # write one pipe-delimited record to the text file
        try:
            with open(FILENAME, "a", encoding="utf-8") as f:
                f.write(f"{frm}|{to}|{name}|{hrs}|{rate}|{tax}\n")
        except OSError:
            print("(Could not write to employee.txt)")

    # totals dictionary for this run
    totals = {
        "employees": 0,
        "total_hours": 0.0,
        "total_gross": 0.0,
        "total_tax": 0.0,
        "total_net": 0.0
    }

    i = 0
    while i < len(names):
        g, tax_amt, net_amt = show_emp(
            from_dates[i], to_dates[i], names[i], hours[i], rates[i], taxes[i]
        )
        totals["employees"] += 1
        totals["total_hours"] += hours[i]
        totals["total_gross"] += g
        totals["total_tax"] += tax_amt
        totals["total_net"] += net_amt
        i += 1

    show_totals(totals)

if __name__ == "__main__":
    main()
