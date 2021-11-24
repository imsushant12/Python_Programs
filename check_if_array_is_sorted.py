def check_sorted(a):
    strictly_increasing = True
    for i in range(len(a)-1):
        if a[i] < a[i+1]:
            pass
        elif a[i] <= a[i+1]:
            strictly_increasing = False
        else:
            print("Not Sorted!")
            break

    if strictly_increasing == False:
        print("Sorted but not Strictly Increasing!")
    else:
        print("Strictly Increasing!")


if __name__ == "__main__":
    a = [1, 2, 4, 4, 10]
    check_sorted(a)
