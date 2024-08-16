import math


class Real:
    def __init__(self, diagonal, ratio):
        self.diognal = diagonal
        self.ratio = ratio
        self.width_ratio, self.height_ratio = ratio.split(":")

    def __str__(self):
        width, height, area = self.get_dimensions()
        return f"{area:.2f} inches squared"

    def get_dimensions(self):
        diagonal_ratio = math.sqrt(
            int(self.width_ratio) ** 2 + int(self.height_ratio) ** 2
        )
        width = (self.diognal / diagonal_ratio) * int(self.width_ratio)
        height = (self.diognal / diagonal_ratio) * int(self.height_ratio)
        area = width * height
        return width, height, area


if __name__ == "__main__":
    real = Real(55, "16:9")
    print(real)
