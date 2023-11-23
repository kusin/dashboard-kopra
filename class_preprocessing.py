# library normalization min-max
from sklearn.preprocessing import MinMaxScaler

# define class preprocessing
class preprocessing:

    # method normalization
    @staticmethod
    def normalization(df):
        # min-max algorithm
        scaler = MinMaxScaler()
        scaled = scaler.fit_transform(df) 
        return scaled