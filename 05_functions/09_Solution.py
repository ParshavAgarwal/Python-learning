## Geberator Function with Yield
    # write a Generator func. that yields even number upto a specified limit



#yeild is a keyword which also used to GENERATE the value
# y function ko store karta hain and uske STATE ko(mtlb kis position m hain or kya kar raha hain) bhi memory m rakhta hain
# alag alag loop alag jagah store hote hain - y python kar leta hain internally

#yield main vo value generate karta hain aur fir memory main dhyan bhi rakhta hain ki yha tak kaam ho chuka hain.

def even_generator(limit):
    for i in range(2, limit + 1, 2): # python main last wala exclude hota hain 
        yield i # generate i and yaad rakhega ki 2 generate hi gaya hain taaki next 4 generate kare
    

for num in even_generator(10):
    print(num)

# we can store the values of i in list using list.append(i) and return list,, but hme list m nhi chahiye tha