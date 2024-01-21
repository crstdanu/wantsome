
def eq1(x, y, z, t): return 4*x + 2*y - 6*z + 2*t
def eq2(x, y, z, t): return x - y + z + 4*t
def eq3(x, y, z, t): return x - 2*y + 5*z - 3*t
def eq4(x, y, z, t): return 5*x + 10*y + 10*z + 5*t


def solve_equations():
    for x in range(-100, 101):
        for y in range(-100, 101):
            for z in range(-100, 101):
                for t in range(-100, 101):
                    if (
                        eq1(x, y, z, t) == 0
                        and eq2(x, y, z, t) == 20
                        and eq3(x, y, z, t) == 3
                        and eq4(x, y, z, t) == 70
                    ):
                        return x, y, z, t


solutions = solve_equations()


if solutions:
    x, y, z, t = solutions
    print("Solution:")
    print(f"x = {x}")
    print(f"y = {y}")
    print(f"z = {z}")
    print(f"t = {t}")
else:
    print("No solution found in the given range.")
