vector<vector<int> > Solution::anagrams(const vector<string> &A) {
    vector<vector<int>> result;
    map<string, vector<int>> hashmap;
    
    for (int i = 0; i<A.size();i++) {
        string str=A[i];
        sort(str.begin(), str.end());
        hashmap[str].push_back(i+1);
    }
    map<string, vector<int>>::iterator itr;
     itr=hashmap.begin();
    while (itr!=hashmap.end())
       {
        result.push_back(itr->second);
        itr++;
       }
    return result;
}