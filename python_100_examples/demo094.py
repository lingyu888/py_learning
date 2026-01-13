# 题目：时间函数举例4,一个猜数游戏，判断一个人反应快慢。

if __name__ == '__main__':
    import time
    import random
    
    play_it = input('Do you want to play it? (\'y\' or \'n\'): ')  
    while play_it == 'y':
        c = input('Input a character:\n')  
        i = random.randint(0, 2**32) % 100
        print('Please input number you guess:\n')
        
        start = time.perf_counter()  # 使用 perf_counter() 替代 time.clock()
        a = time.time()
        
        guess = int(input('Input your guess:\n'))  
        while guess != i:
            if guess > i:
                print('Please input a little smaller')
                guess = int(input('Input your guess:\n'))  
            else:
                print('Please input a little bigger')
                guess = int(input('Input your guess:\n'))  
        
        end = time.perf_counter()  # 使用 perf_counter() 替代 time.clock()
        b = time.time()
        
        var = (end - start) / 18.2
        print(var)
        
        if var < 15:
            print('You are very clever!')
        elif var < 25:
            print('You are normal!')
        else:
            print('You are stupid!')
        
        print('Congratulations')
        print('The number you guessed is %d' % i)
        
        play_it = input('Do you want to play it?')  
