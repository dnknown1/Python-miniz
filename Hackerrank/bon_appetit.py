'''Anna and Brian are sharing a meal at a restuarant and they agree to split the bill equally. Brian wants to order something that Anna is allergic to though, and they agree that Anna won't pay for that item. Brian gets the check and calculates Anna's portion. You must determine if his calculation is correct.

For example, assume the bill has the following prices:b[] . Anna declines to eat item k which costsb[k] . If Brian calculates the bill correctly, Anna will pay p . If he includes the cost of b[k], he will calculate g. In the second case, he should refund (g-p) to Anna.'''


#O(n)
def bon_appetit(b,k,g):
	return (g - (sum(b)-b[k]) >> 1) if g <  (sum(b)-b[k]) >> 1 else 'Bon Appetit'

print(bon_appetit([3,10,2,9],1, 12))
print(ok)
