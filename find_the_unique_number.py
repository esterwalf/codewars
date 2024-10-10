"""There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.

This is the first kata in series:

Find the unique number (this kata)
Find the unique string
Find The Unique"""

def find_uniq(arr):
    def find_uniq(arr):
        # Use a dictionary to count occurrences
        count = {}
        for n in arr:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1

        # Find the unique number
        for n in count:
            if count[n] == 1:
                return n

"""try:
    import codewars_test as test
except:
    pass


@test.describe("Basic Tests")
def f():
    @test.it("Simple tests")
    def _():
        test.assert_equals(find_uniq([ 1, 1, 1, 2, 1, 1 ]), 2)
        test.assert_equals(find_uniq([ 0, 0, 0.55, 0, 0 ]), 0.55)
        test.assert_equals(find_uniq([ 3, 10, 3, 3, 3 ]), 10)"""