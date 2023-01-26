if __name__=='__main__':
    from binance.client import Client
    import kody
    from tkinter import *
    from pprint import pprint
    import scraps
    import google
    import pandas as pd
    import matplotlib_inline



    client = Client(kody.apiKey,kody.apiSecurity)
    print('logged in')
    info = client.get_account()

    root = Tk()
    root.geometry('300x250')
    root.resizable(False, False)

    WSframe = Frame(root,background='green')
    WSframe.pack(pady= 5)
    Kframe = Frame(root,bg='blue')
    Kframe.pack(pady= 5)
    Sframe = Frame(root)
    Sframe.pack(pady= 5)
    KLframe = Frame(root)
    KLframe.pack(pady= 5)
    AMframe = Frame(root)
    AMframe.pack(pady= 5)
    ATframe = Frame(root)
    ATframe.pack(pady= 5)



    def saldo():
        wroc_frame = Frame(WSframe,background='red')
        wroc_frame.pack()
        but1.destroy()
        saldoo = {}

        for elements in info['balances']:
            if elements['free'] != '0.00000000' and elements['free'] != '0.00' and elements['free'] != '0.0':
                saldoo[str(elements['asset'])] = str(elements['free'])
                # saldo.append(str(elements['asset']))
                # saldo.append(str(elements['free']))
        print('wykonuje',saldoo)
        for keys in saldoo:
            label = Label(wroc_frame, text=str(keys + '             ' + saldoo[keys]))
            label.pack()
        root.geometry('300x350')


        def wroc():
            global but1
            but1 = Button(WSframe, text="Wyswietl saldo", fg='Blue', command=saldo)
            but1.pack()
            wroc_frame.destroy()
            root.geometry('300x250')

        but = Button(wroc_frame, text="Wróć", fg='Red', command=wroc)
        but.pack()


    from functools import partial


    def exit(root):
        root.destroy()
    wyjdz = partial(exit,root)

    from binance.enums import *
    def kup():
        kupfr = Frame(Kframe,bg='white')
        kupfr.pack()
        n = Label(kupfr,text='Narazie można kupić tylko USDT za Euro \n Ile USDT chcesz kupić?')
        n.grid(row=0 ,column=1)
        n1 = Label(kupfr,text='Podaj symbol pary')
        n1.grid(row=1,column=0)
        n2 = Label(kupfr, text='Ile chcesz kupić?')
        n2.grid(row=2, column=0)
        entrykup = Entry(kupfr)
        entrykup.grid(row=2,column=1)
        entrypara = Entry(kupfr)
        entrypara.grid(row = 1, column=1)
        root.geometry('350x350')
        but2.destroy()

        def kup1(entrykup):
            client.create_order(symbol=entrypara.get(), side=SIDE_BUY, type=ORDER_TYPE_MARKET, quantity=entrykup.get())
            global but2
            but2 = Button(Kframe, text="Kup", command=kup)
            but2.pack()
            kupfr.destroy()

        kup2 = partial(kup1,entrykup)
        ZatKupno = Button(kupfr, text='Zatwierdź kupno', command = kup2)
        ZatKupno.grid(row=3,column=1)

        def wroc():
            global but2
            but2 = Button(Kframe, text="Kup", command=kup)
            but2.pack()
            kupfr.destroy()
            root.geometry('300x250')

        but = Button(kupfr, text="Wróć",fg='Red',command=wroc)
        but.grid(row=4,column=1)



    def sprzedaj():
        sprzfr = Frame(Sframe)
        sprzfr.pack()
        n = Label(sprzfr, text='Narazie można sprzedac tylko Euro za USDT \n Ile USDT chcesz sprzedac?')
        n.grid(row=0, column=1)
        n1 = Label(sprzfr, text='Podaj symbol pary')
        n1.grid(row=1, column=0)
        n2 = Label(sprzfr, text='Ile chcesz sprzedać?')
        n2.grid(row=2, column=0)
        entrysprz = Entry(sprzfr)
        entrysprz.grid(row=2, column=1)
        entrypara1 = Entry(sprzfr)
        entrypara1.grid(row=1, column=1)
        root.geometry('350x350')
        but3.destroy()

        def sprz1(entrysprz):
            client.create_order(symbol=entrypara1.get(), side=SIDE_SELL, type=ORDER_TYPE_MARKET, quantity=entrysprz.get())
            global but3
            but3 = Button(Sframe, text="Sprzedaj", command=sprzedaj)
            but3.pack()
            sprzfr.destroy()
            root.geometry('300x250')

        sprz2 = partial(sprz1, entrysprz)
        ZatSprz = Button(sprzfr, text='Zatwierdź sprzedaż', command=sprz2)
        ZatSprz.grid(row=3,column=1)

        def wroc():
            global but3
            but3 = Button(Sframe, text="Sprzedaj", command=sprzedaj)
            but3.pack()
            sprzfr.destroy()
            root.geometry('300x250')

        but = Button(sprzfr, text="Wróć",fg='Red',command=wroc)
        but.grid(row=4,column=1)

    def an():
        anfr = Frame(AMframe)
        anfr.pack()
        n = Label(anfr, text='Co chcesz wyszukać?')
        n.grid(row = 0, column = 0)
        entryan = Entry(anfr)
        entryan.grid(row=0, column=1)
        root.geometry('350x350')
        but5.destroy()
        def c():
            import multi
            multi.dnr(scraps.techAn,google.techang,entryan.get())
            # scraps.techAn(entryan.get())
            # google.techang(entryan.get())

        zat = Button(anfr,text='Przeszukaj',command = c)
        zat.grid(row=1,column=1)
        def wroc():
            global but5
            but5 = Button(AMframe, text="Analiza mediów", command=an)
            but5.pack()
            anfr.destroy()
            root.geometry('300x250')

        but = Button(anfr, text="Wróć",fg='Red',command=wroc)
        but.grid(row=2,column=1)

    def at():
        atfr = Frame(ATframe)
        atfr.pack()

        n1 = Label(atfr, text='Podaj symbol pary')
        n1.grid(row=0, column=0)
        entrypara = Entry(atfr)
        entrypara.grid(row=0,column=1)

        n2 = Label(atfr, text='Podaj krok')
        n2.grid(row=1, column=0)
        entrykrok = Entry(atfr)
        entrykrok.grid(row=1,column=1)

        n3 = Label(atfr, text='Podaj okres')
        n3.grid(row=2,column=0)
        entryokres = Entry(atfr)
        entryokres.grid(row=2, column=1)

        but6.destroy()

        def at1(entryokres):
            data = pd.DataFrame(client.get_historical_klines(str(entrypara.get()), str(entrykrok.get()), str(entryokres.get())))
            global but6
            but6 = Button(ATframe, text="Analiza techniczna", command=at)
            but6.pack()
            atfr.destroy()
            def getminutedata(symbol,interval, lookback):
                frame = pd.DataFrame(client.get_historical_klines(symbol,interval,lookback))
                frame = frame.iloc[:,:6]
                frame.columns =['T','O','H','L','C','V']
                frame = frame.set_index('T')
                frame.index = pd.to_datetime(frame.index, unit='ms')
                frame = frame.astype(float)
                return frame
            test = getminutedata('BTCUSDT','1d','1w')
            test.plot()


            root.geometry('300x250')


        at2 = partial(at1, entryokres)
        ZatAna = Button(atfr, text='Zatwierdź', command=at2)
        ZatAna.grid(row=3,column=1)

        def wroc():
            global but6
            but6 = Button(ATframe, text="Analiza techniczna", command=at)
            but6.pack()
            atfr.destroy()
            root.geometry('300x250')

        but = Button(atfr, text="Wróć",fg='Red',command=wroc)
        but.grid(row=4,column=1)

        root.geometry('350x350')

        # data = pd.DataFrame(client.get_historical_klines('BTCUSDT', '1d', '1 week ago UTC'))
        # pprint(data)

    but1 = Button(WSframe, text="Wyswietl saldo",fg='Blue',command=saldo)
    but2 = Button(Kframe, text="Kup",command = kup)
    but3 = Button(Sframe, text="Sprzedaj", command = sprzedaj)
    but4 = Button(KLframe, text="Kup po wybranej cenie")
    but5 = Button(AMframe, text="Analiza mediów", command = an)
    but6 = Button(ATframe, text="Analiza techniczna", command = at)
    but1.pack()
    but2.pack()
    but3.pack()
    but4.pack()
    but5.pack()
    but6.pack()

    root.mainloop()




# order = client.create_order(symbol = 'EURUSDT',side = SIDE_SELL,type = ORDER_TYPE_MARKET,quantity=20)




