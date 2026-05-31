import random
import datetime

"""
TODO: 

1. Improve tests to make sure statistical distributions make sense.

"""

class FinantialProfile:

    """
    - The amount of days late is calculated by casting to int a sample drawn from a normal distribution with 
    mean = self.delay_avg and std = self.delay_std
    default_probability: probability of silent churn, without paying or communicating.

    """

    def __init__(self, monthly_fee, delay_avg, delay_std, default_probability): 

        self.monthly_fee = monthly_fee
        self.delay_avg = delay_avg
        self.delay_std = delay_std
        self.default_probability = default_probability
    
    @property
    def _has_defaulted(self):
        return random.random() <= self.default_probability

    def simulate_payment(self, date):
        if self._has_defaulted:
            return {"ref_year": date.year,
                    "ref_month": date.month,
                    "value": "default",
                    "days_late": None
                   }
        else:
            return {"ref_year": date.year,
                    "ref_month": date.month,
                    "value": self.monthly_fee,
                    "days_late": int(random.normalvariate(self.delay_avg, self.delay_std))
                   }
    
def profile_tests():
    
    f1 = FinantialProfile(360, -3, 0.3, 0.01)
    f2 = FinantialProfile(343, 0, 1, 0.05)
    f3 = FinantialProfile(331, 0, 2, 0.10)
    f4 = FinantialProfile(360, 5, 3, 0.15)

    date = datetime.date(2023, 11, 30)

    print(f1.simulate_payment(date))
    print(f2.simulate_payment(date))
    print(f3.simulate_payment(date))
    print(f4.simulate_payment(date))

if __name__ == "__main__":
    profile_tests()

    
    