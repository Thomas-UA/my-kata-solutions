import random
random.seed()
def generate_color_rgb():
    rgb = ''
    x_r= '0123456789CDEF'
    for i in range(6):
        a = random.randint(0, len(x_r)-1)
        rgb += rgb.join(x_r[a])
    return '#'+rgb