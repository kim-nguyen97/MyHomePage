import io
from pathlib import Path

from PIL import Image
from rembg import remove

SOURCE = Path("static/images/7A9026DE-E10C-47FE-BEFF-03B020BBF6D4.jpg")
OUTPUT = Path("static/images/profile.png")

input_data = SOURCE.read_bytes()
output_data = remove(input_data)

output_image = Image.open(io.BytesIO(output_data)).convert("RGBA")
output_image.save(OUTPUT)

print(f"Saved {OUTPUT} ({output_image.size[0]}x{output_image.size[1]})")
