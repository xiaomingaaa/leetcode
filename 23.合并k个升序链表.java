/*
 * @lc app=leetcode.cn id=23 lang=java
 *
 * [23] 合并K个升序链表
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution1 {
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length==0){return null;}
        // ListNode temp=lists[0];
        // for(int i=1;i<lists.length;i++){
        //     if(lists[i]==null){
        //         continue;
        //     }
        //     temp=mergeTwoLists(temp, lists[i]);
        // }
        // return temp;
        return merge(lists, 0, lists.length-1);
    }
    public ListNode merge(ListNode[] lists, int left, int right){
        if(left==right){return lists[left];}
        int mid=left+(right-left)/2;
        ListNode l1=merge(lists, left, mid);
        ListNode l2=merge(lists, mid+1, right);
        //跟归并排序一个道理
        return mergeTwoLists(l1, l2);
    }
    public ListNode mergeTwoLists(ListNode l1, ListNode l2){
        if(l1==null){
            return l2;
        }
        if(l2==null){
            return l1;
        }
        else if(l1.val<l2.val){
            l1.next=mergeTwoLists(l1.next, l2);
            return l1;
        }else{
            l2.next=mergeTwoLists(l1, l2.next);
            return l2;
        }
    }
}
// @lc code=end

