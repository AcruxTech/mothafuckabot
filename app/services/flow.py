from datetime import datetime, time, timedelta


class Flow:     
    flows = []
    # fill flows list
    for hour in range(24):
        flows.append(time(hour=hour, minute=hour))


    def __init__(self):
        now_datetime = datetime.today()
        self.now_time = time(hour=now_datetime.hour, minute=now_datetime.minute, second=now_datetime.second)


    def get_next(self, from_: time = None) -> time:
        if not from_:
            from_ = self.now_time

        # if now time is flow
        if from_.hour == from_.minute:
            return from_
        
        for flow in self.flows:
            if from_ < flow:
                return flow

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