import os
from dotenv import load_dotenv
import json
from openai import OpenAI
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Required OpenAI config
OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'gpt-4o-mini')
OPENAI_MAX_TOKENS = int(os.getenv('OPENAI_MAX_TOKENS', '1000'))
OPENAI_TEMPERATURE = float(os.getenv('OPENAI_TEMPERATURE', '0.7'))

# Required Gemini config
GEMINI_MODEL = os.getenv('GEMINI_MODEL', 'gemini-1.5-flash')
GEMINI_MAX_TOKENS = int(os.getenv('GEMINI_MAX_TOKENS', '1000'))
GEMINI_TEMPERATURE = float(os.getenv('GEMINI_TEMPERATURE', '0.7'))

# Check API keys
openai_api_key = os.getenv('OPENAI_API_KEY')
gemini_api_key = os.getenv('GEMINI_API_KEY')

if not openai_api_key:
    raise EnvironmentError("❌ OPENAI_API_KEY is missing from environment variables")

if not gemini_api_key:
    raise EnvironmentError("❌ GEMINI_API_KEY is missing from environment variables")

# Create OpenAI client
client = OpenAI(api_key=openai_api_key)

# Configure Gemini
genai.configure(api_key=gemini_api_key)


# Legacy helper removed: verb suggestions are now provided by Bloom taxonomy via
# the /get_bloom_verbs route. Keep this file for other helpers.


def generate_ai_response(prompt):
    """
    Generate AI response using OpenAI GPT
    """
    try:
        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": "Tu es un expert en formation et en pédagogie spécialisé dans la génération de contenus pédagogiques selon les règles ABC Learning Design."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=OPENAI_MAX_TOKENS * 2,  # Allow more tokens for contenus generation
            temperature=OPENAI_TEMPERATURE
        )
        
        return response.choices[0].message.content
        
    except Exception as e:
        print(f"Error generating AI response: {e}")
        return None


def generate_gemini_response(prompt):
    """
    Generate AI response using Google Gemini Flash 2.5
    """
    try:
        model = genai.GenerativeModel(GEMINI_MODEL)
        
        system_prompt = "Tu es un expert en formation et en pédagogie spécialisé dans la génération de contenus pédagogiques selon les règles ABC Learning Design."
        
        response = model.generate_content(
            f"{system_prompt}\n\n{prompt}",
            generation_config=genai.types.GenerationConfig(
                max_output_tokens=GEMINI_MAX_TOKENS * 2,  # Allow more tokens for contenus generation
                temperature=GEMINI_TEMPERATURE
            )
        )
        
        return response.text
        
    except Exception as e:
        print(f"Error generating Gemini response: {e}")
        return None
