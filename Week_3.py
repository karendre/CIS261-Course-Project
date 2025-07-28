# Ka Yan Drebelbis
# Course: CIS261
# Week 3, Project Phase 1
# Create and Call Functions with Parameters

def get_employee_name():
    """Prompt the user to enter the employee's name."""
    name = input("Enter employee name (or type 'End' to finish): ")
    return name

def get_total_hours():
    """Prompt the user to enter total hours worked, with validation."""
    while True:
        try:
            hours = float(input("Enter total hours worked: "))
            if hours < 0:
                print("Hours cannot be negative. Please try again.")
                continue
            return hours
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_hourly_rate():
    """Prompt the user to enter the hourly rate, with validation."""
    while True:
        try:
            rate = float(input("Enter hourly rate: "))
            if rate < 0:
                print("Hourly rate cannot be negative. Please try again.")
                continue
            return rate
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_tax_rate():
    """Prompt the user to enter the tax rate, with validation."""
    while True:
        try:
            tax_rate = float(input("Enter income tax rate (e.g., 0.15 for 15%): "))
            if not (0 <= tax_rate <= 1):
                print("Tax rate must be between 0 and 1. Please try again.")
                continue
            return tax_rate
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def calculate_pay(hours, rate, tax_rate):
    """Calculate gross pay, income tax, and net pay."""
    gross_pay = hours * rate
    income_tax = gross_pay * tax_rate
    net_pay = gross_pay - income_tax
    return gross_pay, income_tax, net_pay

def show_employee_details(name, hours, rate, tax_rate, gross, tax, net):
    """Display the details of an employee's pay."""
    print("\n--- Employee Summary ---")
    print("Name:", name)
    print("Total Hours:", hours)
    print("Hourly Rate: $", format(rate, ".2f"))
    print("Gross Pay: $", format(gross, ".2f"))
    print("Tax Rate:", format(tax_rate * 100, ".1f"), "%")
    print("Income Tax: $", format(tax, ".2f"))
    print("Net Pay: $", format(net, ".2f"))
    print("------------------------\n")

def show_final_totals(emp_count, total_hours, total_gross, total_tax, total_net):
    """Display the final totals for all employees."""
    print("\n=== Final Totals ===")
    print("Total Employees:", emp_count)
    print("Total Hours Worked:", total_hours)
    print("Total Gross Pay: $", format(total_gross, ".2f"))
    print("Total Tax: $", format(total_tax, ".2f"))
    print("Total Net Pay: $", format(total_net, ".2f"))

# Main Program
def main():
    emp_count = 0
    total_hours = 0
    total_gross = 0
    total_tax = 0
    total_net = 0

    while True:
        name = get_employee_name()
        if name.lower() == "end":
            break

        hours = get_total_hours()
        rate = get_hourly_rate()
        tax_rate = get_tax_rate()

        gross, tax, net = calculate_pay(hours, rate, tax_rate)

        show_employee_details(name, hours, rate, tax_rate, gross, tax, net)

        emp_count += 1
        total_hours += hours
        total_gross += gross
        total_tax += tax
        total_net += net

    show_final_totals(emp_count, total_hours, total_gross, total_tax, total_net)

# Call Main
main()
