#structure, scope


x = 43
def count_coins( coins ):
    '''
    in: list of numbers
    out: sum in integer
    '''
    print(x)
    coins = coins.copy()
    coins[0] = 99999999
    for coin in coins: #for each
        sum = 0
        if sum == 0:
            pass
            #x = 10
        sum = sum + coin
    
    print(sum,x)
    return sum


#student:
print("before function:")
mycoins = [2,3,2,3,2,3,2,3,5]
print(mycoins)
sum = count_coins(mycoins)
print("outside function:")
print(mycoins)

# print("------------------")
# print(sum)
# print("------------------")

# print("Sum of coins:", sum)

# sum = count_coins([3,2,5,6])
# print("Sum of coins:", sum)
# sum = count_coins([1,1,1,1,1,])
# print("Sum of coins:", sum)


# print("Sum of coins:", sum)

# #arguments
# #default arguments
# def count_coins_and_notes( coins, notes=0 ):
#     print("Notes:",notes, "coins: ", coins)
#     return coins, notes, 45, 

# print("return vals")
# print( count_coins_and_notes( [4,5]) )

# count_coins_and_notes( [4,5], [4] )
# #return value
# #return multiple values


# #args, kwargs

# def count_coins_and_notes( *args ):
#     print(args)



# print("Args")
# count_coins_and_notes( 1 )
# count_coins_and_notes( "list_me","show_file", "delete",4,5 )

# def count_coins_and_notes_kwargs( **kwargs ):
#     print(kwargs)

# count_coins_and_notes_kwargs(a=1,b=2)


# #scope of variables.