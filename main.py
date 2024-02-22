def calc_year_code(year):
    formatted_year = int(str(year)[2:])
    
    first_result = ((formatted_year // 2) // 2) % 7
    last_result = (formatted_year + first_result) % 7
    
    return last_result

def is_year_leap(year):
    if year < 1852:
        return False
    
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 4 == 0 and year % 400 == 0:
        return True
    else:
        return False

def days_in_month(year, month):
    if not isinstance(year, int) or not isinstance(month, int):
        return None
    
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if month == 2 and is_year_leap(year):
        return 29
    
    return month_days[month - 1]

def day_of_year(year, month, day):
    if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int) or year < 1000:
        return None
    
    weakdays = ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado']
    month_codes = [6, 2, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    year_leap = is_year_leap(year)
    
    century = int(str(year)[:2]) - 20
    day_code = day % 7
    year_code = calc_year_code(year)
    month_code = month_codes[month - 1]
    
    if year_leap and month == 1 or year_leap and month == 2:
        month_code -= 1
        
    result_code = century + day_code + year_code + month_code
    
    if result_code > 7:
        result_code -= 7
    
    return weakdays[result_code]

print(day_of_year(2023, 1, 12))
