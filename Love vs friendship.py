def words_to_marks(s):
    return sum('_abcdefghijklmnopqrstuvwxyz'.index(i) for i in s)