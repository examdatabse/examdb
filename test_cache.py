import lfu

if __name__ == '__main__':
    t1 = lfu.LFUCache(10000)
    t1.set('a', 'b')
    t1.set('c', 'd')
    print(t1.get('a'))
