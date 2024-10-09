
seq = "ATCATGCTGATAAACCTATA" 
dict_seqflipper = {"A":"T", "T":"A", "C":"G", "G":"C"} 
seq_flipped = "" 
for l in seq: 
  seq_flipped += dict_seqflipper[l] 
  
print(seq_flipped)

