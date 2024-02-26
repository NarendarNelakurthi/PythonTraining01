import string
sentence="""Multicollinearity occurs when two or more independent variables in a regression model are highly correlated with each other . This high correlation can cause issues in the estimation of the regression coefficients Multicollinearity does not affect the predictive power of the model , but it makes it difficult to interpret the individual effects of the correlated variables on the dependent variable . Symptoms of multicollinearoving one of the correlated variables , combining the correlated variables into a single variable , or using regularization . techniques such as ridge regression or LASSO"""
#print(sentence)
case_sensitive={}
for char in sentence:
    if char in case_sensitive:
        case_sensitive[char]+=1
    else:
        case_sensitive[char] = 1
print(f"The case sensitive count {case_sensitive}")
print('\n')
case_insensitive=dict()
sentence_lower=sentence.lower()
for char in sentence_lower:
    if char in case_insensitive:
        case_insensitive[char] +=1
    else:
        case_insensitive[char] = 1
print(f"The case insensitive count= {case_insensitive}")
print('\n')
sentence_word_count={}
sentence_words=sentence.split()
for char in sentence_words:
    if char in sentence_word_count:
        sentence_word_count[char] +=1
    else:
        sentence_word_count[char] = 1
print(f"The case sentence word count= {sentence_word_count}")
print('\n')
sentence_word_count={}
sentence_words=sentence.lower().split()

for char in sentence_words:
    if char in sentence_word_count:
        sentence_word_count[char] +=1
    else:
        sentence_word_count[char] = 1
print(f"The case sentence word count= {sentence_word_count}")

print('\n')

sentence_word_count={}
sentence_words=sentence.lower().split()

for char in sentence_words:
    if char not in string.punctuation:
      if char in sentence_word_count:
        sentence_word_count[char] +=1
      else:
         sentence_word_count[char] = 1
    else:
        continue
print(f"The case sentence word count= {sentence_word_count}")

a=case_sensitive.setdefault('M',20)
print(a)