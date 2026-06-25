<!-- source: https://developer.dji.com/doc/cloud-api-tutorial/cn/feature-set/pilot-feature-set/pilot-third-party-app.html -->
<!-- path: feature-set/pilot-feature-set/pilot-third-party-app -->

##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/feature-set/pilot-feature-set/pilot-third-party-app.html#%E5%8A%9F%E8%83%BD%E6%A6%82%E8%BF%B0) 功能概述
对于使用DJI Pilot 2无法满足的业务场景，开发商可以自己开发一个轻型App与DJI Pilot一起使用，例如需要用遥控器进行对讲、特殊的任务命令、工单等等，这样对于终端用户来说，可以直接通过DJI Pilot的webview页面打开三方的APP，而开发商只需要在打开webview页面时，自动调用唤醒第三方App的JSBridge接口即可。详细的配置可以参考链接：[Android webview 中跳转第第三方Appopen in new window](https://developer.aliyun.com/article/595078)。
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/feature-set/pilot-feature-set/pilot-third-party-app.html#%E6%8E%A5%E5%8F%A3%E8%AF%A6%E7%BB%86%E5%AE%9E%E7%8E%B0) 接口详细实现
[JSBridgeopen in new window](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/jsbridge.html) 跳转至第三方App `window.open('scheme://host...', arg)`