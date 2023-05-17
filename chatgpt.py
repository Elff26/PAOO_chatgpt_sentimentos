import openai

def encontrar_sentimento(
    OPENAI_API_KEY,
    frase
):
    openai.api_key = OPENAI_API_KEY
    
    pergunta_padrao = "Qual sentimento da seguinte frase? Responda com apenas uma palavra: Positivo, Negativo ou Neutro. Eis a frase: "
    
    prompt = f'{pergunta_padrao}{frase}'

    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=prompt
    )

    return response.choices[0].text.strip()