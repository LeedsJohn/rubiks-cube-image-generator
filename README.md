# rubiks-cube-image-generator
Program to generate topdown images of a Rubik's cube

## Use
In directory "input", create json files for the algorithm sets you want images for - ex: CMLL.json

Inside this json file, the keys should be the algorithm names and the values should be [cubestate], where cubestate is the same cubestate used in Herbert Kociemba's two phase Rubik's cube solver. Certain pieces can also be greyed out - greyed out pieces can be determined by the algorithm set.

This format is used because I already had a program to generate json files in this way - see https://github.com/LeedsJohn/Scramble-Generator

If you are interested in using this project and would like to discuss configuring it for your use, please open an issue on this project, leave your email, and I will do my best to get back to you.

## Dependencies

Pillow==9.1.1

## Example Output
Example OLL:
![OLL example](https://ibb.co/HVJsjYy)
Example ZBLL
![ZBLS example](https://ibb.co/bPd50f8)