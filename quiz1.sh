echo "Real name:Ruihan Yuan"
echo "User name:lisayuan"

gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "a" | grep -E 
"^[cmuotfa]{4,}$"
gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "b" | grep -E 
"^[rtailnb]{4,}$"
gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "c" | grep -E 
"^[dmaocni]{4,}$"
gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "z" | grep -E 
"^[ianorgz]{4,}$"

gunzip -c ~/Code/MCB185/data/jaspar2024_core.transfac.gz | grep -c "CC 
tax_group:" | cut -d ":" -f2 | sort | uniq -c  
