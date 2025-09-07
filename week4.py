# Name: Ka Yan Dreibelbis
# Course: CIS261
# Week 8 – Course Project Phase 4
#
#   users.txt      -> user_id|password|role
#   employees.txt  -> from|to|name|hours|rate|tax

USERS_FILE = "users.txt"
EMP_FILE   = "employees.txt"

# ---------- small helpers ----------
def read_all(path):
    """Read non-empty lines from a text file, or [] if it doesn't exist."""
    try:
        with open(path, "r") as f:
            return [ln.strip() for ln in f if ln.strip()]
    except FileNotFoundError:
        return []

def append_line(path, text):
    """Append one line to a text file (creates file if missing)."""
    with open(path, "a") as f:
        f.write(text + "\n")

def is_mmddyyyy(s):
    """Very basic date shape check like Phase 3 (no datetime import)."""
    return len(s) == 10 and s[2] == "/" and s[5] == "/"

# ---------- Phase 4: user setup ----------
def add_users_loop():
    """
    Keep asking for user accounts until user_id == 'End'.
    Validate: unique user_id, role in {'Admin','User'}.
    Write rows to users.txt as: user|pwd|role
    """
    print("=== User Setup ===")
    print("Add accounts (type 'End' for user id to stop).")
    # build a set of existing ids for quick duplicate checks
    existing = set()
    for row in read_all(USERS_FILE):
        parts = row.split("|")
        if len(parts) == 3:
            existing.add(parts[0])

    while True:
        uid = input("User ID: ")
        if uid.lower() == "end":
            break
        if uid in existing:
            print("That user id already exists. Try another.\n")
            continue

        pwd  = input("Password: ")
        role = input("Role (Admin/User): ")
        if role not in ("Admin", "User"):
            print("Role must be Admin or User. Try again.\n")
            continue

        append_line(USERS_FILE, f"{uid}|{pwd}|{role}")
        existing.add(uid)
        print("Saved.\n")

def show_all_users():
    """Simple display so you can screenshot what's in users.txt."""
    rows = read_all(USERS_FILE)
    print("\n=== Current Users ===")
    if not rows:
        print("(none)\n")
        return
    for r in rows:
        p = r.split("|")
        if len(p) == 3:
            print(f"User: {p[0]}   Password: {p[1]}   Role: {p[2]}")
    print()

# ---------- Phase 4: login ----------
class Login:
    """Just holds who logged in and their role so we can print and check it."""
    def __init__(self, user_id, password, role):
        self.user_id = user_id
        self.password = password
        self.role = role

def do_login():
    """Return Login object on success, or None to abort."""
    rows = read_all(USERS_FILE)
    # map id -> (pwd, role)
    creds = {}
    for r in rows:
        p = r.split("|")
        if len(p) == 3:
            creds[p[0]] = (p[1], p[2])

    print("\n== Login ==")
    uid = input("User ID: ")
    if uid not in creds:
        print("User id not found. Exiting.")
        return None
    pwd = input("Password: ")
    real_pwd, role = creds[uid]
    if pwd != real_pwd:
        print("Password does not match. Exiting.")
        return None
    return Login(uid, pwd, role)

# ---------- Phase 3 core: employee entry + report ----------
def enter_employee_data():
    """
    Admin-only: append employee rows until name == 'End'.
    We keep Phase 3 format exactly: from|to|name|hours|rate|tax
    """
    print("\n=== Employee Data Entry ===")
    while True:
        frm = input("FROM date (mm/dd/yyyy): ")
        if frm.lower() == "end":
            break
        to = input("TO date (mm/dd/yyyy): ")
        if to.lower() == "end":
            break
        if not (is_mmddyyyy(frm) and is_mmddyyyy(to)):
            print("Dates must be mm/dd/yyyy. Try again.\n")
            continue

        name = input("Employee name (or 'End' to stop): ")
        if name.lower() == "end":
            break

        # keep inputs simple like Phase 3 (basic float conversion)
        try:
            hours = float(input("Total hours: "))
            rate  = float(input("Hourly rate: "))
            tax   = float(input("Tax rate (e.g., 0.15): "))
        except ValueError:
            print("Invalid number, try again.\n")
            continue

        append_line(EMP_FILE, f"{frm}|{to}|{name}|{hours}|{rate}|{tax}")
        print("Saved.\n")

def calc_totals(hours, rate, tax):
    gross = hours * rate
    inc_tax = gross * tax
    net = gross - inc_tax
    return gross, inc_tax, net

def show_emp(frm, to, name, hours, rate, tax):
    """Print detail for one employee and return (gross, tax, net)."""
    g, t, n = calc_totals(hours, rate, tax)
    print("\n--- Employee ---")
    print("From:", frm, "To:", to)
    print("Name:", name)
    print("Hours:", hours)
    print("Hourly Rate: $", format(rate, ".2f"))
    print("Gross Pay: $", format(g, ".2f"))
    print("Tax Rate:", format(tax * 100, ".1f"), "%")
    print("Income Tax: $", format(t, ".2f"))
    print("Net Pay: $", format(n, ".2f"))
    return g, t, n

def show_totals(t):
    """Totals dictionary display, same idea as your Phase 3."""
    print("\n=== Totals ===")
    print("Employees:", t["emp"])
    print("Total Hours:", t["hours"])
    print("Total Gross: $", format(t["gross"], ".2f"))
    print("Total Tax: $", format(t["tax"], ".2f"))
    print("Total Net: $", format(t["net"], ".2f"))

def run_report():
    """
    Ask for FROM date or 'All'.
    Read employees.txt and print matching rows then totals.
    """
    rows = read_all(EMP_FILE)
    if not rows:
        print("\nNo employee records found.")
        return

    pick = input("\nRun report for FROM date (mm/dd/yyyy) or 'All': ")
    want_all = (pick.lower() == "all")

    totals = {"emp": 0, "hours": 0.0, "gross": 0.0, "tax": 0.0, "net": 0.0}

    for r in rows:
        p = r.split("|")
        if len(p) != 6:
            continue
        frm, to, name, hs, rt, tx = p
        if not want_all and frm != pick:
            continue

        hours = float(hs)
        rate  = float(rt)
        tax   = float(tx)

        g, t, n = show_emp(frm, to, name, hours, rate, tax)
        totals["emp"]   += 1
        totals["hours"] += hours
        totals["gross"] += g
        totals["tax"]   += t
        totals["net"]   += n

    show_totals(totals)

# ---------- main flow ----------
def main():
    print("Payroll Security App (Phase 4)")

    # Step 1: user setup (you can press End right away if users already exist)
    add_users_loop()
    show_all_users()

    # Step 2: login
    who = do_login()
    if not who:
        return

    # Per instructions: show who is logged in before any output
    print(f"\nLogged in as: {who.user_id}   Role: {who.role}\n")

    # Step 3: authorization
    if who.role == "Admin":
        # Admin can enter data and run reports
        enter_employee_data()
        run_report()
    else:
        # User can only run reports
        run_report()

if __name__ == "__main__":
    main()
