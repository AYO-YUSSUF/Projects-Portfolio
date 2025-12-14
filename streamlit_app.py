import pandas as pd
import re
import numpy as np

import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

@st.cache_data
def load_data(path="image_caption.txt"):
    df = pd.read_csv(path, sep="\t")
    return df

def clean_text(s):
    s = str(s).lower()
    s = re.sub(r"[^a-z\s]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s

@st.cache_resource
def build_index(df):
    df = df.copy()
    df["clean_caption"] = df["caption"].apply(clean_text)
    vec = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
    X = vec.fit_transform(df["clean_caption"])
    return df, vec, X

def search(df, vec, X, query, k=10):
    q_vec = vec.transform([clean_text(query)])
    sims = cosine_similarity(q_vec, X).ravel()
    top_idx = np.argsort(sims)[::-1][:k]
    out = df.loc[top_idx, ["ID", "caption"]].copy()
    out["score"] = sims[top_idx]
    return out.reset_index(drop=True)

st.title("Medical Caption Search (TF-IDF + Cosine Similarity)")

df_raw = load_data()
df, vec, X = build_index(df_raw)

query = st.text_input("Enter your query:")
k = st.selectbox("Top K results", [5, 10], index=1)

# Buttons for the two required queries :contentReference[oaicite:2]{index=2}
col1, col2 = st.columns(2)
with col1:
    if st.button("Run Q1"):
        query = "angiographic image shows normal coronary artery"
with col2:
    if st.button("Run Q2"):
        query = "fluoroscopy image demonstrating of balloon occlusion"

if query.strip():
    results = search(df, vec, X, query, k=k)
    st.write("Results:")
    st.dataframe(results)
