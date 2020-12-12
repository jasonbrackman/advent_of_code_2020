"""
PPM
    P3
    # The P3 means colors are in ASCII, then 3 columns and 2 rows,
    # then 255 for max color, then RGB triplets
    3 2
    255
    255   0   0
"""

import random


class Image:

    multiplier = 1

    def __init__(self, rows, cols):
        self.COLOURS = {
            "white": "255 255 255\n",
            "black": "0 0 0\n",
            "blackish": "20 20 20\n",
            "green": "0 255 0\n",
            "blue": "0 0 255\n",
            "purple": "128 0 128\n",
            "random": f"{random.randint(0, 255)} {random.randint(0, 255)} {random.randint(0, 255)}\n",
            "red": "255 0 0\n",
        }

        self.rows = rows * self.multiplier
        self.cols = cols * self.multiplier
        print(f"Image Size: {self.rows}, {self.cols}")
        # Default background is near black
        self.pixels = [[self.COLOURS["blackish"]] * self.cols for _ in range(self.rows)]

    def pixel(self, row, col, colour: str):
        if colour not in self.COLOURS:
            raise ValueError(
                f"Expected one of the following colours: {self.COLOURS.keys()}"
            )
        # print(row, col, colour)
        r = row * self.multiplier
        c = col * self.multiplier
        if r < self.rows and c < self.cols:
            for incr in range(self.multiplier):
                for incc in range(self.multiplier):
                    self.pixels[r + incr][c + incc] = self.COLOURS[colour]

    def paint(self, file_path: str, fmt: str):
        """

        :param file_path:
        :param fmt: Expecting P3 (ascii) or P6 (binary)
        :return:
        """
        ascii_colours = fmt
        max_colour = 255

        header = f"{ascii_colours} {self.cols} {self.rows} {max_colour} "

        mode = "wt" if fmt == "P3" else "wb+"
        with open(file_path, mode) as handle:
            handle.write(header.encode())
            for lines in self.pixels:
                if fmt == "P6":
                    for line in lines:
                        r, g, b = line.split()
                        r, g, b = int(r), int(g), int(b)
                        handle.write(
                            r.to_bytes(2, "big") + g.to_bytes(2, "big") + b.to_bytes(2, "big")
                        )
                else:
                    handle.writelines(lines)


def example():
    test_data = [
        "###########",
        "#0.1.....2#",
        "#.#######.#",
        "#4.......3#",
        "###########",
    ]
    rows = len(test_data)
    cols = len(test_data[0])
    for index in range(3):
        canvas = Image(rows, cols)
        for r in range(rows):
            for c in range(cols):
                colour = "black"
                if test_data[r][c] == ".":
                    colour = "white"
                elif test_data[r][c].isdigit():
                    colour = "random"
                canvas.pixel(r, c, colour)
        canvas.paint(f"./images/test_{index:02}.ppm")


def generic_out(data, index):
    rows = len(data)
    cols = len(data[0])

    canvas = Image(rows, cols)
    for r in range(rows):
        for c in range(cols):
            colour = "black"
            if data[r][c] == ".":
                colour = "white"
            elif data[r][c] == "L":
                colour = "blue"
            elif data[r][c] == "#":
                colour = "red"
            canvas.pixel(r, c, colour)
    canvas.paint(f"./images/test_{index:02}.ppm", fmt="P6")

if __name__ == "__main__":
    example()
