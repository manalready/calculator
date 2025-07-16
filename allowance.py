allowance= 2000
#400 on book
allowance -= 400
print(f"spent ₦400 on books, my balance is now ₦{allowance}")
#found ₦100 
allowance += 100
print(f"found ₦100, my balance is now ₦{allowance}")
#spend ₦250 on snacks
allowance -= 250
print(f"spend ₦250 on snacks, my balance is now ₦{allowance}")
#gave 25% to my brother
allowance -= (25/100) * (allowance)
print(f"i gave 25% to my brother, my balance is now ₦{allowance:.2f}")
#used 1/3 of balance to buy data
allowance -= (1/3) * (allowance)
print(f"used one-third for data, my balance is now ₦{allowance:.2f}")
#split balance for saving and tithing
allowance //= 2
print(f"i split balance for tithing and savings,my balance is now ₦{allowance:.2f}")
#remove all complete 100 note
allowance %=100
print(f"final remaining after remove all ₦100 notes: ₦{allowance:.2f}")


