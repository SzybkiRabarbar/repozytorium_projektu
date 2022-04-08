
def sum_for_list(lst:list): #input: list of integers(positive and negative)
    content=[]
    factors = set()
    for number in lst:
        if number<0: number=-number
        factors.update([divider for divider in range(number+1) if divider and number%divider==0])
    for factor in factors:
        numbers_divided_by_factor = [number for number in lst if number%factor==0]
        content.append([factor, sum(numbers_divided_by_factor)])
        
    return content # return: list of list with factors with summary of numbers from input (if number is divided by factor)