import examdb.lfu

if __name__ == '__main__':
    t1 = examdb.lfu.LFUCache(10000)
    t1.set('a', 'b')
    t1.set('c', 'd')
    print(t1.get('a'))
