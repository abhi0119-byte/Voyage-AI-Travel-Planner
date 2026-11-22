
import tomllib
from pathlib import Path
from groq import Groq

secrets_path = Path(".streamlit/secrets.toml")

with open(secrets_path, "rb") as file:
    secrets = tomllib.load(file)

client = Groq(api_key=secrets["GROQ_API_KEY"])

models = client.models.list()

print("AVAILABLE GROQ MODELS:")
for model in models.data:
    print(model.id)
