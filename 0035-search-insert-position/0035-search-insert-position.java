class Solution {
    public int searchInsert(int[] nums, int target) {
        int n = nums.length;
        int s=0,m,e=n-1;
    
      
        while(s<=e)
        {
              m =(e+s)/2;
           if(nums[m]<target)
           {
              s=m+1;
           }
           else if(nums[m]==target)
           {
            return m;
           }
           else{
            e = m-1;
           }
            }
            
            return s;
        }
      
     
    
    }
