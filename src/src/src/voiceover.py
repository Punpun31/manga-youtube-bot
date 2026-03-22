import subprocess
import os

def generate_voiceover(script_text, output_path="output/voiceover.wav"):
    os.makedirs("output", exist_ok=True)
    
    script_file = "output/script.txt"
    with open(script_file, "w", encoding="utf-8") as f:
        f.write(script_text)

    subprocess.run([
        "python", "-m", "kokoro",
        "--text-file", script_file,
        "--output", output_path,
        "--lang", "en-us",
        "--voice", "af_heart"
    ], check=True)

    return output_path

if __name__ == "__main__":
    test_script = "Welcome back to the channel! Today we are reviewing the latest chapter of One Piece!"
    path = generate_voiceover(test_script)
    print(f"Voiceover saved to: {path}")
