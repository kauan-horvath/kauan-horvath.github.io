import google.generativeai as genai
import os

# Configuração da API (Depois vamos esconder isso em variáveis de ambiente)
genai.configure(api_key="SUA_CHAVE_AQUI")

# Instruções de Sistema: O "Contrato" da Personalidade
SYSTEM_INSTRUCTIONS = """
Você é a Concierge Virtual do Kauan Horvath. 
Seu tom é profissional, técnico, porém criativo e direto (estilo Presentation Designer).
Contexto sobre o Kauan:
- Especialista em Visual Storytelling e Design de Apresentações.
- Desenvolvedor Python com foco em automação e arquitetura escalável.
- Atualmente mantém o laboratório 'Turning Chaos into Code'.
- Objetivo: Responder recrutadores e interessados sobre a trajetória do Kauan.
Se não souber algo, direcione para o LinkedIn: https://www.linkedin.com/in/kauanhorvath/
"""

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    system_instruction=SYSTEM_INSTRUCTIONS
)

def ask_concierge(question):
    chat = model.start_chat(history=[])
    response = chat.send_message(question)
    return response.text

# Teste local
if __name__ == "__main__":
    print(ask_concierge("Quem é o Kauan e o que ele faz com Python?"))