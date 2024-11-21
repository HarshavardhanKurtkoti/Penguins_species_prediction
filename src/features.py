import pandas as pd

def encode_input_features(input_features):

    """
    Encodes categorical features in the input data (e.g., island, sex).
    Returns the encoded input data.
    """

    input_df = pd.DataFrame(input_features, index=[0])
    
    encoded_input = pd.get_dummies(input_df, columns=['island', 'sex'])
    return encoded_input
