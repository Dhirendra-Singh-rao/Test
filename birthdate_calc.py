def day():
    return int(input("Enter your birth day: "))

def month():
    return int(input("Enter your birth month: "))

def year():
    return int(input("Enter your birth year: "))

def age(y, m, d):
    # Today's date (set manually)
    cy, cm, cd = 2025, 8, 6

    # Adjust days
    if cd < d:
        cm -= 1
        cd += 30  # assume average month length

    # Adjust months
    if cm < m:
        cy -= 1
        cm += 12

    years = cy - y
    months = cm - m
    days = cd - d

    print("Your current age is", years, "years", months, "months", days, "days")

def main():
    y = year()
    m = month()
    d = day()
    age(y, m, d)

if __name__ == "__main__":
    main()
