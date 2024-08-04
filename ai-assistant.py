import wave
import sounddevice as sd
import os
import subprocess
import time

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
MODEL = "meta-llama-3.1-8b-instruct-abliterated.Q4_K_M.gguf"
CONTEXT_LENGTH = 2048
THREADS = 4

def get_response(prompt):
    command = [
        f"{BASE_PATH}/llama.cpp/llama-cli",
        "-m", f"{BASE_PATH}/llama.cpp/models/{MODEL}",
        "-p", f"{prompt}", "-c", f"{CONTEXT_LENGTH}",
        "-n", "8", "-t", f"{THREADS}"
    ]

    response = subprocess.run(command, capture_output=True, text=True)
    return response.stdout.strip()
    
def main():
    print(get_response("What is 9 + 10?"))

if __name__ == "__main__":
    main()
