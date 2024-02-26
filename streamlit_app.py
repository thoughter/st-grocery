import streamlit as st

st.title('食材采购助手')

###
st.header('请选择菜单', divider='rainbow')

# Beef and Goat
st.subheader('牛羊肉',divider='gray')

# Pork
st.subheader('猪肉',divider='gray')
col1, col2, col3 = st.columns(3)
红烧肉=col1.checkbox('红烧肉')

# Chicken
st.subheader('鸡肉',divider='gray')

# Seafood
st.subheader('海鲜',divider='gray')
col1, col2, col3 = st.columns(3)
水煮鱼=col1.checkbox('水煮鱼')
油焖大虾=col2.checkbox('油焖大虾')

# Vegetables
st.subheader('青菜',divider='gray')

# Mian Shi
st.subheader('面食',divider='gray')


### 
st.header('建议采购清单', divider='rainbow')

mylist=[]
if(红烧肉):
    mylist.extend(['五花肉','姜','八角','葱','桂皮','冰糖','生抽','料酒','盐','老抽'])
if(油焖大虾):
    mylist.extend(['虾','姜','蒜','葱','白糖','生抽','料酒','盐'])
if(水煮鱼):
    mylist.extend(['鱼片','姜','蒜','淀粉','花椒','料酒','盐','干辣椒','豆瓣酱','黄豆芽'])


mkdn=''
uniqlist=list(set(mylist))
for item in uniqlist:
    mkdn+=f'- {item}\n'

st.markdown(mkdn)
