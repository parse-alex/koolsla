#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pandas

from os.path import join, dirname

# Parent directory
parent_directory_path = dirname(__file__)
# Path to dish dataset
dish_dataset_path = join(parent_directory_path,
                          'dataset/dish.csv')

def import_data(dataset_path):
    dish_dataset = pandas.read_csv(dataset_path)
    return dish_dataset

def split_data(dish_dataset):
    # Get dish names
    dish_names = dish_dataset[['name']].values.flatten().tolist()
    # Pack and return the split data
    return {'names': dish_names}

def validate_dish_id(dish_id):
    # Check whether the id is valid
    if not (isinstance(dish_id, int) and dish_id >= 0 and dish_id <= 424508):
        print('Input is not a valid integer between [0, 424508]')
        return False
    return True
