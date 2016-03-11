package merge_two_sorted_lists;
/**
 * Created by liujia on 16/3/11.
 * <p>
 * https://leetcode.com/problems/merge-two-sorted-lists/
 * <p>
 * Merge two sorted linked lists and return it as a new list.
 * The new list should be made by splicing together the nodes of the first two lists.
 */

import org.junit.Assert;
import org.junit.Test;

import java.util.List;
import java.util.Random;

public class Solution {

    class ListNode {
        int val;
        ListNode next;

        ListNode(int x) {
            val = x;
        }
    }


    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if (l1 == null) {
            return l2;
        }
        if (l2 == null) {
            return l1;
        }

        ListNode pre;
        if (l1.val < l2.val) {
            pre = new ListNode(l1.val - 1);
        } else {
            pre = new ListNode(l2.val - 1);
        }
        pre.next = l1;
        l1 = pre;

        ListNode temp;
        while (l1 != null && l2 != null) {
            while (l1.next != null && l2 != null && l1.next.val < l2.val) {
                l1 = l1.next;
            }
            temp = l1.next;
            l1.next = l2;
            l1 = temp;
            if (l1 == null) {
                break;
            }

            while (l2.next != null && l1 != null && l2.next.val < l1.val) {
                l2 = l2.next;
            }
            temp = l2.next;
            l2.next = l1;
            l2 = temp;
            if (l2 == null) {
                break;
            }
        }
        return pre.next;
    }

    @Test
    public void testmergeTwoLists() {
        StringBuffer sb;
        ListNode list1, list2, c;

        // 0
        // null
        list1 = new ListNode(0);
        sb = new StringBuffer();
        c = mergeTwoLists(list1, null);
        while (c != null) {
            sb.append(c.val);
            c = c.next;
        }
        Assert.assertEquals("0", new String(sb));

        // null
        // 0
        list1 = new ListNode(0);
        sb = new StringBuffer();
        c = mergeTwoLists(null, list1);
        while (c != null) {
            sb.append(c.val);
            c = c.next;
        }
        Assert.assertEquals("0", new String(sb));

        // 0
        // 0
        list1 = new ListNode(0);
        list2 = new ListNode(0);
        sb = new StringBuffer();
        c = mergeTwoLists(list1, list2);
        while (c != null) {
            sb.append(c.val);
            c = c.next;
        }
        Assert.assertEquals("00", new String(sb));

        // 3 5 7
        // 2 4 6 8
        list1 = new ListNode(3);
        list1.next = new ListNode(5);
        list1.next.next = new ListNode(7);
        list2 = new ListNode(2);
        list2.next = new ListNode(4);
        list2.next.next = new ListNode(6);
        list2.next.next.next = new ListNode(8);

        sb = new StringBuffer();
        c = mergeTwoLists(list1, list2);
        while (c != null) {
            sb.append(c.val);
            c = c.next;
        }
        Assert.assertEquals("2345678", new String(sb));

        // 1 3 5 7
        // 2 4 6 8
        list1 = new ListNode(1);
        list1.next = new ListNode(3);
        list1.next.next = new ListNode(5);
        list1.next.next.next = new ListNode(7);
        list2 = new ListNode(2);
        list2.next = new ListNode(4);
        list2.next.next = new ListNode(6);
        list2.next.next.next = new ListNode(8);

        sb = new StringBuffer();
        c = mergeTwoLists(list1, list2);
        while (c != null) {
            sb.append(c.val);
            c = c.next;
        }
        Assert.assertEquals("12345678", new String(sb));

        // 1 3 5 7
        // 2 8
        list1 = new ListNode(1);
        list1.next = new ListNode(3);
        list1.next.next = new ListNode(5);
        list1.next.next.next = new ListNode(7);
        list2 = new ListNode(2);
        list2.next = new ListNode(8);

        sb = new StringBuffer();
        c = mergeTwoLists(list1, list2);
        while (c != null) {
            sb.append(c.val);
            c = c.next;
        }
        Assert.assertEquals("123578", new String(sb));


        // 1 3 5 7
        // 0 2 8
        list1 = new ListNode(1);
        list1.next = new ListNode(3);
        list1.next.next = new ListNode(5);
        list1.next.next.next = new ListNode(7);
        list2 = new ListNode(0);
        list2.next = new ListNode(2);
        list2.next.next = new ListNode(8);

        sb = new StringBuffer();
        c = mergeTwoLists(list1, list2);
        while (c != null) {
            sb.append(c.val);
            c = c.next;
        }
        Assert.assertEquals("0123578", new String(sb));


        // 1 2 3
        // 4 5
        list1 = new ListNode(1);
        list1.next = new ListNode(2);
        list1.next.next = new ListNode(3);
        list2 = new ListNode(4);
        list2.next = new ListNode(5);

        sb = new StringBuffer();
        c = mergeTwoLists(list1, list2);
        while (c != null) {
            sb.append(c.val);
            c = c.next;
        }
        Assert.assertEquals("12345", new String(sb));
    }
}
