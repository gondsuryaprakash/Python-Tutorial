MAX_SIZE=100001
isPrime=[True]*MAX_SIZE
prime=[]
SPF=[None]*MAX_SIZE
def maniPulatef_Sieve(N):
    isPrime[0]=isPrime[1]=False
    for i in range(2,N):
        if isPrime[i]==True:
            prime.append(i)
            SPF[i]=i

        j=0;
        while j<len(prime) and i*prime[j]<N and prime[j]<=SPF[i]:
            isPrime[i*prime[j]]=False
            SPF[i*prime[j]]=prime[j]
            j+=1
    