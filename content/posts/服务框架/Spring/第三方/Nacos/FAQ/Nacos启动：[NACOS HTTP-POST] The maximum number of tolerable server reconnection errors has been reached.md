---
book_id: 28973507
cnblog_id: '17913125'
doc_id: 88576360
tags:
- 服务框架
- Spring
- 第三方
- Nacos
- FAQ
title: Nacos启动：[NACOS HTTP-POST] The maximum number of tolerable server reconnection
  errors has been reached
---
<a name="JMeBy"></a>
## 一、表象
![image.png](https://cdn.nlark.com/yuque/0/2022/png/26501265/1659664430669-0f1e4750-08a9-44fb-acf0-560508b66753.png#averageHue=%23f0da8e&clientId=uaee44362-6bc2-4&from=paste&height=303&id=u38aa3127&originHeight=606&originWidth=3154&originalType=binary&ratio=1&rotation=0&showTitle=false&size=403560&status=done&style=none&taskId=u7ad67acd-a05e-421b-8a84-467562f4726&title=&width=1577)
<a name="oxkTY"></a>
## 二、分析
源码：
```java
public HttpRestResult<String> httpPost(String path, Map<String, String> headers, Map<String, String> paramValues,
            String encode, long readTimeoutMs) throws Exception {
    final long endTime = System.currentTimeMillis() + readTimeoutMs;
    injectSecurityInfo(paramValues);
    String currentServerAddr = serverListMgr.getCurrentServerAddr();
    int maxRetry = this.maxRetry;
    HttpClientConfig httpConfig = HttpClientConfig.builder()
        .setReadTimeOutMillis(Long.valueOf(readTimeoutMs).intValue())
        .setConTimeOutMillis(ConfigHttpClientManager.getInstance().getConnectTimeoutOrDefault(3000)).build();
    do {

        try {
            Header newHeaders = getSpasHeaders(paramValues, encode);
            if (headers != null) {
                newHeaders.addAll(headers);
            }
            HttpRestResult<String> result = NACOS_RESTTEMPLATE
                .postForm(getUrl(currentServerAddr, path), httpConfig, newHeaders, paramValues, String.class);

            // 错误码 HTTP_INTERNAL_ERROR = 500 || HTTP_BAD_GATEWAY = 502 || HTTP_UNAVAILABLE = 503 为异常
            if (isFail(result)) {
                LOGGER.error("[NACOS ConnectException] currentServerAddr: {}, httpCode: {}", currentServerAddr,
                             result.getCode());
            } else {
                // Update the currently available server addr
                serverListMgr.updateCurrentServerAddr(currentServerAddr);
                // 应从这里返回，否则会进入重试
                return result;
            }
        } catch (ConnectException connectException) {
            LOGGER.error("[NACOS ConnectException httpPost] currentServerAddr: {}, err : {}", currentServerAddr,
                         connectException.getMessage());
        } catch (SocketTimeoutException socketTimeoutException) {
            LOGGER.error("[NACOS SocketTimeoutException httpPost] currentServerAddr: {}， err : {}",
                         currentServerAddr, socketTimeoutException.getMessage());
        } catch (Exception ex) {
            LOGGER.error("[NACOS Exception httpPost] currentServerAddr: " + currentServerAddr, ex);
            throw ex;
        }

        // 重试逻辑
        if (serverListMgr.getIterator().hasNext()) {
            currentServerAddr = serverListMgr.getIterator().next();
        } else {
            // maxRetry = 3
            maxRetry--;
            if (maxRetry < 0) {
                throw new ConnectException(
                    "[NACOS HTTP-POST] The maximum number of tolerable server reconnection errors has been reached");
            }
            serverListMgr.refreshCurrentServerAddr();
        }

    } while (System.currentTimeMillis() <= endTime);

    LOGGER.error("no available server, currentServerAddr : {}", currentServerAddr);
    throw new ConnectException("no available server, currentServerAddr : " + currentServerAddr);
}
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/26501265/1659665464536-d044ba60-e0ff-482a-9ec5-6da82943a272.png#averageHue=%23faf8f8&clientId=uaee44362-6bc2-4&from=paste&height=662&id=u481a936d&originHeight=1324&originWidth=1904&originalType=binary&ratio=1&rotation=0&showTitle=false&size=353430&status=done&style=none&taskId=u3ebc2b6c-23e5-4837-845f-40cc3aa16a1&title=&width=952)
<a name="XDCep"></a>
## 三、解决
将配置文件`application.yml`更改为`bootstrap.yml`

