"""humanYears >= 1
humanYears are whole numbers only
Cat Years
15 cat years for first year
+9 cat years for second year
+4 cat years for each year after that
Dog Years
15 dog years for first year
+9 dog years for second year
+5 dog years for each year after that"""
def human_years_cat_years_dog_years(human_years):
    # Your code here
    return [0,0,0]


"""1
import codewars_test as test
2
from solution import human_years_cat_years_dog_years
3
​
4
@test.describe("Fixed Tests")
5
def fixed_tests():
6
    @test.it("one")
7
    def _():
8
        test.assert_equals(human_years_cat_years_dog_years(1), [1,15,15])
9
    @test.it("two")
10
    def _():
11
        test.assert_equals(human_years_cat_years_dog_years(2), [2,24,24])
12
    @test.it("ten")
13
    def _():
14
        test.asse"""