"""
main.py
John Leeds
6/19/2022

Driver program to create images for my algorithm trainer
"""
import json
import three_image_gen
import two_image_gen

def main():
    two = ["CLL", "EG-1", "EG-2", "Ortega_OLL", "Ortega_PBL"]
    for algSet in two:
        states = {}
        with open(f"input/two/{algSet}.json") as f:
            states = json.load(f)
        for alg in states:
            print(f"states[alg]: {states[alg]} - alg: {alg} - algSet: {algSet}")
            gen = two_image_gen.ImageGen(states[alg][0], alg.replace(" ", "_"), algSet)
            gen.make()

    # three = ["CMLL", "COLL", "ELL", "OLL", "PLL", "WVLS_FL", "WVLS", "ZBLL_AS",
    #            "ZBLL_H", "ZBLL_L", "ZBLL_Pi", "ZBLL_S", "ZBLL_T", "ZBLL_U"]
    # for algSet in three:
    #     states = {}
    #     with open(f"input/three/{algSet}.json") as f:
    #         states = json.load(f)
    #     for alg in states:
    #         print(f"states[alg]: {states[alg]} - alg: {alg} - algSet: {algSet}")
    #         gen = three_image_gen.ImageGen(states[alg][0], alg.replace(" ", "_"), algSet)
    #         gen.make()

if __name__ == "__main__":
    main()