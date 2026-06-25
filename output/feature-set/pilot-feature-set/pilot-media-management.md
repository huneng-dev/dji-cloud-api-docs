---
source: https://developer.dji.com/doc/cloud-api-tutorial/cn/feature-set/pilot-feature-set/pilot-media-management.html
path: feature-set/pilot-feature-set/pilot-media-management
---

##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/feature-set/pilot-feature-set/pilot-media-management.html#%E5%8A%9F%E8%83%BD%E6%A6%82%E8%BF%B0) 功能概述
媒体库功能集主要是DJI Pilot 2或大疆机场把飞行器上的媒体文件（图片/视频）下载到遥控器/机场的本地存储，然后再通过网络上传到三方服务器的过程。媒体上传包含自动上传和手动上传功能。
我们提供了媒体文件上传功能的Demo，实现效果可以点击[功能预览视频open in new window](https://developer.dji.com/doc/cloud-api-tutorial/cn/quick-start/function-display-video.html)查看视频。通过该视频可以了解到如何进行对象存储的配置、如何打开自动上传开关、文件自动上传与手动上传的操作流程等。
![](https://terra-1-g.djicdn.com/84f990b0bbd145e6a3930de0c55d3b2b/admin/doc/2b7346f7-7631-404e-8bbb-0b1d99255cac.png)   
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/feature-set/pilot-feature-set/pilot-media-management.html#%E4%BA%A4%E4%BA%92%E6%97%B6%E5%BA%8F) 交互时序
DJI Pilot2Cloud ServerObject Storagealt[文件已存在云端][文件未存在云端]文件快传POST /media/api/v1/workspaces/{workspace_id}/fast-upload获取已存在文件的精简指纹POST /media/api/v1/workspaces/{workspace_id}/files/tiny-fingerprints判断文件是否存在于云端返回结果文件已存在获取文件上传临时凭证POST /storage/api/v1/workspaces/{workspace_id}/sts返回凭证API中“credentials”字段执行文件上传返回上传结果媒体文件上传结果上报POST /media/api/v1/workspaces/{workspace_id}/upload-callback返回上传结果DJI Pilot2Cloud ServerObject Storage
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/feature-set/pilot-feature-set/pilot-media-management.html#%E6%8E%A5%E5%8F%A3%E8%AF%A6%E7%BB%86%E5%AE%9E%E7%8E%B0) 接口详细实现
  * [JSBridgeopen in new window](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/jsbridge.html)  
加载Media媒体库模块  
在使用媒体库模块功能之前，需要预先在H5页面中通过JSBridge设置好工作空间信息（workspaceId），配置好api模块，然后加载DJI Pilot 2的media模块。开发者可以考虑在上下线登录阶段直接添加加载media模块的接口。
  * [媒体管理（HTTPS）open in new window](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/media-management/fast-upload.html)
    * 文件快传  
由于传输文件时可能会存在云端已有的图片，那么DJI Pilot 2或机场在上传文件时，会启动文件快传接口，服务端需要检查该文件是否已经上传存在了，如果存在了，直接返回上传成功。
    * 获取已存在文件的精简指纹  
通过精简指纹校验，确认文件是否已经上传
    * 获取上传临时凭证  
每次媒体上传时，需要向服务端获取临时文件上传凭证，这样DJI Pilot 2在上传时会带上该凭证给对象存储服务进行校验。
    * 媒体文件上传结果上报  
媒体文件传输结束后，DJI Pilot会调用该接口向服务端告知对应的媒体文件上传结果。
    * 文件组上传完成后回调