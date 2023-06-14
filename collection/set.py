##skills = set()
##
##if not skills:
##    print('Empty sets are falsy')
    
##skills = set(['Problem solving','Critical Thinking'])
##print(skills)

##ratings = {1, 2, 3, 4, 5}
##size = len(ratings)
##
##print(size)    

##ratings = {1, 2, 3, 4, 5}
##rating = 1
##
##if rating in ratings:
##    print(f'The set contains {rating}')

##ratings = {1, 2, 3, 4, 5}
##rating = 6
##
##if rating not in ratings:
##    print(f'The set does not contain {rating}')

##skills = {'Python programming', 'Software design'}
##skills.add('Problem solving')
##
##print(skills)

##skills = {'Problem solving', 'Software design', 'Python programming'}
##skills.discard('Java')

skills = {'Problem solving', 'Software design', 'Python programming'}

for index, skill in enumerate(skills):
    print(f"{index}.{skill}")
