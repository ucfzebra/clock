import random


class RGBColor:
    def __init__(self, text_color=(0,0,0), bg_color=(255,255,255), outline_color=(0,0,0)):
        self.text_color = text_color
        self.bg_color = bg_color
        self.outline_color = outline_color
    
    def set_text_color(self, red, green, blue):
        self.text_color = (red, green, blue)
    
    def set_bg_color(self, red, green, blue):
        self.bg_color = (red, green, blue)
    
    def set_outline_color(self, red, green, blue):
        self.outline_color = (red, green, blue)
    
    def randomize(self):
        self.text_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.bg_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.outline_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        
    def set_predefined_color(self, color):
        if color == "red":
            self.text_color = (255, 0, 0)
        elif color == "green":
            self.text_color = (0, 255, 0)
        elif color == "blue":
            self.text_color = (0, 0, 255)
        elif color == "yellow":
            self.text_color = (255, 255, 0)
        elif color == "purple":
            self.text_color = (255, 0, 255)
        elif color == "turquoise":
            self.text_color = (0, 255, 255)
    
    def get_text_color(self):
        return self.text_color
    
    def get_bg_color(self):
        return self.bg_color
    
    def get_outline_color(self):
        return self.outline_color
    
    def is_legible(self):
       ## Calculate relative luminance of text color and background color
       ## For more information: https://www.w3.org/TR/WCAG20/#relativeluminancedef
        def calculate_luminance(color):
            r, g, b = color
            r_linear = r / 255.0 if r <= 10 else ((r / 255.0) ** 2.2)
            g_linear = g / 255.0 if g <= 10 else ((g / 255.0) ** 2.2)
            b_linear = b / 255.0 if b <= 10 else ((b / 255.0) ** 2.2)
            return 0.2126 * r_linear + 0.7152 * g_linear + 0.0722 * b_linear
        
        ## Compare relative luminance of text color and background color
        text_luminance = calculate_luminance(self.text_color)
        bg_luminance = calculate_luminance(self.bg_color)
        if text_luminance > bg_luminance:
            contrast_ratio = (text_luminance + 0.05) / (bg_luminance + 0.05)
        else:
            contrast_ratio = (bg_luminance + 0.05) / (text_luminance + 0.05)
        
        ##Check if contrast ratio is sufficient for legibility
        return contrast_ratio