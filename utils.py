
# Controlling data format whether its class and name
# Returns global list data format
def checkDataFormat(data):
    if data.__class__.__name__ is 'DataFrame':
        return data.values.tolist() , 'dataframe'
    elif data.__class__.__name__ is 'ndarray':
        ll = [len(k) for k in data]
        if max(ll) == max(ll):
            return data.tolist(), 'ndarray'
    elif isinstance(data, list):
        ll = [len(k) for k in data]
        if max(ll) == max(ll):
            return data, 'list'
    else:
        raise ValueError('Unexpected data format, please use nested np.array, pd.DataFrame or nested lists.')



#def check1DArrayFormat(array):

