from sklearn.model_selection import train_test_split



def split_data(data,test_size=0.3,random_state=42):
    train,test=train_test_split(data,test_size=test_size,random_state=random_state)

    return train,test
