import random
import uuid
from student_profiles import T1_Profile, T2_Profile, T3_Profile, T4_Profile
from mock_student import MockStudent


class StudentFactory:
    
    def __init__(self, profile_distribution):

        if( sum([x[1] for x in profile_distribution]) != 1.0):
            raise ValueError("Provided values are not a valid probability distribution.")
        else: 
            self.profile_distribution = profile_distribution

    def generate_cohort(self, n):

        profiles = [x[0] for x in profile_distribution]
        weights = [x[1] for x in profile_distribution]

        cohort_profiles = random.choices(profiles, weights=weights, k = n)

        return [MockStudent(uuid.uuid4(), p) for p in cohort_profiles]

    
profile_distribution = [(T1_Profile(), 0.05),
                        (T2_Profile(), 0.3),
                        (T3_Profile(), 0.5),
                        (T4_Profile(), 0.15)]

Factory = StudentFactory(profile_distribution)

students = Factory.generate_cohort(20)

for s in students:
    print(s)
    print(s.generate_monthly_data(ref_month="2026-04", total_classes=8, days_studied=30))