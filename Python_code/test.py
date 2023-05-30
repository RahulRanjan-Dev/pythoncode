
def solution(S):
    lst_occ={}
    substr=[]
    strt_indx=0

    for i,char in enumerate(S):
        if char in lst_occ and lst_occ[char]>= strt_indx:
            substr.append(S[strt_indx:i])
            strt_indx =i
        lst_occ[char]=i
    substr.append(S[strt_indx:])
    return len(substr)




    for hos_sch in A:
        for doc_id in set(hos_sch):
            if doc_id in doc_count:
                doc_count[doc_id] +=1
            else:
                doc_count[doc_id]=1

    solution=sum(count >1 for count in doc_count.values())
    return solution


A=[[1,2,2],[3,1,4]]
res=solution(A)
print(res)

