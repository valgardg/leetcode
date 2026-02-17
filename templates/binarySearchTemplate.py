def binary_search(array) -> int:
    # 1. Define the condition function to check if a value satisfies the requirement
    def condition(value) -> bool:
        pass

    # 2. Initialize the boundary variables `left` and `right`
    #    Ensure the boundaries cover all possible elements in the search space
    left, right = min(search_space), max(search_space)
    
    # Use 'left < right' to ensure the loop terminates with left == right
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            # mid is a potential answer, but we might find a smaller one to the left
            right = mid
        else:
            # mid does not satisfy the condition, so the answer must be to the right
            left = mid + 1
            
    # 3. Decide the return value
    #    After the loop, 'left' (or 'right') is the minimal k satisfying the condition
    return left
