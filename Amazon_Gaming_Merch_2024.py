import pandas as pdimport osos.chdir('/Users/andrewsfolder/Documents/Portfolio/VG Merch Project') #os.chdir allows you to change the current directory to the path you inputos.getcwd() #this shows the current working directorydf = pd.read_csv("amazon_best_sellers_gaming_merchandise_2024.csv")list = [0,1,2,3,4,5,6]def Cleaner(df):    df = df.dropna(subset = ["brand", "stars", "reviewsCount", "price/currency", "price/value"])    return(df)def Breakdown(data):    #Tells us what item has the most reviews    # Sort by review_count and get the first row    top_item = data.sort_values('reviewsCount', ascending=False).iloc[0]    print(f"{top_item['title']} has the most reviews with {top_item['reviewsCount']} reviews")#This function will be used for any adjustments like new columns for the datasetdef Adjuster(df):    #This creates a new column that measures the length of the description string    df["desc_length"] = df["description"].str.len()    df["desc_length"] = df["desc_length"].fillna(0)    df["desc_length"] = df["desc_length"].astype(int)        #This creates a new column of the overall category of the item listing on amazon    #df["Category"] = df.breadCrumbs.str.split('›').str[0]    for i in list:        df[f"Category_{i}"] = df.breadCrumbs[:].str.split('›').str[i]        df['Specific_Category'] = df['breadCrumbs'].fillna('').str.count('›')+1        return(df)#Shows the average ratings of different brands and the total reviews their products havedef Topitems(df):    brandreviews = df.groupby('brand').agg(        Rating=('stars', 'mean'), Reviews=(            'reviewsCount', 'sum')).sort_values(                "Reviews", ascending = False).reset_index()    top = brandreviews[brandreviews.Rating > 4.5].head(10)       return(top)            #Shows the average ratings of different brands and the total reviews their products havedef TopCat(df):    for i in list:        print(df.groupby(f'Category_{i}').agg(Overall_Cat = (f"Category_{i}", "count")).sort_values(            "Overall_Cat", ascending = False).head(10))   df = Cleaner(df)df = Adjuster(df)df.to_excel("amazon_gaming_merch_updated.xlsx")#df['Specific_Category'].sort_values(ascending = False)#Breakdown(data)#df.groupby("brand")["reviewsCount"].aggregate(sum).sort_values(ascending = False).head(20)#pd.crosstab(data["brand"], data["stars"])#joe = 2+2#print(f"hi, {joe}")#Cleans the dataset for any nulls to improve our exploration and visualization#lets make a function that gets the overall category. This would check the initial# text of the item before it reaches the ›#df[["stars", "desc_length"]]#df.groupby("brand")[["stars"]].mean().sort_values("stars", ascending=False)#brandreviews["Rating"] = brandreviews["Rating"].astype(int)#df[["title", "reviewsCount"]]