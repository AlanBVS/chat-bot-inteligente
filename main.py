import os
import google.generativeai as genai

# Definição do modelo e chave da API
MODEL = genai.GenerativeModel("gemini-2.0-flash")
API_KEY = os.getenv('GEMINI_API_KEY') # Utilizei chave de ambiente
QTDE_PERGUNTAS = 3  # Número de perguntas permitidas

def obter_resposta(pergunta, modelo):
    """Consulta a API e retorna uma resposta baseadano contexto"""
    resposta = modelo.generate_content(
        f"Você é um assistente especializado em trânsito e comandos da polícia. "
        f"Responda perguntas sobre leis de trânsito, segurança viária e ações policiais.\nPergunta: {pergunta}"
    )
    return resposta.text

def main():
    """Executa o fluxo do chatbot."""
    genai.configure(api_key=API_KEY)
    
    print("Bem-vindo ao Chatbot Inteligente!")
    
    print(f"Ótimo! Você pode fazer até {QTDE_PERGUNTAS} perguntas.")

    perguntas = []
    respostas = []

    for i in range(QTDE_PERGUNTAS):
        pergunta = input(f"Pergunta {i+1}: ")  # Usuário faz uma pergunta
        perguntas.append(pergunta)
        resposta = obter_resposta(pergunta, MODEL)  # Obtém a resposta
        respostas.append(resposta)
        print(f"Resposta: {resposta}\n")  # Exibe a resposta

    # Gera um resumo das interações
    resumo = MODEL.generate_content(
        "Resuma as seguintes perguntas e respostas de forma clara, objetiva e bem humorada:\n" +
        "\n".join([f"Pergunta: {p}\nResposta: {r}" for p, r in zip(perguntas, respostas)])
    )

    print("\nResumo das respostas:")
    print(resumo.text)  # Exibe o resumo

if __name__ == "__main__":
    main()  # Inicia o chatbot