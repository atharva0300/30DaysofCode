ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        //Creating a new linkedlist for us to stored the digits.
        ListNode* ans=new ListNode(-1);
        ListNode* temp_ans=ans;
        
        //Creating 2 temps to traverse the 2 given linked lists.
        ListNode* temp1=l1;
        ListNode* temp2=l2;
        int carry=0;
        int digit;
        int value1;
        int value2;
        
        //Traversing till both of them become NULL and carry!=0 (for cases like 999)
        while(temp1!=NULL || temp2!=NULL || carry!=0){
            int sum=0;
            //This 'if' statements ensure that value will be taken 0 if any one temp has already reached NULL.
            if(temp1!=NULL){
                sum+=temp1->val;
                temp1=temp1->next;
            }
            if(temp2!=NULL){
                sum+=temp2->val;
                temp2=temp2->next;
            }
            
            //Basic addition and math.
            int value=sum + carry;
            carry=value/10;
            digit=value%10;
            
            //Add the digit to the tail.
            ListNode* tobeadded=new ListNode(digit);
            temp_ans->next=tobeadded;
            temp_ans=temp_ans->next;
            
        }
        
        //Delete the reduntant node and return ans.
        ListNode* tobedeleted=ans;
        ans=ans->next;
        delete tobedeleted;
        return ans;
    }