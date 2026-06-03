import os
import argparse
from dotenv import load_dotenv
from openai import OpenAI

# Cargar variables de entorno desde el archivo .env en la raíz
load_dotenv()

def main():
    # 1. Verificar y configurar la API Key
    api_key = os.getenv("TOGETHER_API_KEY")
    if not api_key:
        print("❌ Error: No se encontró TOGETHER_API_KEY en el archivo .env")
        print("💡 Asegúrate de haber creado el archivo .env con tu clave de Together.ai")
        return

    # 2. Inicializar el cliente de Together.ai (compatible con la librería de OpenAI)
    client = OpenAI(
        api_key=api_key,
        base_url="https://api.together.xyz/v1",
    )

    # 3. Configurar argumentos de línea de comandos
    parser = argparse.ArgumentParser(description="Asistente de investigación Qwen vía Together.ai")
    parser.add_argument("prompt", type=str, help="La pregunta o instrucción para Qwen")
    parser.add_argument("--model", type=str, default="Qwen/Qwen2.5-72B-Instruct", help="Modelo de Qwen a utilizar")
    parser.add_argument("--system", type=str, default="Eres un asistente de investigación académica experto en economía heterodoxa, ciencia de datos, macroeconomía y metodología rigurosa. Responde de forma estructurada, cita fuentes cuando sea posible y mantén un tono académico.", help="Prompt del sistema para contextualizar")
    
    args = parser.parse_args()

    print(f"🔄 Consultando a {args.model}...\n" + "="*60)

    # 4. Hacer la petición a la API
    try:
        response = client.chat.completions.create(
            model=args.model,
            messages=[
                {"role": "system", "content": args.system},
                {"role": "user", "content": args.prompt}
            ],
            temperature=0.2, # Temperatura baja para garantizar rigor y consistencia académica
            max_tokens=4000,
        )
        print(response.choices[0].message.content)
        print("\n" + "="*60)
    except Exception as e:
        print(f"❌ Error al consultar la API: {e}")

if __name__ == "__main__":
    main()