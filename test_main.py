import pytest
from main import identify_zerolist, find_sublist, main


class TestIdentifyZerolist:
    """Tests for the identify_zerolist function"""
    
    def test_positive_sum(self):
        """Test with positive sum"""
        assert identify_zerolist((1, 2, 3)) is False
    
    def test_negative_sum(self):
        """Test with negative sum"""
        assert identify_zerolist((-1, -2, -3)) is False
    
    def test_zero_sum(self):
        """Test with zero sum"""
        assert identify_zerolist((1, -1, 2, -2)) is True
    
    def test_single_zero(self):
        """Test with single zero"""
        assert identify_zerolist((0,)) is True
    
    def test_empty_tuple(self):
        """Test with empty tuple"""
        assert identify_zerolist(()) is True
    
    def test_large_numbers(self):
        """Test with large numbers"""
        assert identify_zerolist((1000000, -1000000)) is True
        assert identify_zerolist((1000000, 1000000)) is False
    
    def test_type_error_list(self):
        """Test raises TypeError for list input"""
        with pytest.raises(TypeError, match="Error: Input must be of type tuple"):
            identify_zerolist.__wrapped__([1, 2, 3])
    
    def test_type_error_string(self):
        """Test raises TypeError for string input"""
        with pytest.raises(TypeError, match="Error: Input must be of type tuple"):
            identify_zerolist.__wrapped__("123")
    
    def test_type_error_none(self):
        """Test raises TypeError for None input"""
        with pytest.raises(TypeError, match="Error: Input must be of type tuple"):
            identify_zerolist.__wrapped__(None)


class TestFindSublist:
    """Tests for the find_sublist function"""
    
    def test_entire_list_sums_to_zero(self):
        """Test when the entire list sums to zero"""
        result = find_sublist((3, 5, -8))
        assert result == (3, 5, -8)
        assert sum(result) == 0
    
    def test_partial_zero_sum(self):
        """Test finding partial zero-sum sublist"""
        result = find_sublist((1, 3, 5, -8))
        assert result == (3, 5, -8)
        assert sum(result) == 0
    
    def test_no_zero_sum_exists(self):
        """Test when no zero-sum sublist exists"""
        result = find_sublist((1, 2, 3))
        assert result == ()
    
    def test_single_zero_element(self):
        """Test with single zero element"""
        result = find_sublist((1, 0, 2))
        assert result == (0,)
        assert sum(result) == 0
    
    def test_empty_tuple(self):
        """Test with empty tuple"""
        result = find_sublist(())
        assert result == ()
    
    def test_all_zeros(self):
        """Test with all zeros"""
        result = find_sublist((0, 0, 0))
        assert result == (0, 0, 0)
        assert sum(result) == 0
    
    def test_alternating_pattern(self):
        """Test with alternating positive/negative"""
        result = find_sublist((1, -1, 2, -2))
        assert result == (1, -1, 2, -2)
        assert sum(result) == 0
    
    def test_zero_at_start(self):
        """Test with zero at the beginning"""
        result = find_sublist((0, 1, 2))
        assert result == (0,)
        assert sum(result) == 0
    
    def test_zero_at_end(self):
        """Test with zero at the end"""
        result = find_sublist((1, 2, 0))
        assert result == (0,)
        assert sum(result) == 0
    
    def test_multiple_zero_sum_sublists(self):
        """Test with multiple possible zero-sum sublists"""
        # Both (2, -2) and (3, -3) sum to zero
        result = find_sublist((1, 2, -2, 3, -3))
        assert sum(result) == 0
        assert len(result) > 0
    
    def test_complex_case(self):
        """Test with complex case from main example"""
        result = find_sublist((3, 5, -8, 3, -3))
        assert sum(result) == 0
        assert len(result) > 0
    
    def test_single_element_positive(self):
        """Test with single positive element"""
        result = find_sublist((5,))
        assert result == ()
    
    def test_single_element_negative(self):
        """Test with single negative element"""
        result = find_sublist((-5,))
        assert result == ()
    
    def test_two_element_sum_zero(self):
        """Test with two elements that sum to zero"""
        result = find_sublist((7, -7))
        assert result == (7, -7)
        assert sum(result) == 0
    
    def test_two_element_no_sum_zero(self):
        """Test with two elements that don't sum to zero"""
        result = find_sublist((3, 5))
        assert result == ()
    
    def test_large_numbers(self):
        """Test with large numbers"""
        result = find_sublist((1000000, -1000000, 999999))
        assert result == (1000000, -1000000)
        assert sum(result) == 0
    
    def test_type_error_list(self):
        """Test raises TypeError for list input"""
        with pytest.raises(TypeError, match="Error: Input must be of type tuple"):
            find_sublist.__wrapped__([1, 2, 3])
    
    def test_type_error_string(self):
        """Test raises TypeError for string input"""
        with pytest.raises(TypeError, match="Error: Input must be of type tuple"):
            find_sublist.__wrapped__("123")


class TestEdgeCases:
    """Tests for edge cases and boundary conditions"""
    
    def test_very_long_sequence(self):
        """Test with longer sequence"""
        # Create a sequence that sums to zero
        long_tuple = tuple(range(-5, 6))  # -5, -4, ..., 4, 5 sums to 0
        result = find_sublist(long_tuple)
        assert result == long_tuple
        assert sum(result) == 0
    
    def test_repeated_elements(self):
        """Test with repeated elements"""
        result = find_sublist((2, 2, -2, -2))
        assert result == (2, 2, -2, -2)
        assert sum(result) == 0
    
    def test_negative_numbers_only(self):
        """Test with only negative numbers"""
        result = find_sublist((-1, -2, -3))
        assert result == ()
    
    def test_positive_numbers_only(self):
        """Test with only positive numbers"""
        result = find_sublist((1, 2, 3))
        assert result == ()
    
    def test_mixed_with_zero_in_middle(self):
        """Test with zero in the middle"""
        result = find_sublist((1, 2, 0, 3, 4))
        assert result == (0,)
        assert sum(result) == 0
    
    def test_symmetric_sequence(self):
        """Test with symmetric sequence"""
        result = find_sublist((1, 2, 3, -3, -2, -1))
        assert result == (1, 2, 3, -3, -2, -1)
        assert sum(result) == 0


class TestAlgorithmProperties:
    """Tests for algorithm correctness properties"""
    
    @pytest.mark.parametrize("test_input", [
        (1, -1),
        (3, 5, -8),
        (1, 2, -3),
        (0,),
        (1, -1, 2, -2),
        (-5, 2, 3),
        (10, -5, -5),
        (1, 0, -1),
        (4, -2, -2),
    ])
    def test_result_always_sums_to_zero_if_nonempty(self, test_input):
        """Test that non-empty results always sum to zero"""
        result = find_sublist(test_input)
        if len(result) > 0:
            assert sum(result) == 0, f"Result {result} from input {test_input} should sum to 0"
    
    def test_deterministic_results(self):
        """Test that algorithm produces consistent results"""
        test_input = (1, 2, -3, 0, 1)
        
        # Run multiple times and ensure consistent results
        results = [find_sublist(test_input) for _ in range(5)]
        assert all(result == results[0] for result in results)
    
    def test_empty_result_when_no_solution(self):
        """Test that empty tuple is returned when no zero-sum sublist exists"""
        no_solution_cases = [
            (1, 2, 3),
            (5, 10, 15),
            (-1, -2, -3),
            (1,),
            (100,),
        ]
        
        for case in no_solution_cases:
            result = find_sublist(case)
            assert result == (), f"Expected empty tuple for {case}, got {result}"


class TestMainFunction:
    """Tests for the main demonstration function"""
    
    def test_main_runs_without_error(self, capsys):
        """Test that main() runs without errors"""
        main()
        captured = capsys.readouterr()
        
        # Check that it produces expected output
        assert "Zero-Sum Sublist Finder" in captured.out
        assert "Input:" in captured.out
        assert "Longest zero-sum sublist:" in captured.out
    
    def test_main_shows_examples(self, capsys):
        """Test that main() shows the expected examples"""
        main()
        captured = capsys.readouterr()
        
        # Should show both example inputs
        assert "(3, 5, -8, 3, -3)" in captured.out
        assert "(1, 2, -3, 4, -4)" in captured.out


class TestPerformance:
    """Tests for performance and memoization"""
    
    def test_memoization_works(self):
        """Test that memoization improves performance"""
        # Clear cache first
        find_sublist.cache_clear()
        identify_zerolist.cache_clear()
        
        # This should complete quickly due to memoization
        large_input = tuple(range(-10, 11))  # -10 to 10, sums to 0
        result = find_sublist(large_input)
        
        # Should return the full list since it sums to 0
        assert result == large_input
        assert sum(result) == 0
        
        # Check that cache has entries
        assert find_sublist.cache_info().hits > 0 or find_sublist.cache_info().misses > 0
    
    def test_repeated_calls_use_cache(self):
        """Test that repeated calls use cached results"""
        find_sublist.cache_clear()
        
        test_input = (1, 2, -3, 0)
        
        # First call
        result1 = find_sublist(test_input)
        cache_info_1 = find_sublist.cache_info()
        
        # Second call with same input
        result2 = find_sublist(test_input)
        cache_info_2 = find_sublist.cache_info()
        
        # Results should be identical
        assert result1 == result2
        
        # Cache hits should have increased
        assert cache_info_2.hits > cache_info_1.hits
