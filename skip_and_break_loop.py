for i in range (1,10):
    if i == 3:
        print(f"skipping {i} in the inner loop")
        continue
    elif i == 7:
        print(f"Reached {i}, outer loop broken")
        break
    print(i)
