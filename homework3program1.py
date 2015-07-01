def bunnyEars(bunnies):
  if (bunnies == 0):
    return 0
  else:
    if (bunnies % 2 == 0):
      return 3 + bunnyEars (bunnies - 1)
    else:
      return 2 + bunnyEars (bunnies - 1)
