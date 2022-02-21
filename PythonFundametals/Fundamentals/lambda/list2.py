def mylist (nums):
    myl_list = 2000000
    for x in nums:
        if x < myl_list:
            myl_list = x

    return myl_list

print (mylist([1,2, - 8]))
