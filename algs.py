import pandas as pd
import numpy as np
from sklearn import datasets

def clean_data(df):  
    dropped_columns = [
        "Timestamp", "Packet Type", "Payload Data", "Malware Indicators", 
        "Alerts/Warnings", "Attack Signature", "Action Taken", "Severity Level", 
        "User Information", "Network Segment", "Geo-location Data", 
        "Proxy Information", "Firewall Logs", "IDS/IPS Alerts", "Log Source"
    ]  
    df.drop(dropped_columns, axis = 1, inplace = True)

    # Normalizing Packet Length and Anomaly Score with z-score standardization
    col1 = "Packet Length"
    col2 = "Anomaly Score"
    df[col1] = (df[col1] - df[col1].mean()) / df[col1].std()
    df[col2] = (df[col1] - df[col1].mean()) / df[col1].std()
    print(df[col2]) 


def main():
    df = pd.read_csv('cybersecurity_attacks.csv')
    clean_data(df)


if __name__ == "__main__":
    main()