i

ticker = 'clf'
start = '20070705'
end = '20110810'
count=500*0
left=[]
h
#    hk_tickers.append('0%s.hk' %i)
#for i in range(1000,4000):
#    hk_tickers.append('%s.hk' %i)
#print hk_tickers
#hk=[]
#for i in hk_tickers:
#    a=get_all(i)
#    if a['market_cap'][-1]=='B':
#        hk.append(i)
#print hk
#print len(hk)

#
    share=hs_shares[i]
    item.append(ticker)
    item.append(name)
    if  ticker in hs_energy:
        sector='energy'
    elif ticker in hs_basic_materials:
        sector='basic materials'
    elif ticker in hs_industrial:
        sector='industrial'
    elif ticker in hs_consumer_dis:
        sector='consumer discretionary'
    else:
        sector='consumer staples'
    item.append(sector)
    item.append(share)
    hs300_list.append(item)
#print len(hs300_list)
#print hs300_list
hs300_dic={}
for i in hs300_list:
    hs300_dic[i[0]]=i[1:]
print hs300_dic
#conn=connectdb('hk')
#cursor = conn.cursor()
#for i in range(len(hs300_list)):
#    query="insert into  sector(ticker,name,sector,shares) values(%s,%s,%s,%s)" 
#    cursor.execute (query,tuple(hs300_list[i]))
#cursor.close ()
#conn.close ()
#print 'write database success!'   


    
#writedb('hk','hs300',hs300)
#writedb('hk','hs300',left)