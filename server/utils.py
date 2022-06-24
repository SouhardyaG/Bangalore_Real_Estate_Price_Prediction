import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None


# from the ipynb
def get_estimated_price(location, sqft, bhk, balcony, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = balcony
    x[3] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)


def get_location_names():
    return __locations


# to load the artifacts
def load_saved_artifacts():
    print("Loading the saved artifacts...")
    global __data_columns
    global __locations

    with open("./artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    global __model
    with open("./artifacts/Bengaluru_House_Data.pickle", 'rb') as f:
        __model = pickle.load(f)
    print("Artifacts Loaded")


if __name__ == "__main__":
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2, 2))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2, 3))
    print(get_estimated_price('Kalhalli', 1000, 2, 2, 2))  # other location
    print(get_estimated_price('Ejipura', 1000, 2, 2, 3))  # other location
