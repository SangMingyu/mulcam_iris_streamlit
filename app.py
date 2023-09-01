# -*- coding:utf-8 -*-

import streamlit as st
import numpy as np
import pandas as pd

import seaborn as sns
import scikitlearn as sklearn
import plotly as px


def main():
    st.markdown("# Hello World")
    st.write(np.__version__),
    st.write(pd.__version__),
    
    st.write(sns.__version__),
    st.write(sklearn.__version__),
    st.write(px.__version__)

if __name__ == "__main__":
    main()
