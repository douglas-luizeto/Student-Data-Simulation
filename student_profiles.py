from abc import ABC, abstractmethod
import random

###########################################
#
# TODO:
# 
# Granularity at the month level
# All profiles are static
# Distributions have clear cutoffs (normals would be better)
#
##########################################

class BaseProfile:

    @abstractmethod
    def obtain_churn_probability(self):
        pass

    @abstractmethod
    def simulate_frequency(self, monthly_classes):
        pass
    
    @abstractmethod
    def simulate_homework(self, days_studied):
        pass

    @abstractmethod
    def __repr__(self):
        pass

# Type-1 (above average): churn: 5%, frequency: 75-100%, homework: 75-100%
class T1_Profile(BaseProfile):
    
    def __init__(self):
        self.churn_probability = 0.05

    def obtain_churn_probability(self):
        return self.churn_probability

    def simulate_frequency(self, monthly_classes):
        return int(monthly_classes * random.randint(75, 100) / 100)

    def simulate_homework(self, days_studied):
        return int(days_studied * random.randint(75, 100) / 100) 

    def __repr__(self):
        return "T1_Profile"

# Type-2 (average): churn: 20%, frequency: 50-100%, homework: 50-100%
class T2_Profile(BaseProfile):
    
    def __init__(self):
        self.churn_probability = 0.20

    def obtain_churn_probability(self):
        return self.churn_probability

    def simulate_frequency(self, monthly_classes):
        return int(monthly_classes * random.randint(50, 100) / 100)

    def simulate_homework(self, days_studied):
        return int(days_studied * random.randint(50, 100) / 100) 

    def __repr__(self):
        return "T2_Profile"

# Type-3 (below average): churn: 50%, frequency: 25-75%, homework: 25-75%
class T3_Profile(BaseProfile):
    
    def __init__(self):
        self.churn_probability = 0.50

    def obtain_churn_probability(self):
        return self.churn_probability

    def simulate_frequency(self, monthly_classes):
        return int(monthly_classes * random.randint(25, 75) / 100)

    def simulate_homework(self, days_studied):
        return int(days_studied * random.randint(25, 75) / 100) 
    
    def __repr__(self):
        return "T3_Profile"

# Type-4 (disengaged): churn: 90%, frequency: 0-50%, homework: 0-50%
class T4_Profile(BaseProfile):
    
    def __init__(self):
        self.churn_probability = 0.90

    def obtain_churn_probability(self):
        return self.churn_probability

    def simulate_frequency(self, monthly_classes):
        return int(monthly_classes * random.randint(0, 50) / 100)

    def simulate_homework(self, days_studied):
        return int(days_studied * random.randint(0, 50) / 100) 

    def __repr__(self):
        return "T4_Profile"

def test_perfis():
    # Fixando a semente para garantir previsibilidade no teste
    random.seed(42) 
    
    t1 = T1_Profile()
    t2 = T2_Profile()
    t3 = T3_Profile()
    t4 = T4_Profile()
    
    assert t1.obtain_churn_probability() == 0.05
    assert t2.obtain_churn_probability() == 0.20
    assert t3.obtain_churn_probability() == 0.50
    assert t4.obtain_churn_probability() == 0.90
    
    # Testando os limites (8 aulas no mês)
    freq_t1 = t1.simulate_frequency(8)
    freq_t2 = t2.simulate_frequency(8)
    freq_t3 = t3.simulate_frequency(8)
    freq_t4 = t4.simulate_frequency(8)

    assert 6 <= freq_t1 <= 8, f"Frequência t1 fora do padrão: {freq_t1}"
    assert 4 <= freq_t2 <= 8, f"Frequência t2 fora do padrão: {freq_t2}"
    assert 2 <= freq_t3 <= 6, f"Frequência t3 fora do padrão: {freq_t3}"
    assert 0 <= freq_t4 <= 4, f"Frequência t4 fora do padrão: {freq_t4}"
    
    hw_t1 = t1.simulate_homework(30)
    hw_t2 = t2.simulate_homework(30)
    hw_t3 = t3.simulate_homework(30)
    hw_t4 = t4.simulate_homework(30)

    assert 22 <= hw_t1 <= 30, f"Número de atividades t1 fora do padrão: {hw_t1}"
    assert 15 <= hw_t2 <= 30, f"Número de atividades t2 fora do padrão: {hw_t2}"
    assert 7 <= hw_t3 <= 23, f"Número de atividades t3 fora do padrão: {hw_t3}"
    assert 0 <= hw_t4 <= 15, f"Número de atividades t4 fora do padrão: {hw_t4}"
    
    
    print("Desafio 1: Sucesso!")

if __name__ == '__main__':
    test_perfis()