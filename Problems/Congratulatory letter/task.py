def congratulations(*names):
    print("Happy New Year! Take care of yourself and your loved ones!")
    print("For:")
    for name in names:
        print("\n".join(single_name for single_name in name.split()))