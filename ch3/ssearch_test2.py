from ssearch_while import seq_search

t = (4,7,5.6,2,3.14,1)
s = "string"
a = ["DTS", "AAC", "FLAC"]

print(f'The index of 5.6 in {t} is {seq_search(t, 5.6)}')
print(f'The index of "n" in {s} is {seq_search(s, "n")}')
print(f'The index of "DTS" in {a} is {seq_search(a,"DTS")}')
