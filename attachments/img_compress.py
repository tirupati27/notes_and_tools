import os
from PIL import Image

def compress_image(input_path, output_path, quality=60, max_width=None):
    """
    Compress a JPEG image while keeping text readable.
    :param input_path: Original file path
    :param output_path: Compressed file path
    :param quality: JPEG quality (40–70 recommended for text-heavy images)
    :param max_width: Resize width (None = no resize)
    """
    img = Image.open(input_path)

    # Optional resizing (helps reduce size while keeping legible text)
    if max_width is not None and img.width > max_width:
        ratio = max_width / img.width
        new_height = int(img.height * ratio)
        img = img.resize((max_width, new_height), Image.LANCZOS)

    img.save(
        output_path,
        "JPEG",
        optimize=True,
        quality=quality,
        progressive=True
    )

def compress_all_jpgs(quality=60, max_width=None):
    cwd = os.getcwd()
    files = os.listdir(cwd)

    for file in files:
        if file.lower().endswith((".jpg", ".jpeg")):
            input_path = os.path.join(cwd, file)
            output_path = os.path.join(cwd, f"{file}")
            compress_image(input_path, output_path, quality, max_width)
            print(f"Compressed: {file} → {output_path}")

if __name__ == "__main__":
    # Adjust quality:
    # 50–70 keeps text very readable
    #compress_all_jpgs(quality=60, max_width=None)
    compress_all_jpgs(quality=45, max_width=1000)