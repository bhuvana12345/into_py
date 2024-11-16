
## assert is key word in python used to boldy should be true always 

from cal import square

def main():
    test_square()

def test_square():
    try: 
        assert square(2) == 4
    except AssertionError:
        print("not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("not 9")

# def test_square(): 
#     if square(2) != 4:
#         print("error in 2")
#     if square(3) != 9:
#         print("error in 3")

if __name__ == "__main__":
    main()
