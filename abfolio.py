from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import investpy as inv
assets_class = ['stocks','bonds','etfs','cryptos',"currencies","funds"]
isin_history = []
isin_history2 = []
sum1=1
sum2=1
pos_var = 425
click_count = -1
#********REGISTER ALL DATA IN ISIN_ARRAY**********************
def registerData():
    global pos_var
    global sum1
    global sum2
    global click_count
    global isin_history
    global isin_history2
    if len(asset_perc.get()) > 0 and len(asset_box.get()) > 0 and len(asset_name.get())>0:
        click_count +=1
        if click_count > 10:
            click_count = 1 

    if round(sum1,4)>0:
        if len(asset_perc.get()) > 0 and len(asset_box.get()) > 0 and len(asset_name.get())>0:
            history_label = Label(root)
            individual_asset_label = Label(root)
            quote = inv.search_quotes(text=asset_name.get().upper(),products = [asset_box.get().lower()],n_results = 1)
            isin_history.append([quote.name,quote.symbol,quote.country,round(float(asset_perc.get())/100,4),asset_box.get().lower(),asset_name.get().upper()])
            sum1 -= round((float(asset_perc.get())/100),4)
            individual_asset_label.config(text="%s - %s"%(quote.symbol,round(float(asset_perc.get()),4)) + '%' ,fg='black',font='Consolas 13 underline',bg="#1c87b7")
            total_sum_label.config(text=str(round(sum1,4)*100)+"% unallocated (Portfolio 1)",fg='black',font='Times 13 italic',bg="#1c87b7")
            if 70 + (20*click_count) < 300:
                individual_asset_label.place(x=pos_var,y=70 + (20*click_count))
            else:
                pos_var = pos_var + 400
                individual_asset_label.place(x=pos_var,y=70 + (20*click_count))

            

            print(isin_history)
            asset_perc.delete(0,'end')
            asset_box.delete(0,'end')
            asset_name.delete(0,'end')
    elif round(sum2,4)>0:
        register_bttn.configure(bd=5,relief='raised',text='Click to register asset in "Portfolio 2"',fg='black')
        if len(asset_perc.get()) > 0 and len(asset_box.get()) > 0 and len(asset_name.get())>0:
            quote = inv.search_quotes(text=asset_name.get().upper(),products = [asset_box.get().lower()],n_results = 1)
            isin_history2.append([quote.name,quote.symbol,quote.country,round(float(asset_perc.get())/100,4),asset_box.get().lower(),asset_name.get().upper()])
            sum2 -= round(float(asset_perc.get())/100,4)
            total_sum_label.config(text=str(round(sum2,4)*100)+"% unallocated (Portfolio 2)",fg='black',font='Times 13 italic',bg="#1c87b7")
            asset_perc.delete(0,'end')
            asset_box.delete(0,'end')
            asset_name.delete(0,'end')
        print(isin_history2)
    
    else:
        register_bttn.place_forget()
    
    if round(sum1,4)<0:
        sum1 = 0
        messagebox.showwarning(title="Warning!",message='Portfolio 1 total percentage is higher than 100%')
    
    if round(sum2,4)<0:
        sum2 = 0
        messagebox.showwarning(title="Warning!",message='Portfolio 1 total percentage is higher than 100%')

    if round(sum1,4) == 0:
        p1_area_label.configure(text= 'Portfolio 1:',font='Consolas 16 bold',bg='#1c87b7',fg='black')
        total_sum_label.config(text=str(round(sum2,4)*100)+"% unallocated (Portfolio 2)",fg='black',font='Times 13 italic',bg="#1c87b7")
        p2_area_label.configure(text= 'Portfolio 2:',font='Consolas 16 bold',bg='#1c87b7',fg="#c50017")
        register_bttn.configure(bd=5,relief='raised',text='Click to register asset in "Portfolio 2"',fg='black')
    
    

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
    total_sum_label.place(x=16,y=110)
    p1_area_label.place(x=420,y=38)
    p2_area_label.place(x=420,y=300)

   
root = Tk()
total_sum_label = Label(root)
#**************SCREEN CONFIG****************
#comprimento x altura
root.geometry("900x600+0+0")
root.title("ABFolio - Market tools")
root.configure(background='#1c87b7')
#*************Screen change BUTTON******************
start_bttn = Button(root,bg='#2B3E6E',width=25,height=1,fg='white',command=backtestScreen)
start_bttn.configure(bd=5,relief='raised',text='Click to Proceed')
start_bttn.place(x=354,y=300)
#**********MAIN MENU TITLE********************
title = Label(root)
title.configure(font='Consolas 32 bold',fg="black",bg = '#1c87b7',text='ABFolio')
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
register_bttn.configure(bd=5,relief='raised',text='Click to register asset in "Portfolio 1"',fg='black')
#**************SUM LABEL FOR ASSET ALLOC. init screen******************
total_sum_label.config(text=str(round(sum1,4)*100)+"% unallocated (Portfolio 1)",fg='black',font='Times 13 italic',bg="#1c87b7")
#*****************Portfolio 1 Area Label****************************
p1_area_label = Label(root)
p1_area_label.configure(text= 'Portfolio 1:',font='Consolas 16 bold',bg='#1c87b7',fg='#c50017')
#*****************Portfolio 2 Area Label****************************
p2_area_label = Label(root)
p2_area_label.configure(text= 'Portfolio 2:',font='Consolas 16 bold',bg='#1c87b7')

root.mainloop()
