def removeDuplicates(nums):
        if len(nums)==0:
            return 0
        j=0
        for i in range(1,len(nums)):
            if nums[i]!=nums[j]:
                j=j+1
                nums[j]=nums[i]
        return j+1

removeDuplicate=removeDuplicates([1,1,2])
print(removeDuplicate)