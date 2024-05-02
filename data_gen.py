from faker import Faker
import random
from datetime import datetime, timedelta
import csv

def generate_healthcare_claim_data(num_records):
    fake = Faker()

    # Realistic data for diagnosis and claim status
    diagnosis_descriptions = [
        'Upper Respiratory Infection',
        'Type 2 Diabetes Mellitus',
        'Hypertension',
        'Acute Pharyngitis',
        'Asthma',
        'Osteoarthritis',
        'Acute Bronchitis',
        'Anxiety Disorder',
        'Depressive Disorder',
        'Dermatitis',
        'Urinary Tract Infection',
        'Coronary Atherosclerosis'
    ]
    claim_statuses = ['Approved', 'Pending', 'Rejected']

    # Realistic provider names
    provider_names = [
        'St. Mary\'s Medical Center',
        'General Hospital Corporation',
        'Mercy Health System',
        'University of Washington Medical Center',
        'Mayo Clinic',
        'Cleveland Clinic',
        'Johns Hopkins Hospital',
        'Massachusetts General Hospital',
        'Mount Sinai Hospital',
        'NYU Langone Health',
        'UCLA Health',
        'Stanford Health Care'
    ]

    claims_data = []

    for _ in range(num_records):
        # Generate random claim data
        patient = fake.name()
        diagnosis_description = random.choice(diagnosis_descriptions)
        procedure_code = fake.random_element(elements=('12001', '23045', '45678', '78901'))  # Example: Realistic procedure codes
        provider = random.choice(provider_names)  # Randomly select a realistic provider name
        bill_amount = round(random.uniform(100.00, 1000.00), 2)  # Random bill amount between 100 and 1000
        claim_status = random.choice(claim_statuses)
        
        # Generate random dates for service date and claim submission date
        service_date = datetime.now() - timedelta(days=random.randint(1, 365))
        claim_submission_date = service_date + timedelta(days=random.randint(1, 30))

        # Construct the claim data dictionary
        claim = {
            'patient': patient,
            'diagnosis_description': diagnosis_description,
            'procedure_code': procedure_code,
            'provider': provider,
            'service_date': service_date.strftime('%Y-%m-%d'),
            'claim_submission_date': claim_submission_date.strftime('%Y-%m-%d'),
            'bill_amount': bill_amount,
            'claim_status': claim_status
        }
        
        claims_data.append(claim)

    return claims_data

def write_healthcare_claim_data_to_csv(data, filename):
    fieldnames = ['patient', 'diagnosis_description', 'procedure_code', 'provider', 
                  'service_date', 'claim_submission_date', 'bill_amount', 'claim_status']
    
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        writer.writeheader()
        for claim in data:
            writer.writerow(claim)

# Example usage:
num_records = 10
claims_data = generate_healthcare_claim_data(num_records)

filename = 'healthcare_claims.csv'
write_healthcare_claim_data_to_csv(claims_data, filename)
print(f"Generated data has been written to '{filename}'")
