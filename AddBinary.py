class Solution:
  def addBinary(self, a, b):

    binNumA = int(a, 2)
    binNumB = int(b, 2)

    Sum = binNumA + binNumB

    binSum = bin(Sum)

    return binSum[2:]

result = Solution()
print(result.addBinary("1010", "1011"))

