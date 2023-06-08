from datetime import datetime, time, timedelta

from app.services.misc_functions import get_reversed_number


class Palindrome:     
    palindromes = []
    # fill palindromes list
    for hour in range(24):
        minute = get_reversed_number(hour)
        if minute > 59:
            continue
        palindromes.append(time(hour=hour, minute=minute))


    def __init__(self):
        now_datetime = datetime.today()
        self.now_time = time(hour=now_datetime.hour, minute=now_datetime.minute, second=now_datetime.second)


    def get_next(self, from_: time = None) -> time:
        if not from_:
            from_ = self.now_time

        # if now time is palindrome
        if from_.hour == get_reversed_number(from_.minute):
            return from_
        
        # if time more than 23:32 (last palindrome of day)
        if from_ > self.palindromes[-1]:
            return self.palindromes[0]

        for palindrome in self.palindromes:
            if from_ < palindrome:
                return palindrome
            

    def get_time_to_next(self, from_: time = None) -> timedelta:
        if not from_:
            from_ = self.now_time

        next_ = self.get_next()

        from_ = datetime(
            year=1970, 
            month=1, 
            day=1, 
            hour=from_.hour, 
            minute=from_.minute,
            second=from_.second
        )
        next_ = datetime(
            year=1970, 
            month=1, 
            day=(1 if next_ < time(23, 32) else 2), 
            hour=next_.hour, 
            minute=next_.minute,
            second=next_.second
        )

        return next_ - from_