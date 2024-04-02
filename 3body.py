# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def main_3body2():
    #test
    import numpy as np
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D

    # Konstante
    # G = 6.67408e-11  # N-m2/kg2
    G = 1
    # m_nd = 1.989e+30  # kg #mass of the sun
    # r_nd = 5.326e+12  # m #distance between stars in Alpha Centauri
    # v_nd = 30000  # m/s #relative velocity of earth around the sun

    # m1 = 1
    # m2 = 1
    # m3 = 1

    # v10 = np.array([0.0, 0.0, 1.5])
    # v20 = np.array([0.0, 1.5, 0.0])
    # v30 = np.array([0.0, 0.0, -1.5])
    #
    # r10 = np.array([-3.0, 0.0, 0.0])
    # r20 = np.array([0.0, 0.0, 0.0])
    # r30 = np.array([3.0, 0.0, 0.0])

    m1 = 1
    m2 = 1
    m3 = 1
    G = 1

    r10 = np.array([-0.97000436, 0.24308753, 0.0])
    r20 = np.array([0.0, 0.0, 0.0])
    r30 = np.array([0.97000436, -0.24308753, 0.0])

    v10 = np.array([0.4662036850, 0.4323657300, 0.0])
    v20 = np.array([-0.93240737, -0.86473146, 0.0])
    v30 = np.array([0.4662036850, 0.4323657300, 0.5])

    r11 = np.copy(r10)
    v11 = np.copy(v10)
    r21 = np.copy(r20)
    v21 = np.copy(v20)
    r31 = np.copy(r30)
    v31 = np.copy(v30)
    dt = 0.00001

    steps = 2000
    t = 0

    r1xs = [r10[0]]
    r1ys = [r10[1]]
    r1zs = [r10[2]]
    r2xs = [r20[0]]
    r2ys = [r20[1]]
    r2zs = [r20[2]]
    r3xs = [r30[0]]
    r3ys = [r30[1]]
    r3zs = [r30[2]]
    ts = [t]

    fig = plt.figure()
    ax = Axes3D(fig)

    i = 0
    while i < steps:
        r12 = np.copy(r11) + v11 * dt
        v12 = np.copy(v11) + (G * (((m3 * (r31 - r11)) / (np.linalg.norm(r31 - r11) ** 3)) + (
                    (m2 * (r21 - r11)) / (np.linalg.norm(r21 - r11) ** 3)))) * dt

        r22 = np.copy(r21) + v21 * dt
        v22 = np.copy(v21) + (G * (((m3 * (r31 - r21)) / (np.linalg.norm(r31 - r21) ** 3)) + (
                    (m1 * (r11 - r21)) / (np.linalg.norm(r11 - r21) ** 3)))) * dt

        r32 = np.copy(r31) + v31 * dt
        v32 = np.copy(v31) + (G * (((m1 * (r11 - r31)) / (np.linalg.norm(r11 - r31) ** 3)) + (
                    (m2 * (r21 - r31)) / (np.linalg.norm(r21 - r31) ** 3)))) * dt

        r11 = np.copy(r12)
        v11 = np.copy(v12)
        r21 = np.copy(r22)
        v21 = np.copy(v22)
        r31 = np.copy(r32)
        v31 = np.copy(v32)
        t = t + dt
        r1xs.append(r11[0])
        r1ys.append(r11[1])
        r1zs.append(r11[2])
        r2xs.append(r21[0])
        r2ys.append(r21[1])
        r2zs.append(r21[2])
        r3xs.append(r31[0])
        r3ys.append(r31[1])
        r3zs.append(r31[2])

        ts.append(t)
        print(t)
        i += 1

    ax.plot(r1xs, r1ys, r1zs)
    ax.plot(r2xs, r2ys, r2zs)
    ax.plot(r3xs, r3ys, r3zs)
    plt.show()
    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main_3body2()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
