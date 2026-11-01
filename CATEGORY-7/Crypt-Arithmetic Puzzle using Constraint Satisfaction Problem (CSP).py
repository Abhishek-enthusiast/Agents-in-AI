import itertools

def solve_cryptarithmetic():
    letters = ('S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y')
    digits = range(10)

    for perm in itertools.permutations(digits, len(letters)):
        mapping = dict(zip(letters, perm))

        if mapping['S'] == 0 or mapping['M'] == 0:
            continue

        send = mapping['S'] * 1000 + mapping['E'] * 100 + mapping['N'] * 10 + mapping['D']
        more = mapping['M'] * 1000 + mapping['O'] * 100 + mapping['R'] * 10 + mapping['E']
        money = mapping['M'] * 10000 + mapping['O'] * 1000 + mapping['N'] * 100 + mapping['E'] * 10 + mapping['Y']

        if send + more == money:
            return mapping, send, more, money

    return None, None, None, None


if __name__ == "__main__":
    mapping, send, more, money = solve_cryptarithmetic()
    print("Crypt-Arithmetic Solution:")
    print(f"Mapping: {mapping}")
    print(f"{send} + {more} = {money}")
