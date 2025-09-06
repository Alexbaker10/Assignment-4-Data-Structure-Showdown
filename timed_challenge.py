# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!
"""3. Remove Duplicates (Keep Order)
Return the values in the order they first appeared, without duplicates.
Input: ["apple", "banana", "apple", "kiwi", "banana"]
Output: ["apple", "banana", "kiwi"]"""
def remove_duplicate(input_list):
  results = []
  seen = set()
  for item in input_list:
    if item not in seen:
      results.append(item)
      seen.add(item)
  return results
data = ["apple", "banana", "apple", "kiwi", "banana"]
output = remove_duplicate(data)
print(output)
