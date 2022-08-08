from tkinter import *
from tkinter import ttk
import investpy as inv
assets_class = ['stocks','bonds','etfs','cryptos',"currencies","funds"]
isin_history = []
isin_history2 = []
sum1=1
sum2=1
click_count = -1
#********REGISTER ALL DATA IN ISIN_ARRAY**********************
def registerData():
    global sum1
    global sum2
    global click_count
    global isin_history
    global isin_history2
    click_count +=1
    if round(sum1,4)>=0:
        if round(float(asset_perc.get()),4) >= 100:
            print('heyyy brooooo')
        quote = inv.search_quotes(text=asset_name.get().upper(),products = [asset_box.get().lower()],n_results = 1)
        isin_history.append([quote.name,quote.symbol,quote.country,float(asset_perc.get())/100,asset_box.get().lower(),asset_name.get().upper()])
        
        sum1 -= (float(asset_perc.get())/100)
        print(sum1)
        print(isin_history)
    else:
        isin_history = list(dict.fromkeys(isin_history))
        asset_perc.delete(0,'end')
        asset_box.delete(0,'end')
        asset_name.delete(0,'end')
        quote = inv.search_quotes(text=asset_name.get().upper(),products = [asset_box.get().lower()],n_results = 1)
        isin_history2.append([quote.name,quote.symbol,quote.country,float(asset_perc.get())/100,asset_box.get().lower(),asset_name.get().upper()])
        sum2 -= (float(asset_perc.get())/100)
        print(isin_history2)

#******************************************************************
def backtestScreen():
    start_bttn.place_forget()
    title.place_forget()
    asset_box.place(x=16,y=40)
    asset_name.place(x=160,y=38)
    asset_perc.place(x=310,y=38)

    cat_label.place(x=30,y=20)
    ticker_label.place(x=160,y=17)
    percentage.place(x=310,y=17) 
    register_bttn.place(x=16,y=75)
   
root = Tk()
#**************SCREEN CONFIG****************
#comprimento x altura
root.geometry("900x500")
root.title("ABFolio - Market tools")
root.configure(background='#1c87b7')
#*************Screen change BUTTON******************
start_bttn = Button(root,bg='#2B3E6E',width=25,height=1,fg='white',command=backtestScreen)
start_bttn.configure(bd=5,relief='raised',text='Click to Proceed')
start_bttn.place(x=354,y=300)
#**********MAIN MENU TITLE********************
title = Label(root)
title.configure(font='Consolas 32 bold',fg="gold",bg = '#1c87b7',text='ABFolio')
title.place(x=361,y=80)
#***************COMBOBOX************
asset_box = ttk.Combobox(root,values=assets_class,background='#1c87b7')
asset_box.configure(width=11,height=8,font='Consolas 14 bold')
#********************************
asset_name = Entry(root)
asset_name.config(bd=5,relief='sunken',width=14,font='Consolas 13 bold')
#********************************
asset_perc = Entry(root)
asset_perc.config(bd=5,relief='sunken',width=7,font='Consolas 13 bold')
#********************************
cat_label = Label(root)
cat_label.configure(text='Asset:',bg='#1c87b7',fg='black')

ticker_label = Label(root)
ticker_label.configure(text='Ticker/ISIN code:',bg='#1c87b7',fg='black')

percentage = Label(root)
percentage.configure(text='Percentage:',bg='#1c87b7',fg='black')
#**************COFNIG AND DECLARE ASSET REGISTRATION BUTTON******************

register_bttn = Button(root,bg='orange',width=51,height=1,fg='white',command=registerData)
register_bttn.configure(bd=5,relief='raised',text='Click to register asset',fg='black')


root.mainloop()


