import streamlit as st

st.title('食材采购助手')

###
st.header('请选择菜单', divider='rainbow')

# Beef and Goat
st.subheader('牛羊肉',divider='gray')

# Pork
st.subheader('猪肉',divider='gray')
col1, col2, col3 = st.columns(3)
col1.checkbox('test1')

# Chicken
st.subheader('鸡肉',divider='gray')

# Seafood
st.subheader('海鲜',divider='gray')
col1, col2, col3 = st.columns(3)
shui_zhu_yu=col1.checkbox('水煮鱼')
you_men_da_xia=col2.checkbox('油焖大虾')

# Vegetables
st.subheader('青菜',divider='gray')

# Mian Shi
st.subheader('面食',divider='gray')


### 
st.header('建议采购清单', divider='rainbow')

mylist=[]
if(you_men_da_xia):
    mylist.extend(['虾','姜','蒜','葱','白糖','生抽','料酒','盐'])


mkdn=''
uniqlist=list(set(mylist))
for item in mylist:
    mkdn+=f'- {item}\n'

st.markdown(mkdn)
