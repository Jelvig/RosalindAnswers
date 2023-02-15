def reader():
    file = r"C:\Users\jelvig\Downloads\rosalind_iev.txt"
    with open(file,'r') as f:
        lines = f.readlines()
        for line in lines:
            nums = line.split(' ')
        nums[-1] = nums[-1].strip('\n')
        nums = list(map(lambda x: int(x),nums))
        return nums

def expected(nums):
    dominance = {'AA_AA': 1,'AA_Aa': 1, 'AA_aa': 1, 'Aa_Aa': (3/4), 'Aa_aa': (2/4),'aa_aa':	0}
    count = 0
    babies = 0
    for dom in dominance:
        babies += dominance[dom]*nums[count]
        count+=1
    print(babies*2)  # two offspring and prints final answer

   
nums = reader()
expected(nums)
