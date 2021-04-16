import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.List;

/*
 * @lc app=leetcode.cn id=46 lang=java
 *
 * [46] 全排列
 */

// @lc code=start
class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> res=new ArrayList<List<Integer>>();
        List<Integer> output=new ArrayList<Integer>();

        for(int i=0;i<nums.length;i++){
            output.add(nums[i]);
        }
        int n=nums.length;
        backtract(n, output, res, 0);
        return res;
    }
    public void backtract(int n, List<Integer> output, List<List<Integer>> res, int first){
        if(first==n){
            res.add(new ArrayList<Integer>(output));
        }
        for(int i=first; i<n;i++){
            Collections.swap(output,first,i);
            backtract(n, output, res, first+1);
            Collections.swap(output, first, i);
        }
    }
}
// @lc code=end

