from rapidocr import RapidOCR

class OCREngine:
    def __init__(self):
        self.engine = RapidOCR()

    def process_image(self, img_path, gen_img_path):
        result = self.engine(img_path, return_word_box=True, return_single_char_box=True)
        result.vis(gen_img_path)
        return result