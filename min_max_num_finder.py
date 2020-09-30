
testresult = int(input("Enter a test result: "))
if testresult == -1:
    print("No results input")
    
else:
    minresult = testresult

    maxresult = testresult

    while testresult != -1:
        if testresult < minresult:
            minresult = testresult

        if testresult > maxresult:
            maxresult = testresult


        testresult = int(input("Please enter another test result, or -1 to finish: "))


    print(f"\nMax result is: {maxresult}")

    print(f"Min result is: {minresult}")
