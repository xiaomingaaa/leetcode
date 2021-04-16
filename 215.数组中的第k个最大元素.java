import java.util.PriorityQueue;

/*
 * @lc app=leetcode.cn id=215 lang=java
 *
 * [215] 数组中的第K个最大元素
 */

// @lc code=start
class Solution {
    public int findKthLargest(int[] nums, int k) {
        // nums=sort2(nums);
        // if(k>0&&k<=nums.length){
        //     return nums[k-1];
        // }
        // return -1;
        PriorityQueue<Integer> popNums=new PriorityQueue<>();
        int n=nums.length;
        for(int i=0;i<n;i++){
            popNums.offer(nums[i]);
            if(popNums.size()>k){
                popNums.poll();
            }
        }
        return popNums.peek();
        // int heapsize=nums.length;
        // buildMaxHeap(nums, heapsize);
        // for(int i=nums.length-1;i>=nums.length-k+1;i--){
        //     swap(nums, 0, i);
        //     --heapsize;
        //     maxHeapify(nums, 0, heapsize);

        // }
        // return nums[0];
    }

    
    private void buildMaxHeap(int[] a, int heapsize){
        for(int i=heapsize/2;i>=0;i--){
            maxHeapify(a, i, heapsize);
        }
    }

    private void maxHeapify(int[] a, int i, int heapsize){
        int l=i*2+1,r=i*2+2,largest=i;
        if(l<heapsize&&a[l]>a[largest]){
            largest=l;
        }
        if(r<heapsize&&a[r]>a[largest]){
            largest=r;
        }
        if(largest!=i){
            swap(a, i, largest);
            maxHeapify(a, largest, heapsize);
        }
    }
    private void swap(int[] a, int i, int j){
        int temp=a[i];
        a[i]=a[j];
        a[j]=temp;
    }
    /**
     * 插入排序获得有序数组再选取
     * @param nums
     * @return
     */
    private int[] sort(int[] nums){
        for (int i=0;i<nums.length;i++){
            for(int j=i;j<nums.length;j++){
                if(nums[i]<nums[j]){
                    int temp=nums[j];
                    nums[j]=nums[i];
                    nums[i]=temp;
                }
            }
        }
        return nums;
    }
    /**
     * 使用归并排序获得有序数组后选取元素，o(nlogn),树的深度未logn
     * @param nums
     * @return
     */
    private int[] sort2(int[] nums){
        return merge_sort(nums, 0, nums.length-1);
    }
    private int[] merge_sort(int[] nums,int left,int right){
        int mid=(left+right)/2;
        int[] mergeArray=new int[nums.length];
        if (left<right){
            
            int[] left_=merge_sort(nums, left, mid);
            int[] right_= merge_sort(nums, mid+1, right);
            mergeArray = merge(left_, right_);
        }
        return mergeArray;
    }
    private int[] merge(int[] a, int[] b){
        //引入临时数组
        if(a.length==0){
            return b;
        }
        if(b.length==0){
            return a;
        }
        int[] temp=new int[a.length+b.length];
        int i=0;
        int j=0;
        int t=0;
        while(i<a.length&&j<b.length){
            if(a[i]<b[j]){
                temp[t++]=b[j++];
            }
            else{
                temp[t++]=a[i++];
            }
        }
        while(i<a.length){
            temp[t++]=a[i++];
        }
        while(j<b.length){
            temp[t++]=b[j++];
        }
        return temp;
    }

}
// @lc code=end

