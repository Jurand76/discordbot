from secrets import getStabilityToken

import requests

MY_APIKEY = getStabilityToken()

def parse_command(command):
    # Sprawdzenie obecności argumentów
    if "--" in command:
        # Podziel na prompt i argumenty
        parts = command.split("--", 1)
        prompt = parts[0].strip()
        arguments = f"--{parts[1].strip()}"  # Przywracamy "--" do argumentów
    else:
        prompt = command.strip()
        arguments = ""

    # Przetwarzanie argumentów
    args_dict = {}
    if arguments:
        args = arguments.split("--")  # Rozdzielamy kolejne argumenty
        for arg in args:
            if arg.strip().startswith("ar "):
                args_dict["aspect_ratio"] = arg.strip()[3:].strip()

    return prompt, args_dict

def generate_image(prompt):
    prompt, args = parse_command(prompt)
    aspect_ratio = args.get("aspect_ratio", "1:1")  # Domyślne aspect ratio to 1:1

    print(f"Prompt: {prompt}")
    print(f"Aspect ratio: {aspect_ratio}")

    response = requests.post(
        f"https://api.stability.ai/v2beta/stable-image/generate/ultra",
        headers={
            "authorization": f"Bearer {MY_APIKEY}",
            "accept": "image/*"
        },
        files={"none": ''},
        data={
            "prompt": prompt,
            "aspect_ratio": aspect_ratio,
            "output_format": "webp",
        },
    )

    if response.status_code == 200:
        filename = "./image.webp"
        with open(filename, 'wb') as file:
            file.write(response.content)
        return filename
    else:
        return f"Error {str(response.json())}"


def generate_upscaled_image():
    response = requests.post(
        f"https://api.stability.ai/v2beta/stable-image/upscale/conservative",
        headers={
            "authorization": f"Bearer {MY_APIKEY}",
            "accept": "image/*"
        },
        files={
            "image": open("./image.webp", "rb"),
        },
        data={
            "prompt": "a flower",
            "output_format": "webp",
        },
    )

    if response.status_code == 200:
        filename = "./upscaled.webp"
        with open(filename, 'wb') as file:
            file.write(response.content)
            return filename
    else:
        return "Error"