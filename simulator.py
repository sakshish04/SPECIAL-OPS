import pandas as pd
import random

def generate_payment_data(n=75):
    banks = ['HDFC', 'ICICI', 'Axis', 'SBI']
    methods = ['UPI', 'Credit_Card', 'Debit_Card']
    data = []
    
    for i in range(n):
        bank = random.choice(banks)
        method = random.choice(methods)
        amount = random.randint(100, 15000)
        
        # PATTERN A: Systemic Bank Failure (First 10 Rows)
        if i < 10: 
            bank, method = 'HDFC', 'UPI'
            status, error, latency = 'Failed', '504_GATEWAY_TIMEOUT', random.randint(4000, 6000)
        
        # PATTERN B: Security/Guardrail Edge Case (Next 10 Rows)
        elif 10 <= i < 20:
            status, error, latency = 'Failed', 'RISK_THRESHOLD_EXCEEDED', random.randint(100, 300)
            amount = random.randint(10001, 15000) # Force guardrail trigger
            
        # REGULAR TRAFFIC (Remaining Rows)
        else:
            status = 'Success'
            error = 'None'
            latency = random.randint(150, 450)

        data.append({
            "Transaction_ID": f"TXN_{random.randint(10000, 99999)}",
            "Amount": amount,
            "Bank": bank,
            "Method": method,
            "Status": status,
            "Error": error,
            "Latency_ms": latency
        })
    
    # Shuffle to simulate a real-time mixed stream
    return pd.DataFrame(data).sample(frac=1).reset_index(drop=True)