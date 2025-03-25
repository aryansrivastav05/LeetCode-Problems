class Solution {
    public boolean check(int[] nums) {
        int n = nums.length;
        int count =0;
        if(n==0 || n==1)
        {
            return true;
        }
        for(int i=1;i<n;i++)
        {
             if(nums[i-1]>nums[i])
             {
               count++;
             }}
             if(nums[n-1]>nums[0]){
                count++;
             }
             
        
       
      return (count<=1);
    }
}