import pandas as pd
import numpy as np
import random
from datetime import date, timedelta

def generate_healthcare_data(num_patients=50000, start_date=date(2024, 1, 1), end_date=date(2024, 12, 31)):
    """Generates synthetic healthcare data."""
    
    hospital_ids = [f'HOSPITAL_{i+1:02d}' for i in range(10)]
    departments = ['Emergency', 'Cardiology', 'Oncology', 'Pediatrics', 'General Surgery']
    conditions = ['Influenza', 'Heart Attack', 'Cancer', 'Appendicitis', 'Pneumonia', 'Fracture']
    
    data = []
    current_date = start_date
    
    while current_date <= end_date:
        for _ in range(np.random.randint(50, 150)): # Simulate daily entries
            hospital_id = random.choice(hospital_ids)
            department = random.choice(departments)
            condition = random.choice(conditions)
            
    
            # Simulate hospital metrics
            patients_admitted = np.random.randint(1, 20)
            discharges = np.random.randint(1, patients_admitted + 1)  # ✅ fixed
            readmissions = int(discharges * np.random.uniform(0.01, 0.1))
            avg_stay_days = np.random.uniform(1.5, 15.0)
            er_wait_time = np.random.uniform(0.5, 6.0)

            
            # Simulate financial & patient metrics
            revenue = np.random.uniform(5000, 50000)
            insurance_coverage = np.random.uniform(0.6, 0.95)
            satisfaction_rating = np.random.uniform(3.0, 5.0)
            
            data.append([
                current_date,
                hospital_id,
                department,
                condition,
                patients_admitted,
                discharges,
                readmissions,
                avg_stay_days,
                er_wait_time,
                revenue,
                insurance_coverage,
                satisfaction_rating
            ])
            
        current_date += timedelta(days=1)
    
    df = pd.DataFrame(data, columns=[
        'date', 'hospital_id', 'department', 'condition', 'patients_admitted', 
        'discharges', 'readmissions', 'avg_stay_days', 'er_wait_time', 
        'revenue', 'insurance_coverage', 'satisfaction_rating'
    ])
    
    return df

if __name__ == '__main__':
    df = generate_healthcare_data()
    df.to_csv('data/raw/healthcare_raw_data.csv', index=False)
    print("Synthetic data generated and saved to data/raw/healthcare_raw_data.csv")