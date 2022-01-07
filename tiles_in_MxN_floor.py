# Time Complexity: O(n!)

def place_tiles(n, m):
    # base cases
    if n == m:
        return 2      # as we have 2 ways of placiing tiles
    if n < m:
        return 1

    # Horizontally:
    horizontal_placement = place_tiles(n-1, m)
    # Vertically:
    vertical_placement = place_tiles(n-m, m)

    return horizontal_placement + vertical_placement

if __name__ == "__main__":
    n, m = (3, 3)
    print(place_tiles(n, m))
