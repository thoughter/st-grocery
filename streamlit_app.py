import streamlit as st
import receipt

def update_items(items, gid):

  is_clicked = st.session_state[gid]
  if(is_clicked):
    st.session_state['all_items'][gid]=items
  else:
    del st.session_state['all_items'][gid]

def show_dishes(gid, cat_name, cat_items):
  st.subheader(cat_name,divider='gray')
  col=[None]*3
  col[0], col[1], col[2] = st.columns(3)
  mylist=list(cat_items)
  
  for lid, (dish, items) in enumerate(mylist):
    col[lid%3].checkbox(dish,key=gid,on_change=update_items,args=(items,gid,))
    gid+=1
  return gid  

if('all_items' not in st.session_state):
  st.session_state['all_items']={}

st.title('食材采购助手')

###
st.header('选择菜谱', divider='rainbow')
gid=0

gid=show_dishes(gid, '牛羊肉', receipt.niuyang.items())
gid=show_dishes(gid, '猪肉', receipt.zhurou.items())
gid=show_dishes(gid, '鸡鸭', receipt.jiya.items())
gid=show_dishes(gid, '海鲜', receipt.haixian.items())
gid=show_dishes(gid, '蔬菜', receipt.shucai.items())
gid=show_dishes(gid, '面食', receipt.mianshi.items())

### 
st.header('采购清单', divider='rainbow')

if('all_items' in st.session_state):
  mylist=[]

  for gid, items in st.session_state['all_items'].items():
    mylist.extend(items)

  mkdn=''
  uniqlist=list(set(mylist))
  col=[None]*3
  col[0],col[1],col[2]=st.columns(3)
  for i,item in enumerate(uniqlist):
    col[i%3].checkbox(item)
