import os
import soundfile as sf
from kokoro import KPipeline

def generate_voiceover(script_text, output_path="voiceover.wav"):
    os.makedirs("output", exist_ok=True)
    output_path = "output/" + output_path

    pipeline = KPipeline(lang_code="a")
    samples = []
    for _, _, audio in pipeline(script_text, voice="af_heart"):
        samples.extend(audio.tolist())

    sf.write(output_path, samples, 24000)
    return output_path
