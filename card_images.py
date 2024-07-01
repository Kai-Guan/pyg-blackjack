CARD_IMAGES = [[] for i in range(13)]
n = ['ace','2','3','4','5','6','7','8','9','10','jack','queen','king']
for i, rank in enumerate(n):
    for suit in ['clubs','diamonds','hearts','spades']:
        CARD_IMAGES[i].append(f'cards\{rank}_of_{suit}.png')