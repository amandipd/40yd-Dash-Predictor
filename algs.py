import pandas as pd
import numpy as np
from sklearn import datasets

'''
Keep only input features:
Source IP Address, Destination IP Address, Source Port, Destination Port, Protocol, Packet Length, Traffic Type,
Anomaly Scores, Payload Data
and target variable:
Attack Type
'''
def clean_data(df):  
    dropped_columns = [
        "Timestamp", "Packet Type", "Payload Data", "Malware Indicators", 
        "Alerts/Warnings", "Attack Signature", "Action Taken", "Severity Level", 
        "User Information", "Network Segment", "Geo-location Data", 
        "Proxy Information", "Firewall Logs", "IDS/IPS Alerts", "Log Source"
    ]  
    df.drop(dropped_columns, axis = 1, inplace = True)
    print(df.columns)
    

        

def main():
    df = pd.read_csv('cybersecurity_attacks.csv')
    clean_data(df)


if __name__ == "__main__":
    main()