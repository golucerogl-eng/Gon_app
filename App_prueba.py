import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("traj_UNI_CORR_500_01.txt", 
                 skiprows=4, 
                 sep="\t", 
                 names=["ID", "frames", "X", "Y", "Z"])


st.write("""
# Mi primera aplicación interactiva
## 
""")
