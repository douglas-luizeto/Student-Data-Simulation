import random
from student_profiles import BaseProfile, T1_Profile, T2_Profile, T3_Profile, T4_Profile

class MockStudent:
    def __init__(self, student_id, profile): 
        self.student_id = student_id
        self.profile = profile

    def generate_monthly_data(self, ref_month, total_classes=8, days_studied=30):
        self.churned = random.random() <= self.profile.obtain_churn_probability()
        self.frequency = round(self.profile.simulate_frequency(total_classes) / total_classes, 2)
        self.homework = round(self.profile.simulate_homework(days_studied) / days_studied, 2)

        return {'id': self.student_id,
                'churned': self.churned,
                'reference month': ref_month,
                'frequency': self.frequency,
                'days_studied': self.homework}

    def __repr__(self):
        return f"MockStudent({self.student_id}, {self.profile})"

# Tests

def test_aluno_mock():
    random.seed(10)
    risky_profile = T4_Profile()
    student = MockStudent(student_id=101, profile=risky_profile)
    
    history = student.generate_monthly_data("2026-05", total_classes=8, days_studied=30)
    
    assert history["id"] == 101
    assert history["reference month"] == "2026-05"
    assert "frequency" in history
    assert "days_studied" in history
    assert isinstance(history["churned"], bool)
    
    print("Desafio 2: Sucesso!")

if __name__ == '__main__':
    test_aluno_mock()
