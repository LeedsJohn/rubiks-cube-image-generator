"""
main.py
John Leeds
6/19/2022

Driver program to create images for my algorithm trainer
"""
import json
import imagegenerator

def main():
    # algSets = ["WVLS"]
    algSets = ["CMLL", "COLL", "ELL", "OLL", "PLL", "WVLS_FL", "WVLS", "ZBLL_AS",
               "ZBLL_H", "ZBLL_L", "ZBLL_Pi", "ZBLL_S", "ZBLL_T", "ZBLL_U"]
    for algSet in algSets:
        states = {}
        with open(f"input/{algSet}.json") as f:
            states = json.load(f)
        for alg in states:
            print(f"states[alg]: {states[alg]} - alg: {alg} - algSet: {algSet}")
            gen = imagegenerator.ImageGen(states[alg][0], alg.replace(" ", "_"), algSet)
            gen.make()

if __name__ == "__main__":
    main()