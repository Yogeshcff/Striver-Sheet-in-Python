if nums1[left]>nums2[right]:
    nums1[left],nums2[right]=nums2[right],nums1[left]
    left-=1
    right+=1
else:
    break