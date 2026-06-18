class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str=""
        for s in strs:
            #store the length, a seperator(#) , and the string itself
            encoded_str+=str(len(s))+"#"+s
        return encoded_str

    def decode(self, s: str) -> List[str]:

        decoded_str=[]
        i=0
        while i< len(s):
            j=i
            while s[j] != '#':
                j+=1 #go up to #
            #save the length as ghe number before "#" is the length
            length= int(s[i:j])

            # etract string based on that length
            start=j+1
            end= start+length
            decoded_str.append(s[start:end])

            #move the pointer to the start of the next length prefix
            i=end



        return decoded_str

            

