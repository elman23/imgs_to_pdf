from fpdf import FPDF
from typing import List
from Image import Image


class Converter:
    imgs: List[Image]
    out_file: str

    def __init__(self) -> None:
        self.imgs = []

    def add_img(self, img_path: str, orientation: str = "portrait"):
        img = Image(img_path, orientation)
        self.imgs.append(img)

    def add_out_file(self, out_file: str):
        self.out_file = out_file

    def convert_images(self) -> None:
        if len(self.imgs) == 0:
            return
        if self.out_file == None:
            return
        print([img.file_name for img in self.imgs])
        print(self.out_file)
        pdf = FPDF()
        for img in self.imgs:
            pdf.add_page(orientation=img.orientation)
            # pdf.add_page()
            print(
                f"Adding {img.file_name} with orientation {img.orientation}...")
            pdf.image(img.file_name, h=pdf.eph,
                      w=pdf.epw, keep_aspect_ratio=True)
        pdf.output(self.out_file)
        print(f"Saved to {self.out_file}")
