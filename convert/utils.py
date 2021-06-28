from rembg.bg import remove
import numpy as np
import io
from PIL import Image




def remove_background(input_path,output_path):
    f = np.fromfile(input_path)
    result = remove(f)
    img = Image.open(io.BytesIO(result)).convert("RGBA")
    img.save(output_path)

# remove_background(input_path)