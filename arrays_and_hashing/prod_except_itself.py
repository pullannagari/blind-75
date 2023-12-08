class Solution:
    def productExceptSelf(self, nums: list) -> list:
      # takes O(n) time, and O(1) space(not counting the result as additional space)
      if not nums:
        return None
      result = [1]*(len(nums))
      prefix = 1
      for i in range(len(result)):
        result[i] *= prefix
        prefix *= nums[i]
      suffix = 1
      for i in range(len(result)-1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
      return result

      # takes an additional space of O(n)
      # prod_l_h = []
      # prod = 1
      # for n in nums:
      #   prod *= n 
      #   prod_l_h.append(prod)
      # prod_h_l = [1]*len(nums)
      # prod = 1
      # for i in range(len(nums)-1, -1, -1):
      #   prod *= nums[i]
      #   prod_h_l[i] = prod
      # result = []
      # for i in range(len(nums)):
      #   if i == 0:
      #     l_prod = 1
      #   else:
      #     l_prod = prod_l_h[i-1]
      #   if i == len(nums)-1:
      #     r_prod = 1
      #   else:
      #     r_prod = prod_h_l[i+1]
      #   result.append(l_prod*r_prod)
      # return result
        