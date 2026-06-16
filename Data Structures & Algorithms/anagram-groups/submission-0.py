from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_map= defaultdict(list)

        for s in strs:
            count= [0]*26

            for char in s:
                count[ord(char) - ord('a')] +=1
            string_id= tuple(count)

            anagram_map[string_id].append(s)
        return list(anagram_map.values())