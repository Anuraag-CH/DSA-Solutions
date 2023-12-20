def kDistinctChars(k, s):
    # Write your code here
    # Return an integer value

    distinct_dict = {}
    l = 0
    max_string = 0

    for r in range(0,len(s)):

        if s[r] in distinct_dict :

            distinct_dict[s[r]] +=1
            max_string = max(max_string,r-l+1)
        

        elif len(distinct_dict) +1 <= k:
            
            distinct_dict[s[r]] =1
            max_string = max(max_string,r-l+1)

        else:
            while len(distinct_dict) + 1 > k :
                distinct_dict[s[l]] -=1
                if  distinct_dict[s[l]] == 0 :
                    distinct_dict.pop(s[l])
                l+=1
            distinct_dict[s[r]] =1
            max_string = max(max_string,r-l+1)



    return max_string
