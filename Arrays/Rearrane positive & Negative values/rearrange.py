def rearrange(lst):

    count = 0
    for i in range(len(lst)):
      if( i < 0):
        count +=1
    k = count % len(lst)
    new_list = lst[-count:] + lst[:-count]

    return new_list

# Solution Two: Pythonic Arrangement
    # get negative and positive list after filter and then merge

    return [i for i in lst if i < 0] + [i for i in lst if i >= 0]

# Solution Three: Using Auxiliary Lists:
 # You should do this:)git