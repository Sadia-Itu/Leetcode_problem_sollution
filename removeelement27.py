def removeElement(nums, val):
        r=0
        for i in range(0,len(nums)):
            if nums[i]!=val:
                nums[r]=nums[i]
                r=r+1
            
                
        return r

removeelement=removeElement([1,1,2],1)
print(removeelement)