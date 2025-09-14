import pandas as pd

def calculate_business_kpis(df):
    """Calculates key business-focused KPIs for hospitals."""
    if df.empty:
        return {}
        
    # Bed Occupancy Rate (%) - Assuming a fixed number of beds for simplicity (e.g., 500)
    total_beds = 500
    avg_occupancy = (df['patients_admitted'].sum() / (len(df) * total_beds)) * 100
    
    # Average Length of Stay (ALOS)
    avg_alos = df['avg_stay_days'].mean()
    
    # Readmission Rate (%)
    readmission_rate = (df['readmissions'].sum() / df['discharges'].sum()) * 100
    
    # Emergency Room Wait Time
    avg_er_wait_time = df['er_wait_time'].mean()
    
    # Hospital Revenue (total)
    total_revenue = df['revenue'].sum()
    
    # Cost per Patient
    cost_per_patient = df['revenue'].mean() # Using revenue as a proxy for cost
    
    # KPI dataframes for visualizations
    monthly_admissions = df.groupby(pd.Grouper(key='date', freq='M'))['patients_admitted'].sum().reset_index()
    monthly_admissions.columns = ['date', 'Admissions']
    
    dept_performance = df.groupby('department').agg(
        avg_stay_days=('avg_stay_days', 'mean'),
        total_revenue=('revenue', 'sum')
    ).reset_index()
    
    return {
        'avg_occupancy': avg_occupancy,
        'avg_alos': avg_alos,
        'readmission_rate': readmission_rate,
        'avg_er_wait_time': avg_er_wait_time,
        'total_revenue': total_revenue,
        'cost_per_patient': cost_per_patient,
        'monthly_admissions': monthly_admissions,
        'dept_performance': dept_performance,
    }

def calculate_patient_kpis(df):
    """Calculates key patient-focused KPIs."""
    if df.empty:
        return {}
        
    # Patient Satisfaction Score
    avg_satisfaction_score = df['satisfaction_rating'].mean()
    
    # Average Treatment Cost (per condition)
    avg_cost_per_condition = df.groupby('condition')['revenue'].mean().reset_index()
    avg_cost_per_condition.columns = ['Condition', 'Average Revenue']
    
    # Appointment Availability (Waiting days - simulated as inverse of admissions)
    monthly_availability = df.groupby(pd.Grouper(key='date', freq='M'))['patients_admitted'].sum().reset_index()
    monthly_availability['waiting_days'] = 1 / (monthly_availability['patients_admitted'] / monthly_availability['patients_admitted'].mean())
    
    # Out-of-Pocket Expenses vs Insurance Coverage
    avg_out_of_pocket = df['revenue'].mean() * (1 - df['insurance_coverage'].mean())
    avg_insurance_coverage = df['insurance_coverage'].mean() * 100
    
    return {
        'avg_satisfaction_score': avg_satisfaction_score,
        'avg_cost_per_condition': avg_cost_per_condition,
        'monthly_availability': monthly_availability,
        'avg_out_of_pocket': avg_out_of_pocket,
        'avg_insurance_coverage': avg_insurance_coverage,
    }

if __name__ == '__main__':
    try:
        df = pd.read_csv('data/processed/healthcare_processed_data.csv', parse_dates=['date'])
        
        print("--- Business KPIs ---")
        biz_kpis = calculate_business_kpis(df)
        print(f"Bed Occupancy Rate: {biz_kpis['avg_occupancy']:.2f}%")
        print(f"Average Length of Stay: {biz_kpis['avg_alos']:.2f} days")
        print(f"Readmission Rate: {biz_kpis['readmission_rate']:.2f}%")
        
        print("\n--- Patient KPIs ---")
        patient_kpis = calculate_patient_kpis(df)
        print(f"Average Patient Satisfaction: {patient_kpis['avg_satisfaction_score']:.2f} / 5.0")
        print(f"Average Out-of-Pocket Expense: ${patient_kpis['avg_out_of_pocket']:.2f}")
    except FileNotFoundError:
        print("Processed data not found. Please run the ETL script first.")