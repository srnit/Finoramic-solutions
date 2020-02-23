int Solution::braces(string A) {
    stack<char>st;
    for(int i=0;A[i]!='\0';i++)
    {
       
        if (A[i] == '(' || A[i] == '+' || A[i] == '*' || A[i] == '-' || A[i] == '/')
            st.push(A[i]);
        else if(A[i]==')')
        {
            
            if(st.empty())
                    return 1;
             if(st.top()=='(')
                return 1;
            else
            {
                    while(!st.empty()&& st.top()!='(')
                        st.pop();
                    st.pop();
                
            }
        }
        
    }
    return 0;
}
