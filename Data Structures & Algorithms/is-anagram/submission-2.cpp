class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.length() != t.length()){
            return false;
        }

        unordered_map<char, int> myMap;
        
        for(int i = 0; i < s.size(); i++){
            myMap[s[i]]++;
            myMap[t[i]]--;
        }

        for(int i = 0; i < s.size(); i++){
            if(myMap[s[i]] != 0){
                return false;
            }
        }

        return true;


       

    }
};
