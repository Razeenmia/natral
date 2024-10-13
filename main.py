 Args:
      num: The number to be checked.

  Returns:
      A string indicating whether the number is positive, negative, or zero.
  """

  if num >0:
    return "The number is positive."
  elif num < 0:
    return "The number is negative (medical terminology might use different terms)."  # Clarification for negative values
  else:
    return "The number is zero."

# Get user input for the number
number = float(input("Enter a number: "))

# Call the function to determine the type of number
result = check_number(number)

# Print the result
print(result)