package swap_nodes_in_pairs;

/**
 * Created by liujia on 16/3/11.
 * <p>
 * https://leetcode.com/problems/swap-nodes-in-pairs/
 * <p>
 * Given a linked list, swap every two adjacent nodes and return its head.
 * For example,
 * Given 1->2->3->4, you should return the list as 2->1->4->3.
 * Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
 * Subscribe to see which companies asked this question
 */

import static org.junit.Assert.assertEquals;

import org.junit.Assert;
import org.junit.Test;

public class Solution {
    //Definition for singly-linked list.
    class ListNode {
        int val;
        ListNode next;

        ListNode(int x) {
            val = x;
        }
    }

    public ListNode swapPairs(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }

        ListNode pangu, c, pre;

        pangu = new ListNode(0);
        pangu.next = head;
        c = head;
        pre = pangu;

        while (c != null && c.next != null) {
            pre.next = c.next;
            pre = c;

            ListNode a = c.next.next;
            c.next.next = c;
            c = a;
            pre.next = c;
        }

        return pangu.next;
    }

    @Test
    public void testswapPairs() {
        StringBuffer sb;
        ListNode head, c;

        // 0
        head = new ListNode(0);
        sb = new StringBuffer();
        head = swapPairs(head);
        c = head;
        while (c != null) {
            sb.append(c.val);
            c = c.next;
        }
        Assert.assertEquals("0", new String(sb));

        // 0 1
        head = new ListNode(0);
        head.next = new ListNode(1);
        sb = new StringBuffer();
        head = swapPairs(head);
        c = head;
        while (c != null) {
            sb.append(c.val);
            c = c.next;
        }
        Assert.assertEquals("10", new String(sb));


        // 0 1 2
        head = new ListNode(0);
        head.next = new ListNode(1);
        head.next.next = new ListNode(2);
        sb = new StringBuffer();
        head = swapPairs(head);
        c = head;
        while (c != null) {
            sb.append(c.val);
            c = c.next;
        }
        Assert.assertEquals("102", new String(sb));

        // 0 1 2 3 4 5
        head = new ListNode(0);
        c = head;
        for (int i = 1; i <= 5; i++) {
            c.next = new ListNode(i);
            c = c.next;
        }


        sb = new StringBuffer();
        c = head;
        while (c != null) {
            sb.append(c.val);
            c = c.next;
        }
        Assert.assertEquals("012345", new String(sb));

        sb = new StringBuffer();
        head = swapPairs(head);
        c = head;
        while (c != null) {
            sb.append(c.val);
            c = c.next;
        }
        Assert.assertEquals("103254", new String(sb));
    }
}
