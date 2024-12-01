import requests
import json

# Definir la configuración de la API
API_URL = "http://127.0.0.1:5000/v1/completions"
HEADERS = {"Content-Type": "application/json"}

def prompt_user_for_story_details():
    # Obtener detalles del promp desde input del usuario
    details = {}
    details["main_character"] = input("Enter the name of the main character: ")
    details["secondary_character"] = input("Enter the name of the secondary character: ")
    details["place"] = input("Where does the story take place? ")
    details["action"] = input("What's the main action of the story? ")
    return details

def get_settings():
    # Ajustes avanzados como creatividad y longitud
    try:
        temperature = float(input("Set creativity level (0.0 to 1.0, default 0.7): ") or 0.7)
        max_tokens = int(input("Set max tokens for the story (default 200): ") or 200)
        top_p = float(input("Set nucleus sampling value (0.0 to 1.0, default 1.0): ") or 1.0)

    except ValueError:
        print("Invalid input, using defaults.")
        temperature = 0.7
        max_tokens = 200
        top_p = 1.0
    return temperature, max_tokens, top_p

def format_story_prompt(details):
    # Crear texto para el prompt
    return (
            f"Write a detailed and engaging story where the main character is named {details['main_character']}, "
            f"the secondary character is {details['secondary_character']}, the setting is {details['place']}, "
            f"and the main action is {details['action']}. "
            f"Make the story creative, emotional, and well-structured with a clear beginning, middle, and end. "
            f"Avoid using bullet points or numbered lists."
    )

def fetch_story_from_api(prompt, max_tokens, temperature, top_p):
    # Solicitud a la API con los parámetros obtenidos
    payload = {
        "prompt": prompt,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "top_p": top_p,
    }

    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload, verify=False)
        response.raise_for_status()
        story_data = response.json()
        return story_data.get("choices", [{}])[0].get("text", "").strip()
    except requests.exceptions.RequestException as e:
        return f"Error connecting to the API: {e}"
    except KeyError:
        return "Unexpected response format."

def remove_repetitions(text):
    # Elimina frases repetidas
    sentences = text.split(". ")
    seen = set()
    filtered_sentences = []
    for sentence in sentences:
        if sentence not in seen:
            filtered_sentences.append(sentence)
            seen.add(sentence)
    return ". ".join(filtered_sentences)


def main():
    print("Welcome to the Story Creator!")
    print("Provide the details for your story.\n")

    while True:
        # Obtener detalles de la historia y ajustes del usuario
        story_details = prompt_user_for_story_details()
        temperature, max_tokens, top_p = get_settings()

        # Crear el prompt y obtener la historia
        story_prompt = format_story_prompt(story_details)
        generated_story = fetch_story_from_api(story_prompt, max_tokens, temperature, top_p)

        # Mostrar la historia generada
        print("\nGenerated Story:\n")
        print(generated_story)
        print("\n")

        # Verificar si el usuario desea crear otra historia
        try_again = input("Do you want to create another story? (yes to continue, any key to exit): ").strip().lower()
        if try_again != "yes":
            print("Thank you for using the Story Creator! Goodbye!")
            break

if __name__ == "__main__":
    main()
