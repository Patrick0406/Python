CNBankCard 中国各大银行卡号查询

通过银行卡卡号解析出 发卡行 和 银行卡类别（储蓄卡/信用卡），返回值为JSON数据。

获取方式

支付宝提供的接口。按以下格式发送HTTP请求即可。

curl "https://ccdcapi.alipay.com/validateAndCacheCardInfo.json?_input_charset=utf-8&cardNo=银行卡卡号&cardBinCheck=true"
