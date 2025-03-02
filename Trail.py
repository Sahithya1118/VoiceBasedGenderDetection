#PREPROCESSING =BALANCED CSV------------>FEATURES.NPY LABLES.NPY
import os
import pandas as pd
import numpy as np
from tqdm import tqdm 

lable2int={
    "male":1,
    "female":0

}
def load_data(vector_length=128):
    #making results directory to store result arrays
    if not os.path.isdir('resuilts'):
        os.mkdir('resuilts')

#reading csv
    df=pd.read_csv(r"D:\ai project\gendeefinal\final\balanced-all.csv")
    #statistics
    n_samples = len(df)
    n_male_samples=len(df[df['gender']=='male'])
    n_female_samples=len(df[df['gender']=='female'])
    print("totsl",n_samples)
    print("male",n_male_samples)
    print("female",n_female_samples)
#numpy arrays initialzation with 0

    X=np.zeros((n_samples,vector_length))
    y=np.zeros((n_samples,1))



    for i,(filename,gender) in tqdm.tqdm(enumerate(zip(df['filename'],df['gender'])),"loaidng data", total=n_samples):
        features=np.load(filename)
        X[i]=features #featurrres
        y[i]=lable2int[gender] #lables

    np.save("featuresss.npy",X)   
    np.save("labless.npy",y)  

    return X,y

    print("files saved")


 
