# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

import random
import os
import sys

### functions ###


def create_trait_draw_pool(df) -> list:
    pool = []

    def process_row(row_obj: pd.Series, pool: list) -> None:
        ID = int(row_obj["ID"])
        weight = int(row_obj["weight"])
        pool += [ID] * int(weight)

    df.apply(lambda x: process_row(x, pool), axis=1)
    return pool


def assign_traits(
    n_drivers: int = 12, filename: str = "driver_traits.csv"
) -> None:
    out_str = ""
    # for each driver:
    for i in range(n_drivers):
        out_str += create_driver_trait_string() + "\n"

    with open(filename, "w") as text_file:
        text_file.write(out_str)


def create_driver_trait_string() -> None:
    # roll number of traits to assign
    n_traits = random.sample(number_traits, 1)[0]
    print(f"creating driver with {n_traits} traits ...")
    # draw rolled number of traits
    traits = []
    while len(traits) < n_traits:
        possible_trait = random.sample(draw_pool, 1)[0]
        # if trait is not opposed to exising: add it
        if (not get_opposing(possible_trait) in traits) and (
            not possible_trait in traits
        ):
            traits.append(possible_trait)
    # create trait string
    trait_string = "; ".join(map(str, traits))
    # add driver trait string to output list
    return trait_string


def get_opposing(ID: int) -> int:

    # get entry in table
    opp = config_df[config_df["ID"] == ID]["opposing"]
    # if entry is empty: return -99
    if np.isnan(opp.values[0]) or opp.empty:
        return -99
    # else: return entry
    else:
        return int(opp.values[0])


### sript ###

# manual settings
config_folder = "configs"
input_name = "ids.csv"
number_traits = [0, 1, 2, 3]  # hardcoded for now, could be another config
trait_config_file_path = os.path.join(config_folder, input_name)

# read in config
config_df = pd.read_csv(trait_config_file_path, delimiter=";")
# create pool to draw from
draw_pool = create_trait_draw_pool(config_df)


def main():
    if len(sys.argv) == 3:
        n_drivers = int(sys.argv[1])
        outputfile = sys.argv[2]
        print(
            f"creating traits for {n_drivers} drivers in"
            + f" '{outputfile}' ..."
        )
    else:
        print(
            "to create driver traits please call this module "
            + "with number of drivers and target file name like so: "
            + "'trait_creator.py 23 my_traitfile.csv'"
        )
        sys.exit(0)
    # run trait creation
    print(f"reading trait config from '{config_folder}/{input_name}' ...")

    assign_traits(n_drivers, outputfile)
    print("done.")
    sys.exit(0)


if __name__ == "__main__":
    main()
