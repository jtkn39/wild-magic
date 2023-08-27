import numpy as np
import pandas as pd
import streamlit as st


def check_res_for_rolls(res):
    words = res.split(' ')
    for word in words:
        if word[0].isnumeric() and word[-1].isnumeric() and 'd' in word:
            num_dice_str, dice_size_str = word.split('d')
            num_dice, dice_size = int(num_dice_str), int(dice_size_str)
            roll = np.random.randint(low=1, high=1+dice_size, size=num_dice).sum()
            roll_str = str(roll)
            res = res.replace(word, roll_str)
    return res
            
def format_result(res):
    res = check_res_for_rolls(res)
    if not res.endswith('.'):
        return res+'.'
    else:
        return res
            

st.title('Welcome to the wild magic surge generator.')

df = pd.read_csv('wm_table.csv')
effects = df['Effect'].values

roll_twice = st.checkbox('Roll twice?')

if st.button('Surge!'):
    if roll_twice:
        results = np.random.choice(effects, size=2)
        columns = st.columns(2)
        for res, col in zip(results, columns):
            col.write(format_result(res))
    else:
        res = np.random.choice(effects)
        st.write(format_result(res))