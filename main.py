#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from jd_assistant import Assistant

if __name__ == '__main__':
    """
    重要提示：此处为示例代码之一，请移步下面的链接查看使用教程👇
    https://github.com/tychxn/jd-assistant/wiki/1.-%E4%BA%AC%E4%B8%9C%E6%8A%A2%E8%B4%AD%E5%8A%A9%E6%89%8B%E7%94%A8%E6%B3%95
    """

    sku_ids = '100018640844'  # 商品id
    area = '22_1930_50948_52157'  # 区域id
    asst = Assistant()  # 初始化
    asst.login_by_cookieString('shshshfpa=8b257df8-2b37-cc1b-3876-5893bc4b63e9-1610602086; shshshfpb=t49povbqrojZaUTLkiyvtww%3D%3D; __jdu=456735623; pinId=NyozGQScbNI; pin=zg_vip; unick=zg_vip; _tp=t2ytaFS9aCz0Mc%2FHdtnE3w%3D%3D; _pst=zg_vip; areaId=22; user-key=f6f2a91e-d1e7-40b2-9d98-a6c3b592c1ae; ipLocation=%u56db%u5ddd; __jdv=76161171|direct|-|none|-|1615863684940; mt_xid=V2_52007VwYWVVtaVl0cSykOBzAHRlFaX04NFkkdQABmBkVODlkFWgMdTl4BNFRFBwkPAVgvShhfBXsCEE5dX0NaGEIcVQ5lBCJSbVhiWBpOGF4DYQETUm1dUVwc; ceshi3.com=000; cn=0; shshshfp=bf9d21c40bb8fec0e32ac05784dfa6d3; ipLoc-djd=22-1930-50948-52157; __jdc=122270672; __jda=122270672.456735623.1610602084.1616032169.1616120729.19; wlfstk_smdl=k768x8ndc4e9ph9om7az9x0lvt39mql7; 3AB9D23F7A4B3C9B=5TFN4KA3OZ5HMLRAEUA7VKDL3L44GIHLMNVN2PBIBFXGUJEMH3A5DJBEYDFXUXECDR22I7LERPTJL4L7EG23XDUGT4; TrackID=1koXNjPZqRp7TjbAZML99eQyMB-CtyyejN3DB5VU_FgsijsFy6Cn_8mQeczbHk2_qTYUKyS1zQzua7JXqsPHsn3BYKV0aIhp3lKOLv35QVO8wzwW1ZnClg-PXkH-IeB2N; thor=524A4B2233BB30EA2F3A0A22953B428A316FCBED385DE5494C629AC8B811082EAD616A971485E383F43BE4495A0890623D44695C12F8B0FB48E940FFAE9FDE9D41B9D69E6D50D2001E2830EF9A8FD4E271FCD507C440754715F3E809B2F52C7B8A0A8DE1A8044EB99533003875D4ECF85211BCDCDEC3468BBA7554985EB2469B; __jdb=122270672.7.456735623|19.1616120729')
    asst.login_by_QRcode()  # 扫码登陆
    
    # (self, sku_id, buy_time, retry=4, interval=4, num=1):
    #k40 幻境 
    asst.exec_seckill_by_time('100018640796', '2021-03-19 10:00:00.001', retry=10, interval= 0.1)
    #motorola edge s
    # asst.exec_reserve_seckill_by_time('100018071914', '2021-03-18 10:00:00.001', retry=10, interval= 6)
    # asst.exec_seckill_by_time('100018071914', '2021-03-18 10:00:00.001')
    # asst.exec_reserve_seckill_by_time('100018640796', '2021-03-8 10:00:00.001', retry=10, interval= 6)

# ''
    # sku_ids = '100018071914' 
    # asst.buy_item_in_stock(sku_ids=sku_ids, area=area, wait_all=False, stock_interval=5)  # 根据商品是否有货自动下单
    # 6个参数：
    # sku_ids: 商品id。可以设置多个商品，也可以带数量，如：'1234' 或 '1234,5678' 或 '1234:2' 或 '1234:2,5678:3'
    # area: 地区id
    # wait_all: 是否等所有商品都有货才一起下单，可选参数，默认False
    # stock_interval: 查询库存时间间隔，可选参数，默认3秒
    # submit_retry: 提交订单失败后重试次数，可选参数，默认3次
    # submit_interval: 提交订单失败后重试时间间隔，可选参数，默认5秒
