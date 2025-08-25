# Name: Ka Yan Dreibelbis
# Course: CIS261
# Week 7, Course Project Part 3 - Using Lists and Dictionaries to Store and Retrieve Data

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

def data_entry():
    print("Payroll Program (enter at least 5 employees)\n")

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

        # write one pipe-delimited record to the text file
        with open(FILENAME, "a", encoding="utf-8") as f:
            f.write(f"{frm}|{to}|{name}|{hrs}|{rate}|{tax}\n")

        print("Saved.\n")

def run_report():
    # ask user which report to run
    choice = input("\nEnter FROM date (mm/dd/yyyy) to filter, or type 'All': ").strip()

    totals = {
        "employees": 0,
        "total_hours": 0.0,
        "total_gross": 0.0,
        "total_tax": 0.0,
        "total_net": 0.0
    }

    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) != 6:
                    continue  # skip bad lines

                frm, to, name, s_hrs, s_rate, s_tax = parts
                hrs = float(s_hrs)
                rate = float(s_rate)
                tax = float(s_tax)

                if choice.lower() != "all" and frm != choice:
                    continue  # skip if not matching

                g, tax_amt, net_amt = show_emp(frm, to, name, hrs, rate, tax)

                totals["employees"] += 1
                totals["total_hours"] += hrs
                totals["total_gross"] += g
                totals["total_tax"] += tax_amt
                totals["total_net"] += net_amt
    except FileNotFoundError:
        print("No employee.txt file found yet.")
        return

    show_totals(totals)

def main():
    data_entry()
    run_report()

if __name__ == "__main__":
    main()
