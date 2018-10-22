def solution(S):
    substring = ''

    '''If S has something in it, it will verify each char'''
    if S:
        for i in S:
            '''When it finds a {[( char, 
            it adds to a string substring the opposite char )]}'''
            if i == '{':
                substring += '}'
            if i == '[':
                substring += ']'
            if i == '(':
                substring += ')'

            '''When it finds the )]} char, 
            verifies if he last closing )]} char is the same.
            If true, removes it from the substring, 
            if false the string S does not match the criteria'''
            if i == '}':
                if substring.endswith('}'):
                    substring = substring[:-1]
                else:
                    return 0
            if i == ']':
                if substring.endswith(']'):
                    substring = substring[:-1]
                else:
                    return 0
            if i == ')':
                if substring.endswith(')'):
                    substring = substring[:-1]
                else:
                    return 0

        '''If substring has something in it,
        it means not all the {[( chars have the opposite )]} char'''
        if substring:
            return 0
        else:
            return 1
    else:
        return 0


S = 'cena[5]]'
print(solution(S))

S = '1{}2[[A]]'
print(solution(S))

S = '(teste)'
print(solution(S))

S = '}teste{'
print(solution(S))
