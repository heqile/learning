# Binary search to find n th root
# sometime we need to find the n th root of a large number, standard python lib will not match our need. 
# cf.https://stackoverflow.com/questions/55436001/cube-root-of-a-very-large-number-using-only-math-library 

def find_invpow(x,n):
    """Finds the integer component of the n'th root of x,
    an integer such that y ** n <= x < (y + 1) ** n.
    """
    high = 1
    while high ** n < x:
        high *= 2
    low = high//2
    while low < high:
        mid = (low + high) // 2
        if low < mid and mid**n < x:
            low = mid
        elif high > mid and mid**n > x:
            high = mid
        else:
            return mid
    return mid + 1

# example:
# a=780865154948750571515875825956842965597268480061942498223759415931178548538528991182487495101556011494286950683286512165475038389107892269787484651054279065941410737793736223804092347531386151065849807188034668245557897119294115024094420977925386642701753372658008076601701
# result=9208566198168854769137135900129825812636831889153009607082441577495048346488797274341323901