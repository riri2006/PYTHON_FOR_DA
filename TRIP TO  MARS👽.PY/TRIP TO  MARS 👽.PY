# LEVEL 1 — PIPELINE THINKING
def clean_text(text):
    print("THE UNWANTED DATA IS DELETED/CLEANED" )
    return text.strip().replace("\n"," ")
def lowercase(text):
    print("THE TEXT SHOULD BE IN LOWER_CASE")  
    return text.lower()    
def count_words(text):
    print("THE COUNT OF THE WORDS ARE ")
    return text.split()

pipeline = [
    clean_text,
    lowercase,
    count_words
]    
        
def pipeline1(text,pipeline):
    for func in pipeline:
        text = func(text)
    return text    



result = pipeline1("hello vedant WELCOME to the company!       ",pipeline)
print(result)


