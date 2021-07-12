def middle_me(N, X, Y):
    if N%2==0:
        return Y*int(N/2) + X + Y*int(N/2)
    else:
        return X