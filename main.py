import uvicorn
from fastapi import FastAPI, File, UploadFile, HTTPException

app = FastAPI()


def validate_format(data):
    login_attempts = data.split('\n')

    for attempt in login_attempts:
        if attempt and len(attempt) != 3:
            raise HTTPException(status_code=400, detail="Formato incorrecto del archivo. Cada intento debe tener 3 caracteres.")


@app.put("/api/upload/keylog.txt")
async def upload_keylog(file: bytes = File(...)):
    content_str = file.decode('ascii')

    validate_format(content_str)

    login_attempts = content_str.split('\n')
    unique_chars = set()
    char_frequency = {}

    for attempt in login_attempts:
        if not attempt:
            continue

        characters = list(attempt)

        unique_chars.update(characters)

        for char in characters:
            char_frequency[char] = char_frequency.get(char, 0) + 1

    sorted_chars = sorted(unique_chars, key=lambda x: char_frequency[x])
    secret_code = ''.join(sorted_chars)

    print("Código secreto más corto:", secret_code)

    return {"secret_code": secret_code}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
