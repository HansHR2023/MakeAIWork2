
# tijd en delta tijd
t = 0
dt = 0.01


# define car
F_motor = 800
mass = 600
a = F_motor / mass
v = 0
x = 0

running = True

while running:
    t = t + dt

    dv = a * dt
    v = v + dv

    dx = v * dt
    x = x + dx

    print(t)
    # print(v)
    # print(x)

    if x >= 100:
        break
        # running = False

# accelereren = versnelling F = m * a
