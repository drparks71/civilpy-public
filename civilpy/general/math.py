import civilpy

np = civilpy.np
solver = civilpy.sym
inf = civilpy.sym.oo


def equation_solver(eq, variable):
    return civilpy.sym.solve(eq, variable)


def arithmetic_growth(p_0, r, t):
    p_t = p_0 + (t * r)
    return p_t


def geometric_growth(p_0, r, t):
    p_t = p_0 * ((1 + r) ** t)
    return p_t


def find_global_extrema_order_3(f, x1, x2, variable='x'):
    x = civilpy.sym.symbols(variable)
    f_prime = civilpy.sym.diff(f)
    f_prime2 = civilpy.sym.diff(f_prime)
    print(f'The first derivative is \n{f_prime} the second is \n {f_prime2}\n')

    try:
        root1, root2 = civilpy.sym.solvers.solve(f_prime, x)
        print(f'The first root is {root1}, the second root is {root2}\n')

        for root in [root1, root2]:
            if f_prime2.subs(x, root) > 0:
                print(f'{root} is a local minimum\n')
            elif f_prime2.subs(x, root) < 0:
                print(f'{root} is a local maximum\n')

        inf_point = civilpy.sym.solvers.solve(f_prime2, x)
        print(f'The inflection point is {inf_point[0]}\n')

        check_values = {x1: 0, x2: 0, root1: 0, root2: 0}

        for key, value in check_values.items():
            check_values[key] = f.subs(x, key)

        global_min = min(check_values.keys(), key=(lambda k: check_values[k]))
        global_max = max(check_values.keys(), key=(lambda k: check_values[k]))

        print(f'Global min: {global_min}, Global max: {global_max}')

        return global_min, global_max, check_values
    except ValueError:
        print('This function only works on 3rd order equations')

