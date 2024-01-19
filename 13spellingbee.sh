#7 letters total
#1 char in the middle has to be used every time
#6 outer char can be used any number of times
#word_length min is 4
#Author: Lisa, Henry

#1.grep the letter only with r
#2.grep the word with only the letter:z,o,n,i,a,c; and length must exceed 4
gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "r" | grep -E "^[zoniacr]{4,}$" 
