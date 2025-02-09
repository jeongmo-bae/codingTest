package com.leetcode.studyplan.top150.arraynstring;
//https://leetcode.com/problems/rotate-array/?envType=study-plan-v2&envId=top-interview-150

import java.util.Arrays;
public class RotateArray {
    public static void main(String[] args) {
        RotateArray ra = new RotateArray();
        int[] nums2 = {1, 2, 3, 4, 5, 6};
        ra.rotate(nums2, 2);
        System.out.println(Arrays.toString(nums2));

    }

    public void rotate(int[] nums, int k) {
        int n = nums.length;
        for (int iter = 0; iter < k; iter++) {
            int[] numsRotated = new int[n];
            numsRotated[0] = nums[n - 1];
            System.arraycopy(nums,0,numsRotated,1,n-1);
            System.arraycopy(numsRotated,0,nums,0,n);
            System.out.println(Arrays.toString(nums));
        }
    }
}