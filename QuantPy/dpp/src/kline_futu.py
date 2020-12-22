# -*- coding: utf-8 -*-
"""

"""

from dpp.kline import Kline
from futu import *


class KlineFutu(Kline):

    def req_hist_kline(self, start, end, ktype=KLType.K_1M, autype=AuType.QFQ):
        quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
        # request first page, default 1000 bar per page
        ret, data, page_req_key = quote_ctx.request_history_kline(self.code, start, end,
                                                                  ktype, autype)
        if ret == RET_OK:
            print(data.head())
        else:
            print('error:', data)

        # request rest data
        while page_req_key is not None:
            print('*************************************')
            ret, temp_data, page_req_key = quote_ctx.request_history_kline(self.code, start, end,
                                                                           ktype, autype, page_req_key=page_req_key)
            if ret == RET_OK:
                print(temp_data.head())
                data = data.append(temp_data)
            else:
                print('error:', temp_data)
        print('All pages are finished!')
        quote_ctx.close()  # close request

        # save data to csv
        data.to_csv('data/' + self.src + '/' + self.code + '/temp.csv')
