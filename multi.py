print('gienek')
def dnr(pr1,pr2,arg):
    import multiprocessing
    p1 = multiprocessing.Process(target=pr1,args=(arg,))
    p2 = multiprocessing.Process(target=pr2,args=(arg,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
