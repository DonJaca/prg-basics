facebook = True
twitter = False
instagram = True
print('You are a good influencer!' if sum((facebook, twitter, instagram)) >= 2
      else 'You are not a good influencer.')
