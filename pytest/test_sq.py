
## Using pytest to do try, except and printing all just install it 

from cal import square

def test_square():
    assert square(2) == 4
    assert square(3) == 9  # gives assertion error 
    # for new winow with py file we write code name.py to create one 

    # run like pytest test_sq.py in terminal instead of python test_sq.py 
