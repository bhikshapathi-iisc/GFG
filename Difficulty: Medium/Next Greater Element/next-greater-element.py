class Solution:
    def nextLargerElement(self, arr):
        n = len(arr)
        result = [-1] * n
        stack = []  # to store elements for comparison

        # Traverse from right to left
        for i in range(n - 1, -1, -1):
            # Pop smaller or equal elements
            while stack and stack[-1] <= arr[i]:
                stack.pop()

            # If stack not empty, top is next greater
            if stack:
                result[i] = stack[-1]

            # Push current element
            stack.append(arr[i])

        return result
