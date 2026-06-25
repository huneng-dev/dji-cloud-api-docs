---
source: https://developer.dji.com/doc/cloud-api-tutorial/cn/feature-set/dock-feature-set/dock-media-management.html
path: feature-set/dock-feature-set/dock-media-management
---

##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/feature-set/dock-feature-set/dock-media-management.html#%E5%8A%9F%E8%83%BD%E6%A6%82%E8%BF%B0) 功能概述
媒体库功能集主要是DJI Pilot 2或大疆机场把飞行器上的媒体文件（图片/视频）下载到遥控器/机场本地存储，然后再通过网络上传到三方服务器的过程。媒体上传包含自动上传和手动上传功能，对于机场只有自动上传功能。
使用最新版本大疆机场 2 的固件：
  * 产生的视频文件（红外、可见光、分屏三种视频文件）中会包含飞行器的位置和高度、云台姿态等信息（和旧固件中随视频文件产生的 SRT 字幕文件中的信息内容一致）。
  * 完成一个航线飞行任务后，飞行器在 SD 卡中产生的 PPK 文件（.obs、.rtk、.mrk、.nav）和 RTCM 数据（.dat 格式）也会跟随媒体文件一起上传回云端存储桶。
![](https://terra-1-g.djicdn.com/84f990b0bbd145e6a3930de0c55d3b2b/admin/doc/2b7346f7-7631-404e-8bbb-0b1d99255cac.png)   
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/feature-set/dock-feature-set/dock-media-management.html#%E4%BA%A4%E4%BA%92%E6%97%B6%E5%BA%8F) 交互时序
DJI DockCloud ServerObject Storage获取上传临时凭证Topic: thing/product/{gateway_sn}/requestsMethod: storage_config_get云端下发临时凭证Topic: thing/product/{gateway_sn}/requests_replyMethod: storage_config_get执行文件上传返回上传结果媒体文件上传结果上报Topic: thing/product/{gateway_sn}/eventsMethod: file_upload_callback返回上传结果Topic: thing/product/{gateway_sn}/events_replyMethod: file_upload_callbackDJI DockCloud ServerObject Storage
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/feature-set/dock-feature-set/dock-media-management.html#%E6%8E%A5%E5%8F%A3%E8%AF%A6%E7%BB%86%E5%AE%9E%E7%8E%B0) 接口详细实现
[媒体管理（MQTT）open in new window](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock1/file.html)
  * 获取临时凭证  
每次媒体文件上传时，需要向服务端获取临时文件上传凭证，这样机场在上传时会带上该凭证给对象存储服务进行校验。
  * 媒体文件上传结果上报  
媒体文件传输结束后，机场会调用该接口向服务端告知对应的媒体文件上传结果。