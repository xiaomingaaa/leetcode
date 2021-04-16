import java.util.Deque;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

import javax.swing.tree.TreeNode;

/*
 * @lc app=leetcode.cn id=103 lang=java
 *
 * [103] 二叉树的锯齿形层序遍历
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        if(root==null){return null;}
        List<List<Integer>> result=new ArrayList<List<Integer>>();
        Queue<TreeNode> q=new LinkedList<TreeNode>();
        q.add(root);
        boolean isLeft=true;
        while(!q.isEmpty()){
            int size=q.size();
            Deque<Integer> r=new LinkedList<Integer>();
            for(int i=0;i<size;i++){
                TreeNode temp=q.poll();
                if(isLeft){
                    r.offerLast(temp.val);
                }
                else{
                    r.offerFirst(temp.val);
                }
                if(temp.left!=null){
                    q.add(temp.left);
                }
                if(temp.right!=null){
                    q.add(temp.right);
                }
            }
            result.add(new LinkedList<Integer>(r));
            isLeft=!isLeft;
        }
        return result;
    }
}
// @lc code=end

