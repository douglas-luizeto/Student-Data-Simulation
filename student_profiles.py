import random
import datetime

"""
TODO: 

1. Include helper methods to calculate standard deviations for each variable (churn, presence, etc.).
   All variables are modeled as Bernoulli.

2 Improve tests in order to verify the statistical distributions make sense. 

"""
class StudentProfile:

    def __init__(self, 
                 churn_probability,
                 present_probability,
                 homework_on_weekdays,
                 homework_on_weekends):

        self.churn_probability = churn_probability
        self.present_probability = present_probability
        self.homework_on_weekdays = homework_on_weekdays
        self.homework_on_weekends = homework_on_weekends

    def present_in_class(self) -> bool:
        return random.random() <= self.present_probability 

    def did_homework(self, date) -> bool:
        if date.weekday() < 5:
            return random.random() <= self.homework_on_weekdays
        else:
            return random.random() <= self.homework_on_weekends

    def __repr__(self):
        return f"StudentProfile({self.churn_probability}, {self.present_probability}, {self.homework_on_weekdays}, {self.homework_on_weekends})"

def profile_tests():
    # Fixing seed to garantee predictability
    # random.seed(42) 

    # Type-1 (above average): churn: 5%, frequency: 90%, homework: 85% (weekdays) | 60% (weekends)
    s1 = StudentProfile(0.05, 0.90, 0.85, 0.5)

    # Type-2 (average): churn: 20%, frequency: 75%, homework: 60% (weekdays) | 40% (weekends)
    s2 = StudentProfile(0.2, 0.75, 0.6, 0.4)
    
    # Type-3 (below average): churn: 50%, frequency: 50%, homework: 40% (weekdays) | 25% (weekends)
    s3 = StudentProfile(0.5, 0.5, 0.4, 0.25)
    
    # Type-4 (disengaged): churn: 70%, frequency: 25%, homework: 25% (weekdays) | 10% (weekends)
    s4 = StudentProfile(0.7, 0.25, 0.25, 0.10)
    
    assert s1.churn_probability == 0.05
    assert s2.churn_probability == 0.20
    assert s3.churn_probability == 0.50
    assert s4.churn_probability == 0.70

    freq_s1 = freq_s2 = freq_s3 = freq_s4 = 0
    for _ in range(8):
        freq_s1 += int(s1.present_in_class()) 
        freq_s2 += int(s2.present_in_class())
        freq_s3 += int(s3.present_in_class())
        freq_s4 += int(s4.present_in_class())
        
    assert 6 <= freq_s1 <= 8, f"Frequência s1 fora do padrão: {freq_s1}"
    assert 4 <= freq_s2 <= 8, f"Frequência s2 fora do padrão: {freq_s2}"
    assert 2 <= freq_s3 <= 6, f"Frequência s3 fora do padrão: {freq_s3}"
    assert 0 <= freq_s4 <= 4, f"Frequência s4 fora do padrão: {freq_s4}"

    print(freq_s1, freq_s2, freq_s3, freq_s4)

    date = datetime.date(2024, 8, 1)
    
    hw_s1 = hw_s2 = hw_s3 = hw_s4 = 0
    for i in range(30):
        hw_s1 += int(s1.did_homework(date + datetime.timedelta(i)))
        hw_s2 += int(s2.did_homework(date + datetime.timedelta(i)))
        hw_s3 += int(s3.did_homework(date + datetime.timedelta(i)))
        hw_s4 += int(s4.did_homework(date + datetime.timedelta(i)))

    print(hw_s1, hw_s2, hw_s3, hw_s4)

    # assert 22 <= hw_s1 <= 30, f"Número de atividades s1 fora do padrão: {hw_s1}"
    # assert 15 <= hw_s2 <= 30, f"Número de atividades s2 fora do padrão: {hw_s2}"
    # assert 7 <= hw_s3 <= 23, f"Número de atividades s3 fora do padrão: {hw_s3}"
    # assert 0 <= hw_s4 <= 15, f"Número de atividades s4 fora do padrão: {hw_s4}"
    
if __name__ == '__main__':
    profile_tests()