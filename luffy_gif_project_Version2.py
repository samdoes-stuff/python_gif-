import imageio
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import requests
from io import BytesIO


gif_url = "https://tenor.com/view/one-piece-excited-lets-watch-one-piece-gif-3375125404087240671"  # Example Luffy GIF
response = requests.get(gif_url)
gif_bytes = BytesIO(response.content)


reader = imageio.get_reader(gif_bytes)
frames = []
duration = reader.get_meta_data()['duration']

for i, frame in enumerate(reader):
    pil_frame = Image.fromarray(frame)

    draw = ImageDraw.Draw(pil_frame)
    font = ImageFont.truetype("arial.ttf", 28) if "arial.ttf" in ImageFont.getfontnames() else ImageFont.load_default()
    draw.text((10, 10), f"LUFFY MODE {i+1}", fill=(255, 255, 0), font=font)


    if i % 2 == 1:
        enhancer = ImageEnhance.Contrast(pil_frame)
        pil_frame = enhancer.enhance(2.0)


    border_size = 6
    bordered = Image.new("RGBA", (pil_frame.width + 2*border_size, pil_frame.height + 2*border_size), (255,0,0,255))
    bordered.paste(pil_frame, (border_size, border_size))
    pil_frame = bordered

    frames.append(pil_frame)

output_path = "luffy_advanced.gif"
frames[0].save(
    output_path, save_all=True, append_images=frames[1:],
    duration=duration, loop=0, disposal=2
)

print(f"Advanced Luffy GIF saved as {output_path}!")
