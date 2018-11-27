# Import the necessary packages and modules
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

import pdb;pdb.set_trace()

# # Prepare the data
# x = np.linspace(0, 10, 100)
# x = [1,2,5]  # will leave 3 and 4 empty :D
# y = [1,4,9]
# # Plot the data
# plt.bar(x, y, label='bar')
#
# # Add a legend
# plt.legend()

# Show the plot
# plt.show()
# print x
# plt.savefig('myfilename.png')
#

cnt_amount = {}

news_idx_to_nids = {}

num_news = 0
num_videos = 0



# with open('short_201811151320.cluster.nid') as fp:
with open('201811151320.cluster.nid') as fp:
    news_id = 1
    for line in fp:

        # print line
        news_items = line.strip().split()
        news_items_cnt = len(news_items)
        if news_items_cnt not in cnt_amount:
            cnt_amount[news_items_cnt] = 1
        else:
            cnt_amount[news_items_cnt] += 1
        if news_items_cnt == 98:
            print line

        news_idx_to_nids[news_id] = news_items
        has_text = False
        has_video = False
        for item in news_items:
            if item[0] == 'v' or item[0:2] == 'cv':
                num_videos += 1
                has_text = True
            elif item[0] == 'n' or item[0:2] == 'cn':
                num_news += 1
                has_video = True
            else:
                print 'ERROR'
                print item

        if news_items_cnt > 30 and news_items_cnt < 40 and has_text and has_video:
            print 'Good'
            print news_items
        news_id += 1

        # break

    print 'news_id: ', news_id-1
    print 'news: ', num_news
    print 'videos: ', num_videos
    # print cnt_amount
    x = cnt_amount.keys()
    y = [cnt_amount[k] for k in x]
    x_right = x[len(x)/2:]
    y_right = y[len(y)/2:]
    x_left = x[:len(x)/2]
    y_left = y[:len(y)/2]

    x_mid = x[len(x)/4:3*len(x)/4]
    y_mid = y[len(y)/4:3*len(y)/4]

    print x
    print y


    # zipped = zip(x,y)
    # sorted_zipped = sorted(zipped, key=lambda x: x[1], reverse=True)
    plt.bar(['Total', 'Text/Pictures', 'Videos'], [num_news+num_videos, num_news, num_videos], label='bar')
    plt.legend(['# of News'])
    # plt.xlabel('# of news')
    plt.ylabel('amount of news')
    plt.title('Text/Video Distribution')

    plt.savefig('tmp.png')
