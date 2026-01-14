import pandas as pd
s = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

def test_dataframe_shape():
    print("DataFrame shape:", s.shape)

if __name__ == "__main__":
    
    test_dataframe_shape()