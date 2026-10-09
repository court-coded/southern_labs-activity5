def is_leap_year(year):
     """Returns True if leap year ,False if not """
     return (year % 4 == 0 and year % 100 != 0)

def get_day_of_the_week(month, day, year):
    # month codes from your sheet 
    month_codes = {
        1: 1, # Jan
        2: 4, # Feb
        3: 4, # Mar
        4: 0, # Apr
        5: 2, # May
        6: 5, # Jun
        7: 0, # Jul
        8: 3, # Aug
        9: 6, # Sep
        10: 1, # Oct
        11: 4, # Nov
        12: 6, # Dec
    }
    Last_two =year % 100

    # Step 1: how many 12s fit 
    step1 = Last_two // 12
    # Step 2: remainder
    step2 = Last_two % 12
    # Step 3:how many 4s in remainder
    step3 = step2 // 4
    # Step 4 : day 
    step4 = day 
    # Step 5 : month code + offsets
    step5  = month_codes[month]

    # Special offsets
    # January and February in leap years: add 6
    if month in [1, 2] and is_leap_year(year):
         step5 += 6
      
    # Century offsets 
    if 1600 <= year <= 1699:
        step5 += 6
    elif 1700 <= year <= 1799:
        step5 += 4
    elif 1800 <= year <= 1899:
        step5 += 2
    elif 2000 <= year <= 2099:
        step5 += 6
    elif 2100 <= year <= 2199:
        step5 += 4 

    # Step 6: sum and mod 7 
    total = step1 + step2 + step3 + step4 + step5
    day_num = total % 7

    days = {
         0: "Saturday",
         1: "Sunday",
         2: "Momday",
         3: "Tuesday",
         4: "Wednesday",
         5: "Thursday",
         6: "Friday"
    }

    return days[day_num]

def main ():
    print("Sunday" == get_day_of_the_week(12, 25, 2022))
    print("Friday" == get_day_of_the_week(8, 26, 2022))
    print("Thursday" == get_day_of_the_week(10, 26, 1972))
    print("Wednesday" == get_day_of_the_week(2, 3, 2016))
    print("Monday" == get_day_of_the_week(12, 18, 1899))

if __name__ == "__main__":
    main()
         
