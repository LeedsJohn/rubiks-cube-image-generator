"""
imagegenerator.py
John Leeds
6/19/2022
Class used to generate images of a Rubik's cube
"""
from PIL import Image, ImageDraw

OUTPUT_PATH = "./output/"
CHAR_TO_COLOR = {"w": (255, 255, 255),
                 "y": (255, 255, 0),
                 "g": (30, 255, 30),
                 "b": (0, 0, 255),
                 "r": (255, 0, 0),
                 "o": (255, 165, 0),
                 "x": (127, 127, 127)}

IGNORED_COLORS = {"OLL": "gwrbo", "WVLS": "gwrbo", "WVLS_FL": "gwrbo"}
IGNORED_INDICES = {"CMLL": [1, 3, 4, 5, 7, 10, 13, 16, 19], "COLL": [10, 13, 16, 19]}
KEEP_INDICES = {"WVLS": [5, 8, 10, 11, 12], "WVLS_FL": [5, 8, 10, 11, 12]}

class ImageGen:
    def __init__(self, cubestring, fName, algset):
        self.cubestring = cubestring
        self.fName = fName
        self.algset = algset
        self.img = Image.new('RGB', (81, 81))
    
    def make(self):
        self._convertState()
        self._drawSquares()
        self._drawLines()
        self.img.save(f"{OUTPUT_PATH}{self.fName}.png")
        self.img.close()

    def _drawSquares(self):
        """
        _drawSquares
        Reads from the cubestring to create the representation of the Rubik's cube
           18 19 20
        17 0  1  2  9
        16 3  4  5  10
        15 6  7  8  11
           14 13 12
        """
        bigStartCoords = [11, 31, 51]
        squares = []
        for y in bigStartCoords:
            for x in bigStartCoords:
                squares.append((x, y, x+18, y+18))
        right = [(71, y, 79, y+18) for y in (11, 31, 51)]
        front = [(x, 71, x-18, 79) for x in (69, 49, 29)]
        left = [(1, y, 9, y+18) for y in (11, 31, 51)]
        back = [(x, 1, x+18, 9) for x in (11, 31, 51)]
        squares += right + front + left + back
        draw = ImageDraw.Draw(self.img)
        for square, c in zip(squares, self.cubestring):
            draw.rectangle(square, fill=CHAR_TO_COLOR[c])

    def _drawLines(self):
        """
        _drawLines
        Draws the borders of the Rubik's Cube
        """
        startCoords = (0, 10, 30, 50, 70, 80)
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
        
        self.cubestring = self.cubestring[:12] + self.cubestring[18:21] + self.cubestring[30:33] + self.cubestring[39:42]
        newString = ""
        translations = {"U": "w", "D": "y", "R": "r", "L": "o", "F": "g", "B": "b"}
        for i, char in enumerate(self.cubestring):
            c = translations[char]
            if self.algset in IGNORED_COLORS and c in IGNORED_COLORS[self.algset]:
                if self.algset in KEEP_INDICES and i in KEEP_INDICES[self.algset]:
                    newString += c
                else:
                    newString += "x"
            elif self.algset in IGNORED_INDICES and i in IGNORED_INDICES[self.algset]:
                newString += "x"
            else:
                newString += c
        self.cubestring = newString