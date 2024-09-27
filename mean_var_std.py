import numpy as np

def calculate(list):
    if(len(list)!=9):
        raise ValueError("List must contain nine numbers.")
    l=np.array(list)
    rows_mean=[l[[0,1,2]].mean(),l[[3,4,5]].mean(),l[[6,7,8]].mean()]
    cols_mean=[l[[0,3,6]].mean(),l[[1,4,7]].mean(),l[[2,5,8]].mean()]

    rows_var=[l[[0,1,2]].var(),l[[3,4,5]].var(),l[[6,7,8]].var()]
    cols_var=[l[[0,3,6]].var(),l[[1,4,7]].var(),l[[2,5,8]].var()]

    rows_std=[l[[0,1,2]].std(),l[[3,4,5]].std(),l[[6,7,8]].std()]
    cols_std=[l[[0,3,6]].std(),l[[1,4,7]].std(),l[[2,5,8]].std()]

    rows_max=[l[[0,1,2]].max(),l[[3,4,5]].max(),l[[6,7,8]].max()]
    cols_max=[l[[0,3,6]].max(),l[[1,4,7]].max(),l[[2,5,8]].max()]

    rows_min=[l[[0,1,2]].min(),l[[3,4,5]].min(),l[[6,7,8]].min()]
    cols_min=[l[[0,3,6]].min(),l[[1,4,7]].min(),l[[2,5,8]].min()]

    rows_sum=[l[[0,1,2]].sum(),l[[3,4,5]].sum(),l[[6,7,8]].sum()]
    cols_sum=[l[[0,3,6]].sum(),l[[1,4,7]].sum(),l[[2,5,8]].sum()]

    return {
        'mean':[cols_mean,rows_mean,l.mean()],
        'variance':[cols_var,rows_var,l.var()],
        "standard deviation":[cols_std,rows_std,l.std()],
        'max':[cols_max,rows_max,l.max()],
        'min':[cols_min,rows_min,l.min()],
        'sum':[cols_sum,rows_sum,l.sum()]
    }