def invite_people(n):
    # base cases
    if n == 1:
        return 1
    if n == 2:
        return 2

    single_ways = invite_people(n-1)
    pair_ways = (n-1) * invite_people(n-2)

    return single_ways + pair_ways


if __name__ == "__main__":
    people = 4
    answer = invite_people(people)
    print(answer)
