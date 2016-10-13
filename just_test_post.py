#encoding:utf-8
from Controller.Api import Common
from Util.File import Config

param = {'return': '1', 'uid': '1417842', 'tag_id': '18', 'filename_0': open('D:\\wy_auto\\Config\\1.jpg', 'rb'), 'progressId': '5', 'otime': '1425368542', 'liveId': '839640', 'imgCount': '1', 'to8to_token': '1417842_974fc2d2ece94d0edcd26f3cc808fa7a', 'content': '繁华的世界开放活动时间开发繁华的世界开放活动时间开发活动时间看后付款的角色发挥', 'version': '2.5', 'products': '1626', 'action': 'addDiaries', 'ownerId': '1417842', 'model': 'live'}







print Common.revoke_api_request(param)