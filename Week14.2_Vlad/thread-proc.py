import subprocess
import threading
import time
import concurrent.futures
from multiprocessing import Process, Queue, Pool, Lock
# GIL


def subproc():
    output = subprocess.run(["dir"], shell=True,
                            capture_output=True, text=True)
    result = output.stdout.split('\n')
    print(result)


def suma_single_local(n):
    S = 0
    for i in range(1, n+1):
        S += i
    return S


def suma_2(n1, n2, q):
    S = 0
    for i in range(n1, n2):
        S += i
    q.put(S)


def suma_3(param):
    n1, n2 = param
    S = 0
    for i in range(n1, n2):
        S += i
    return S


def calcul_suma_1(n):
    t_sta = time.time()
    S = suma_single_local(n)
    t_sto = time.time()
    print(S)
    print(t_sto - t_sta)

# [(1,100), (100, 200), ...]


def suma_multi_extern(n, cores):
    n = n + 1
    elemente = n // cores
    params = [(i*elemente, (i+1)*elemente) for i in range(cores)]
    if n % cores != 0:
        params[-1] = (params[-1][0], n)
    q = Queue()
    procese = []
    for param in params:
        p = Process(target=suma_2, args=[param[0], param[1], q])
        p.start()
        procese += [p]
    for p in procese:
        p.join()
    S = 0
    while not q.empty():
        S += q.get()
    print(S)


def suma_multi_extern_pool(n, cores, nr_items):
    n = n + 1
    elemente = n // nr_items
    params = [(i*elemente, (i+1)*elemente) for i in range(nr_items)]
    if n % nr_items != 0:
        params[-1] = (params[-1][0], n)
    with Pool(cores) as p:
        result = p.map(suma_3, params)
    S = 0
    for s in result:
        S += s
    print(S)


def calcul_suma_2(n, p):
    t_sta = time.time()
    suma_multi_extern(n, p)
    t_sto = time.time()
    print(t_sto - t_sta)


def calcul_suma_3(n, p, intervale):
    t_sta = time.time()
    suma_multi_extern_pool(n, p, intervale)
    t_sto = time.time()
    print(t_sto - t_sta)


def scrie(l, i):
    t = str(i*10) + '\n'
    l.acquire()
    with open("fisier.txt", 'a') as f:
        try:
            f.write(t)
        except:
            print("eroare\n")
    l.release()


def resursa_critica():
    l = Lock()
    for i in range(100):
        Process(target=scrie, args=(l, i)).start()


def tfunc(n1, n2):
    S = 0
    for i in range(n1, n2 + 1):
        S += i
    print(S)


def thread_int(n):
    t_sta = time.time()
    t = threading.Thread(target=tfunc, args=(1, n))
    t.start()
    t.join()
    t_sto = time.time()
    print(t_sto - t_sta)


def multi_thread_int(n, threads, workers):
    n = n + 1
    count = n // threads
    params = [(i*count, (i+1)*count) for i in range(threads)]
    t_sta = time.time()
    if n % threads != 0:
        params[-1] = (params[-1][0], n)
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        result = executor.map(suma_3, params)
    t_sto = time.time()
    S = 0
    for s in result:
        S += s
    print(S)
    print(t_sto - t_sta)


def main():
    # subproc()
    # calcul_suma_1(400000000)
    # calcul_suma_2(400000000, 8)
    # calcul_suma_3(400000000, 8, 100)
    # resursa_critica()
    # thread_int(100000000)
    # multi_thread_int(400000000, 50, 16)
    pass


if __name__ == "__main__":
    main()
