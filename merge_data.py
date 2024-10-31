#First data belong to retail information
import pandas as pd


def load_retail_data(store_features_path, sales_path, store_info_path):
    try:
        store_features = pd.read_csv(store_features_path)
        sales = pd.read_csv(sales_path)
        store_info = pd.read_csv(store_info_path)
        return store_features, sales, store_info
        
    except Exception as e:
        print(f"Erros loading data: {e}")



store_features_df, retail_sales_df, retail_store_info = load_retail_data(
    "store_features.csv",
    "historical_sales.csv",
    "store_info.csv"
)

print(store_features_df.head(), retail_sales_df.head(), retail_store_info.head())



def merge_df(df1,df2,df3, merge_keys_df1_df3, merge_keys_df2):
    merge_df1_df3 = df1.merge(df3, on = merge_keys_df1_df3)
    all_merged = df2.merge(merge_df1_df3, on=merge_keys_df2)
    return all_merged


merged_result = merge_df(
    store_features_df,
    retail_sales_df,
    retail_store_info,
    
    merge_keys_df1_df3='Store',               
    merge_keys_df2=['Store', 'Date', 'IsHoliday']  
)

# Display the merged DataFrame
print(merged_result)