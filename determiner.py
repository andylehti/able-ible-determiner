import pandas as pd

def strip_vowels(word):
    while word and word[-1] in 'aeiou':
        word = word[:-1]
    return word

def get_tokens(word): return [word[i:i+n] for n in (2, 3) for i in range(len(word)-n+1)]
def load_csv(file): return pd.read_csv(file, header=None)
def find_row(df, suffix): return df[df[0] == suffix].iloc[0] if not df[df[0] == suffix].empty else None
def count_matches(tokens, cell): return sum(1 for t in tokens if t in cell)

def determine(word):
    tokens = get_tokens(word)
    suffix = word[-2:]
    able_df = load_csv('able.csv')
    ible_df = load_csv('ible.csv')
    able_row = find_row(able_df, suffix)
    ible_row = find_row(ible_df, suffix)
    if able_row is None and ible_row is None:
        return 'able'
    able_matches = count_matches(tokens, able_row[1]) if able_row is not None else 0
    ible_matches = count_matches(tokens, ible_row[1]) if ible_row is not None else 0
    
    return word + 'able' if able_matches >= ible_matches else word + 'ible'

word = 'create' # example of a failed word because the vowel needs to be stripped, but for the most part, -able, -ible does not strip the vowel.

# True: 5117 / False: 209 without stripping
# True: 4389 / False: 937 with stripping

result = determine(word)
print(result)
