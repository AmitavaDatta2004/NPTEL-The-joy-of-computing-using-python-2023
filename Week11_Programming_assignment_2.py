def rotate(nums, k):
  """
  Rotates a list `nums` by `k` positions in a clockwise direction.

  Args:
      nums: The list to be rotated.
      k: The number of positions to rotate the list.
  """
  n = len(nums)
  k = k % n
  nums[:] = nums[-k:] + nums[:-k]

def get_list_from_user():
  """
  Prompts the user to enter a comma-separated list of integers and converts it to a list.
  """
  while True:
    try:
      list_str = input("")
      return [int(num) for num in list_str.split(",")]
    except ValueError:
      print("")

def list_to_string(nums):
  """
  Converts a list of integers to a comma-separated string.
  """
  return ','.join(map(str, nums))

nums = get_list_from_user()
k = int(input(""))

rotate(nums, k)
rotated_list_str = list_to_string(nums)
print("", rotated_list_str,end="")
