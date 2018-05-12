class ProteinN:
    def __init__(self,string):
        self.string = string
        self.codon_dict = {
            "UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
            "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
            "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
            "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
            "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
            "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
            "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
            "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
            "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
            "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
            "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
            "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
            "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
            "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
            "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
            "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}

    def transcriptionCO(self,string):#transcribes crick strand
        self.new_string = self.string.replace("T","U")

    def reverse_compliment_transcription(self):#transcription...transcribes watson strand
        new_string1 = self.string.replace("A","X").replace("T","A").replace("X","T")
        new_string2 = new_string1.replace("C","X").replace("G","C").replace("X","G")
        self.reverse_string = new_string2[-1::-1] #string[start,end,step]
        self.new_string = self.reverse_string.replace("T","U")
        
    def translation(self,mRNA):
        self.peptide = ""
        start_sequence = mRNA.find("AUG")
        if(start_sequence != -1):
            while(start_sequence + 2 < len(mRNA)):
                code = mRNA[start_sequence:start_sequence + 3]
                if(code == "UAA" or code == "UAG" or code == "UGA"):
                    break
                start_sequence += 3 # index to the next 3 nucleotides
                self.peptide += self.codon_dict[code]
                
                
def get_pairs(beginning, end):
    pairs = []
    for i in beginning:
        taken = False
        for j in end:
            if(j>i and (j- i)%3 ==0 and not taken):
                pairs.append((i,j))
                taken = True
    return pairs
                
def Crick(DNA,ls):
    stran = ProteinN(DNA)
    stran.transcriptionCO(stran.string)
    stran.translation(stran.new_string)
    
    start =[i for i in range(len(stran.new_string)-3) if stran.new_string[i:i+3]=='AUG']

    stop_code = ['UAA','UAG','UGA']
    stop = [i for i in range(len(stran.new_string)-3) if stran.new_string[i:i+3] in stop_code]
 
    pairs = get_pairs(start,stop)
    for pair in pairs:
        B, E = pair
        stran.translation(stran.new_string[B:E])
        ls.append(stran.peptide)
    return ls
   

        
def Watson(DNA,ls1):  
    strand = ProteinN(DNA)
    strand.reverse_compliment_transcription()
    strand.translation(strand.new_string)
    stop_code = ['UAA','UAG','UGA']
    start =[i for i in range(len(strand.new_string)-3) if strand.new_string[i:i+3]=='AUG']
    stop = [i for i in range(len(strand.new_string)-3) if strand.new_string[i:i+3] in stop_code]

    
    pairs = get_pairs(start,stop)
    for pair in pairs:
        b, e = pair
        strand.translation(strand.new_string[b:e])
        ls1.append(strand.peptide)
    return ls1


def main():
    DNA = 'TCTCATTCGACTATCCTGTGCGGGCATGACAGCTGGTGGGTCGTCGACGGATGTCGAGGTTTACAACCATATGGTTCTCCTAAAAACGAAAGGCAATCCCTCCCGGGCGAGAGGTTACGATGGACGCGGCAATCGGGCCTGGTTATCATCTTCGGCTGAGGCATGGTCAGTTAACATATGATGTGCCACAGAGCCCAGCTTGAAGCTTGGGTATACCGTCCGCTCCGTGCAGGTTTACTTCTTATCACAAAGTGATCTCCCTAATAACTACACTCGTGTACATGGCGGTACGTCTAGGCATGTCAACTAGATAACTTCTAGATAAGGTGATCGCAGCGTAGCGAGTGCATCGTAACGACAGCAAGAGGCGCGTTAGGACCGCTGTGTCTACACTTTTGGTGCTACACCTTAGTTCCGCATTTATTGAGCATCCCGAGGAATGAAAGAGTTGCCCAAACTGCTGTTACCCTAGCTAGGGTAACAGCAGTTTGGGCAACTCTTTCATACGCCGGTTCGGTTTTGTGCCGTGGATGATGGTGACATACGGAACTCGCTACCTACTCCAGATAGCGTGTTACTACAGCGCAAGTATCTGTCATAAAGGAGTCGGAGGCCATGCCTCCCTGTTGCTGCTTCAGAGGGTCTATACTGATAACGTTGGAGGTACATTGTGCGTTCCGCTGATCTCTTGTAAGCATGTTGGCTTCGGCGTGGATGAAATGCAGAAGAGTCTGTGGTTTCCGCGCCAAACCGGTAGGTACCATACAAACTAAGAACTTGCGCGCGAAGAGGAACCACTGGAACTCCTAATTATCAAGTACTGGAATTCGCAGCACGCCGGCCTTTGCCCCTCAAGGCCTGGCTGAACAGCTATGGCCGCCCACCTGATTTTGGAAGATCTGACGGGCCCTCATCTCCGAGCGAAGACTGACAAAGTGTGCCGG'
    ls = []
    ls1 =[]
    Crick(DNA,ls)
    Watson(DNA,ls1)
    for protein in set(ls + ls1):
        print(protein)
main()   