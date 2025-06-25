#User function Template for python3

class Solution:
    def medianOf2(self, a, b):
        #code here
        m=len(a)
        n=len(b)
        i=0
        j=0
        m1=-1
        m2=-1
        for k in range((m+n)//2+1):
            m2=m1
            if i!=m and j!=n:
                if a[i]<=b[j]:
                    m1=a[i]
                    i+=1
                else:
                    m1=b[j]
                    j+=1
                
            elif i<m:
                m1=a[i]
                i+=1
            else:
                m1=b[j]
                j+=1
                
        if (m+n)%2 == 1:
            return m1
        return (m1+m2)/2.0