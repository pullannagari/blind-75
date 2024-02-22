# we use java cause python numbers are not bounded to 32-bits

# class Solution {
#     public int getSum(int a, int b) {
#         // xor should be used when only one of the bits should be 1
#         // we first xor to add the bits which are mutually exclusive
#         // we also add the bits to find where the carryovers are and left shift by 1
#         // we then add the xor result and the shiftleft-and result
#         while (b != 0){
#             int temp = (a & b) << 1;
#             a = a ^ b;
#             b = temp;
#         }
#         return a;
#     }
# }