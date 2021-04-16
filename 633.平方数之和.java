/*
 * @lc app=leetcode.cn id=633 lang=java
 *
 * [633] 平方数之和
 */

// @lc code=start
class Solution {
    public boolean judgeSquareSum(int c) {
        for(int a=1;a<=Math.sqrt(c);a++){
            int b=c-(int)(a*a);
            if(binary(0, b, b)){
                return true;
            }
        }
        return false;
    }
    private boolean binary(long left, long right, int b){
        if(left==right){
            return false;
        }
        long mid= left+ (left+right)/2;
        if(mid*mid==b){
            return true;
        }
        else if(mid*mid < b){
            return binary(mid+1, right, b);
        }
        else{
            return binary(left, mid-1, b);
        }

    }
}
// @lc code=end

