import os
from dotenv import load_dotenv
from google import genai

# 1. Load your key
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# 2. Setup the Modern Client
client = genai.Client(api_key=api_key)

def analyze_payment_failures(df):
    """Reasoning with Gemini 3 Flash Preview."""
    data_string = df.to_string()
    
    prompt = f"""
    You are a Fintech Ops Agent. Analyze this data: {data_string}
    
    1. Identify patterns (Bank/Method failures).
    2. Suggest an action (Reroute or Alert).
    3. If any transaction is > 10,000, say 'Guardrail Triggered'.
    """
    
    try:
        # Using the EXACT ID from your verified list
        response = client.models.generate_content(
            model='gemini-3-flash-preview', 
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"❌ AI Error: {e}"

if __name__ == "__main__":
    from simulator import generate_payment_data
    test_df = generate_payment_data()
    print("✅ API Key found!" if api_key else "❌ API Key missing!")
    print("\n--- AGENT IS REASONING (GEMINI 3 MODE) ---")
    print(analyze_payment_failures(test_df))