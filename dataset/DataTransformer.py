from PIL.Image import Resampling
from datasets import load_dataset
import os
from tqdm import tqdm
from PIL import Image


class DataTransformer:

    def __init__(self, output_folder):
        self.output_folder = output_folder
        self.dataset = load_dataset("huggan/pokemon", split="train")

    def transform_data(self):
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

        for i, example in enumerate(tqdm(self.dataset, desc="Processing images", unit="images")):
            img = example["image"]

            resized_img = self._resize_image(img)

            filename = os.path.join(self.output_folder, f"pokemon_{i}.png")
            resized_img.save(filename)

    def _resize_image(self, img):
        max_dim = max(img.width, img.height)

        square_img = Image.new("RGB", (max_dim, max_dim), (255, 255, 255))

        offset = ((max_dim - img.width) // 2, (max_dim - img.height) // 2)
        square_img.paste(img, offset)

        resized_img = square_img.resize((256, 256), Resampling.LANCZOS)

        return resized_img



