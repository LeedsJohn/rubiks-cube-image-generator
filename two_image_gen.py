"""
two_image_gen.py
John Leeds
7/5/2022
Class used to generate images of a 2x2 Rubik's cube
"""
import os
from PIL import Image, ImageDraw

OUTPUT_PATH = "./output/two/"
CHAR_TO_COLOR = {"w": (255, 255, 255),
                 "y": (255, 213, 0),
                 "g": (0, 155, 72),
                 "b": (0, 70, 173),
                 "r": (183, 18, 52),
                 "o": (255, 88, 0),
                 "x": (127, 127, 127)}

class ImageGen:
    def __init__(self, cubestring, fName, algset):
        self.cubestring = cubestring
        self.fName = fName
        self.algset = algset
        self.img = Image.new('RGBA', (81, 81), (255, 0, 0, 0))
    
    def make(self):
        self._convertState()
        self._drawSquares()
        self._drawLines()
        if not os.path.isdir(f"{OUTPUT_PATH}{self.algset}"):
            os.mkdir(f"{OUTPUT_PATH}{self.algset}")
        self.img.save(f"{OUTPUT_PATH}{self.algset}/{self.fName}.png")
        self.img.close()

    def _drawSquares(self):
        """
        _drawSquares
        Reads from the cubestring to create the representation of the Rubik's cube
           10 11 
        9  0  1  4
        8  2  3  5
           7  6
           14 13 12
        """
        bigStartCoords = [11, 41]
        squares = []
        for y in bigStartCoords:
            for x in bigStartCoords:
                squares.append((x, y, x+28, y+28))
        right = [(71, y, 79, y+28) for y in (11, 41)]
        front = [(x, 71, x-28, 79) for x in (69, 39)]
        left = [(1, y, 9, y+28) for y in (41, 11)]
        back = [(x, 1, x+28, 9) for x in (11, 41)]
        squares += right + front + left + back
        draw = ImageDraw.Draw(self.img)
        for square, c in zip(squares, self.cubestring):
            draw.rectangle(square, fill=CHAR_TO_COLOR[c])

    def _drawLines(self):
        """
        _drawLines
        Draws the borders of the Rubik's Cube
        """
        startCoords = (0, 10, 40, 70, 80)
        draw = ImageDraw.Draw(self.img)
        for coord in startCoords:
            draw.line((0, coord, 80, coord), fill=(20, 20, 20))
            draw.line((coord, 0, coord, 80), fill=(20, 20, 20))
        

        squares = [(0, 0, 9, 9), (71, 71, 80, 80), (0, 71, 9, 80), (71, 0, 80, 9)]
        for square in squares:
            draw.rectangle(square, fill=(0, 0, 0, 0))

    def _convertState(self):
        """
        _convertState
        Converts the cubestring used in the two phase solver
        to one that this program can generate an image of
        """
        
        self.cubestring = self.cubestring[:4] + self._reverse(self.cubestring[4:6]) + \
        self._reverse(self.cubestring[8:10]) + self._reverse(self.cubestring[16:18]) + \
        self._reverse(self.cubestring[20:22])
        newString = ""
        translations = {"U": "y", "D": "w", "R": "r", "L": "o", "F": "b", "B": "g"}
        for i, char in enumerate(self.cubestring):
            newString += translations[char]
        self.cubestring = newString
        print(self.cubestring)
    
    def _reverse(self, str):
        return str[::-1]