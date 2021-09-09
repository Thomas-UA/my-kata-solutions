def multiple(x):
    return 'Bang' if x%3==0 and x%5!=0 else 'Boom' if x%3!=0 and x%5==0 else 'BangBoom' \
        if x%3==0 and x%5==0 else 'Miss'