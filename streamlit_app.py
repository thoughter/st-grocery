import streamlit as st

st.title('食材采购助手')

###
st.header('选择菜谱', divider='rainbow')

# Beef and Goat
st.subheader('牛羊肉',divider='gray')
col1, col2, col3 = st.columns(3)
with col1:
  芥兰牛=st.checkbox('芥兰牛')


# Pork
st.subheader('猪肉',divider='gray')
col1, col2, col3 = st.columns(3)
with col1:
  红烧肉=st.checkbox('红烧肉')
  辣椒炒香肠=st.checkbox('辣椒炒香肠')
with col2:
  青笋肉片=st.checkbox('青笋肉片')
with col3:
  糖醋里脊=st.checkbox('糖醋里脊')


# Chicken
st.subheader('鸡肉',divider='gray')
col1, col2, col3 = st.columns(3)
with col1:
  红烧鸡=st.checkbox('红烧鸡')

# Seafood
st.subheader('海鲜',divider='gray')
col1, col2, col3 = st.columns(3)
with col1:
  水煮鱼=st.checkbox('水煮鱼')
with col2:
  油焖大虾=st.checkbox('油焖大虾')

# Vegetables
st.subheader('青菜',divider='gray')
col1, col2, col3 = st.columns(3)
with col1:
  香菇油菜=st.checkbox('香菇油菜')

st.subheader('面食',divider='gray')
col1, col2, col3 = st.columns(3)
with col1:
  韭菜盒子=st.checkbox('韭菜盒子')
with col2:
  三鲜水饺=st.checkbox('三鲜水饺')
with col3:
  西红柿鸡蛋面片=st.checkbox('西红柿鸡蛋面片')

### 
st.header('采购清单', divider='rainbow')

mylist=[]

if(辣椒炒香肠):
    mylist.extend(['香肠','薄皮辣椒','洋葱','姜','盐','生抽'])
if(西红柿鸡蛋面片):
    mylist.extend(['面','鸡蛋','小青菜','西红柿','葱','蒜','姜'])
if(三鲜水饺):
    mylist.extend(['猪肉','虾仁','木耳','鸡蛋','香菇','韭菜','料酒','生抽','蚝油','盐','葱','姜','香油','油'])
if(糖醋里脊):
    mylist.extend(['里脊肉','料酒','盐','鸡蛋','番茄酱','糖','白醋','淀粉','面粉'])
if(青笋肉片):
    mylist.extend(['莴笋','猪肉','蒜','干辣椒','料酒','淀粉','生抽','黑胡椒粉','蚝油','盐'])
if(香菇油菜):
    mylist.extend(['香菇','油菜','生抽','蚝油','盐','蒜'])
if(红烧鸡):
    mylist.extend(['鸡腿','干辣椒','八角','花椒','姜','大葱','蒜','生抽','老抽','豆瓣酱','蚝油','冰糖'])
if(芥兰牛):
    mylist.extend(['芥兰','牛肉','老抽','生抽','耗油','姜','蒜','盐','油','淀粉','胡椒粉'])
if(红烧肉):
    mylist.extend(['五花肉','姜','八角','葱','桂皮','冰糖','生抽','料酒','盐','老抽'])
if(油焖大虾):
    mylist.extend(['虾','姜','蒜','葱','白糖','生抽','料酒','盐'])
if(水煮鱼):
    mylist.extend(['鱼片','姜','蒜','淀粉','花椒','料酒','盐','干辣椒','豆瓣酱','黄豆芽'])
if(韭菜盒子):
    mylist.extend(['面粉','韭菜','鸡蛋','盐','油'])


mkdn=''
uniqlist=list(set(mylist))
col=[None]*3
col[0],col[1],col[2]=st.columns(3)
for i,item in enumerate(uniqlist):
  col[i%3].checkbox(item)
