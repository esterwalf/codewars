"""In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

Example
filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]"""
def filter_list(l):
    'return a new list with the strings filtered out'
    return [item for item in l if not isinstance(item, str)]

  """  import codewars_test as unit_testing
    from solution import filter_list

    @unit_testing.describe('Sample tests')
    def sample_tests():
        @unit_testing.it('should work for basic examples')
        def basic_examples():
            unit_testing.assert_equals(filter_list([1, 2, 'a', 'b']), [1, 2], 'For input [1, 2, "a", "b"]')
            unit_testing.assert_equals(filter_list([1, 'a', 'b', 0, 15]), [1, 0, 15], 'Fot input [1, "a", "b", 0, 15]')
            unit_testing.assert_equals(filter_list([1, 2, 'aasf', '1', '123', 123]), [1, 2, 123],
                               'For input [1, 2, "aasf", "1", "123", 123]')"""