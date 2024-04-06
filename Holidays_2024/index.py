from datetime import date, timedelta
import calendar
# Convert bd_holidays to date objects
bd_holidays = [date.fromisoformat(holiday) for holiday in [
    '2024-01-07', # Bangladesh Parliamentary Polls
    '2024-02-21', # Language Martyrs' Day
    '2024-02-26', # Shab e-Barat
    '2024-03-17', # Sheikh Mujibur Rahman's Birthday
    '2024-03-26', # Independence Day
    '2024-04-05', # Jumatul Bidah
    '2024-04-07', # Shab-e-Qadr
    '2024-04-10', # Eid al-Fitr
    '2024-04-11', # Eid al-Fitr Holiday
    '2024-04-12', # Eid al-Fitr Holiday
    '2024-04-14', # Bengali New Year
    '2024-05-01', # Labour Day
    '2024-05-22', # Buddha Purnima
    '2024-06-16', # Eid-ul-Azha
    '2024-06-17', # Eid-ul-Azha Holiday
    '2024-06-18', # Eid-ul-Azha Holiday
    '2024-07-17', # Ashura
    '2024-08-15', # National Mourning Day
    '2024-08-26', # Janmashtami
    '2024-09-16', # Eid-e-Miladunnabi
    '2024-10-13', # Durga Puja
    '2024-12-16', # Victory Day
    '2024-12-25' # Christmas Day
]]

def working_days(start_date, end_date):
  num_days = (end_date - start_date).days + 1
  working_days = 0
  for day in range(num_days):

    current_date = start_date + timedelta(days=day)
    # Check if weekend (Saturday or Friday)
    if current_date.weekday() not in (calendar.FRIDAY, calendar.SATURDAY):
      # Check if not a government holiday
      
      if current_date not in bd_holidays:
        # print(current_date)
        working_days += 1
  return working_days

# Example usage
date1 = date(2024, 4, 1) 
date2 = date(2024, 4, 30) 

total_working_days = working_days(date1, date2)

print("Total working days between", date1, "and", date2, ":", total_working_days)
