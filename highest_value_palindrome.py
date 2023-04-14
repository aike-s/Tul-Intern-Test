def highestValuePalindrome(s, n, k):
    center = None

    if n%2 != 0:
        center = s[n//2]
        s = s[:n//2] + s[n//2+1:]

    middle = len(s)//2
    first_middle = list(s[:middle])
    second_middle = list(s[len(s):middle-1:-1])

    for i in range(0, middle):
        if first_middle[i] == second_middle[i]:
            continue
        elif first_middle[i] != second_middle[i] and k != 0:
            second_middle[i] = first_middle[i]
            k -= 1
        else:
            return -1
        
    if center:
        first_middle.append(center)
    
    second_middle.reverse()
    final_s = ''.join(first_middle + second_middle)
    
    return final_s

      
def read_input():
    line = 0
    while True:
        line += 1
        user_input = input()
        if line == 1:
            n = int(user_input.split(' ')[0])
            k = int(user_input.split(' ')[1])
        else:
            s = user_input
            break

    answer = highestValuePalindrome(s=s, n=n, k=k)
    
    print(answer)


if __name__ == "__main__":
    #answer = highestValuePalindrome("2432", 4, 1)
    #print(answer)
    read_input()