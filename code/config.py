
train_path = r"C:\Users\tanch\Documents\NTU\NTU Year 4\Semester 1\CZ4041 - Machine Learning\Team Project\data\train.csv"
test_path = r"C:\Users\tanch\Documents\NTU\NTU Year 4\Semester 1\CZ4041 - Machine Learning\Team Project\data\test.csv"
merchants_path = r"C:\Users\tanch\Documents\NTU\NTU Year 4\Semester 1\CZ4041 - Machine Learning\Team Project\data\merchants.csv"
historical_transactions_path = r"C:\Users\tanch\Documents\NTU\NTU Year 4\Semester 1\CZ4041 - Machine Learning\Team Project\data\historical_transactions.csv"
new_transactions_path = r"C:\Users\tanch\Documents\NTU\NTU Year 4\Semester 1\CZ4041 - Machine Learning\Team Project\data\new_merchant_transactions.csv"

# dictionary categorizing all coolumns available 
feature_names = {
    "train_test":{
        "id":["card_id"],
        "categoric":['feature_1', 'feature_2', 'feature_3'],
        "datetime":["first_active_month"]
    },
    "merchants":{
        "id": ['merchant_id', 'merchant_group_id', 'merchant_category_id','subsector_id', 'city_id', 'state_id'],
        "categoric": ['category_1','most_recent_sales_range', 'most_recent_purchases_range','category_4', 'category_2'],
        "numeric": ['numerical_1', 'numerical_2','avg_sales_lag3', 'avg_purchases_lag3','avg_sales_lag6', 'avg_purchases_lag6','avg_sales_lag12', 'avg_purchases_lag12', 'active_months_lag3','active_months_lag6','active_months_lag12']
    },
    "transactions":{
        "id": ['card_id', 'city_id','merchant_category_id', 'merchant_id','state_id','subsector_id'],
        "categoric": ['authorized_flag','category_1',"category_3", "category_2"],
        "numeric": ['purchase_amount', 'month_lag',"installments"],
        "datetime": ['purchase_date']
    },
}