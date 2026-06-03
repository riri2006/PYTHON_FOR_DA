import pandas as pd
def student_info(**kwargs):

    df = pd.DataFrame([kwargs])
    
    print("\n--- Pandas DataFrame ---")
    print(df)
    
    # Optional: You can return it to use it later in your code
    return df

name1 = input("Please Enter Your Name ")
age1 = int(input("Please enter your Age "))
city1 = input("Please enter your city name ")


student_info(name = name1, age = age1,city=city1)  