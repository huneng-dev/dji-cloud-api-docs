<!-- source: https://developer.dji.com/doc/cloud-api-tutorial/cn/feature-set/pilot-feature-set/pilot-livestream.html -->
<!-- path: feature-set/pilot-feature-set/pilot-livestream -->

##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/feature-set/pilot-feature-set/pilot-livestream.html#%E5%8A%9F%E8%83%BD%E6%A6%82%E8%BF%B0) 功能概述
直播功能主要是把无人机相机负载和大疆机场的视频码流发给第三方云平台进行播放，用户可以方便的在远程web页面点击直播。
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/feature-set/pilot-feature-set/pilot-livestream.html#%E6%94%AF%E6%8C%81%E7%9A%84%E7%9B%B4%E6%92%AD%E7%B1%BB%E5%9E%8B) 支持的直播类型  
| 直播类型  | 描述  |  
| --- | --- |  
| Agora声网  | 声网Agora成立于2013年，是实时音视频云行业开创者和全球领先的专业PaaS服务商。  
开发者只需简单调用Agora API，30分钟即可在应用内构建多种实时音视频互动场景。  
大疆司空2也是基于声网的“极速直播”功能进行码流推送，整体直播延迟比较低，效果好。  
对于三方云私有化部署，Agora也提供了混合云部署模式，码流和数据都在客户的私有服务器中，然后通过网闸打通一个链路到Agora的运维公有云，这个链路通道主要是用来对私有化部署的服务进行升级和运维。  |  
| RTMP  | RTMP是Real Time Messaging Protocol（实时消息传输[协议open in new window](https://baike.baidu.com/item/%E5%8D%8F%E8%AE%AE/13020269)）的首字母缩写。该协议基于TCP，是一个协议族，包括RTMP基本协议及RTMPT/RTMPS/RTMPE等多种变种。RTMP是一种设计用来进行实时数据通信的网络协议，主要用来在Flash/AIR平台和支持RTMP协议的流媒体/交互服务器之间进行音视频和数据通信。  
 |  
| RTSP  | RTSP（Real Time Streaming Protocol）是 TCP/IP 协议体系中的一个应用层协议，该协议定义了一对多应用程序如何有效地通过 IP 网络传送多媒体数据。RTSP在体系结构上位于RTP和RTCP之上，它使用TCP或UDP完成数据传输。HTTP与RTSP相比，HTTP传送HTML，而RTSP传送的是多媒体数据。  |  
| GB28181  | GB/T 28181-2016 是中国大陆地区对于安防视频设备接入平台的一种传输控制规范，对于已有28181下联网关的服务器，可以直接通过该协议把DJI行业设备的码流推到服务器中。  |  
| WebRTC/WHIP  | WebRTC [（Web Real-Time Communication）open in new window](https://docs.dolby.io/streaming-apis/docs/webrtc-whip)是一种支持网页浏览器进行实时视频和音频流的通信技术，它提供接近实时的音视频流，确保用户体验的流畅性。该技术广泛应用于在线会议、在线教育、远程医疗等高实时通信的场景。  
WHIP [（WebRTC-HTTP Ingestion Protocol）open in new window](https://millicast.medium.com/whip-the-magic-bullet-for-webrtc-media-ingest-57c2b98fb285)是一个基于 HTTP 的协议，旨在为 WebRTC 发布者和流媒体服务器之间提供一个标准化的信令协议，以便于将 WebRTC 流引入流媒体服务器。它允许基于 WebRTC 的内容输入到流媒体服务器或 CDN 中。  |  
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/feature-set/pilot-feature-set/pilot-livestream.html#%E7%9B%B4%E6%92%AD%E6%80%BB%E4%BD%93%E6%A1%86%E6%9E%B6) 直播总体框架
![](https://stag-terra-1-g.djicdn.com/7774da665e07453698314cc27c523096/admin/doc/0ba6ce39-4337-46df-99da-f9905bfd53f6.svg)   
如上图所示，无人机飞行平台并不直接连接第三方云平台，中间是通过DJI Pilot 2或大疆机场进行转流转发，遥控器和机场与无人机之间的通信还是用DJI私有图传ocusync链路。
第三方云平台需要预先部署MQTT网关以及流媒体服务器，DJI推流协议支持 Agora/RTMP/RTSP/GB28181 4种模式，其中MQTT网关主要用来做消息通信，配置信息设置和读取。
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/feature-set/pilot-feature-set/pilot-livestream.html#%E4%BA%A4%E4%BA%92%E6%97%B6%E5%BA%8F%E5%9B%BE) 交互时序图
###  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/feature-set/pilot-feature-set/pilot-livestream.html#%E5%8A%A0%E8%BD%BD%E7%9B%B4%E6%92%AD%E6%A8%A1%E5%9D%97) 加载直播模块
DJI Pilot 2Pilot WebviewMQTT 网关Cloud Server三方 Web 页面直播能力包含在该topic中，需要服务端订阅后解析解析state topic中的live_capacity结构体，并保存在数据库中WEB页面通过JSBridge:platformLoadComponent加载Pilot的直播模块特别注意：使用直播功能需要预先通过JSBridge接口加载PILOT的直播模块订阅 "thing/product/{gateway_sn}/services" topic订阅 "thing/product/{gateway_sn}/osd" topic订阅 "thing/product/{gateway_sn}/services_reply" topic订阅 "thing/product/{gateway_sn}/services" topic推送 "thing/product/{gateway_sn}/state" topic推送 "thing/product/{gateway_sn}/state" topicDJI Pilot 2Pilot WebviewMQTT 网关Cloud Server三方 Web 页面
###  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/feature-set/pilot-feature-set/pilot-livestream.html#%E4%BA%91%E7%AB%AF%E8%B0%83%E7%94%A8%E5%8D%8F%E8%AE%AE%E5%8F%91%E8%B5%B7%E7%9B%B4%E6%92%AD) 云端调用协议发起直播
DJI Pilot 2Pilot PreviewMQTT 网关Cloud Server三方 Web 页面查询本地数据库中设备直播能力解析校验services topic校验内容包括 相机是否正在解码、是否在飞行控制界面进去直播页面后，发送查询设备直播能力给服务端返回直播能力数据发起点播操作发送method="live_start_push"的services topic推送services topicPublish "service_reply" topic推送service_reply topicPublish 包含live_status字段的osd topic推送osd topicDJI Pilot 2Pilot PreviewMQTT 网关Cloud Server三方 Web 页面
###  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/feature-set/pilot-feature-set/pilot-livestream.html#%E6%A0%A1%E9%AA%8C%E6%88%90%E5%8A%9F) 校验成功
DJI Pilot 2Pilot WebviewMQTT 网关Cloud Server三方 Web 页面开启编码器向直播服务器推流通过service_reply topic上报开启成功推送开启直播成功开始拉流DJI Pilot 2Pilot WebviewMQTT 网关Cloud Server三方 Web 页面
###  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/feature-set/pilot-feature-set/pilot-livestream.html#%E6%A0%A1%E9%AA%8C%E5%A4%B1%E8%B4%A5) 校验失败
DJI Pilot 2Pilot WebviewMQTT 网关Cloud Server三方 Web 页面通过service_reply topic上报发起直播失败以及原因推送失败消息DJI Pilot 2Pilot WebviewMQTT 网关Cloud Server三方 Web 页面
###  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/feature-set/pilot-feature-set/pilot-livestream.html#app%E7%AB%AF%E8%B0%83%E7%94%A8jsbridge%E5%8F%91%E8%B5%B7%E7%9B%B4%E6%92%AD) App端调用JSBridge发起直播
DJI Pilot 2Pilot WebviewMQTT 网关Cloud Server三方 Web 页面用户在飞行控制界面选择开始直播或者结束直播进入Pilot Webview页面，拉取服务端直播配置参数返回直播参数设置手动直播参数JSBridge:liveshareSetConfig首次设置后立即发起直播推流直播推流拉流显示播放DJI Pilot 2Pilot WebviewMQTT 网关Cloud Server三方 Web 页面
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/feature-set/pilot-feature-set/pilot-livestream.html#%E6%8E%A5%E5%8F%A3%E8%AF%A6%E7%BB%86%E5%AE%9E%E7%8E%B0) 接口详细实现
  * [JSBridgeopen in new window](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/jsbridge.html)  
    * 加载直播模块  
在使用直播功能之前，需要预先在webview中通过JSBridge加载DJI Pilot 2的直播模块，开发者可以考虑在上下线登录阶段直接添加加载直播模块的接口。
    * App 端调用 JSBridge 手动直播  
对于无需后台直播观看，但是需要在用户使用时，开启直播，把码流传回服务端进行存档分析的场景，可以通过该接口组合，让用户在Pilot 中手动触发直播功能，详细步骤如下：
      1. Pilot 端webview登录第三方云平台后，需要向服务端请求一个流媒体服务器直播地址参数，各个第三方云平台配置不同，也可以直接写死在前端代码中。
      2. 把直播推流参数通过JSBridge接口，发给DJI Pilot 2进行设置。
      3. DJI Pilot 2收到直播配置后，立即发起直播推流，用户可以进入飞行界面查看直播信息，停止直播，重新开始直播等操作。
> **注意：** 采用手动直播方式，推流的画面一直是DJI Pilot 2主画面码流，当飞手切换相机画面时，推流的画面也会跟着变化。
  * [直播功能（MQTT）open in new window](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/mqtt/rc-plus/live.html)  
    * 直播能力更新  
live_capacity这个字段是放在网关设备的物模型中的，同时推送的属性为当设备端有状态变化时才推送。
    * 开始直播  
服务端通过mqtt给设备端发送`method=live_start_push`的指令，这条指令采用的是物模型的service方式交互。
    * 停止直播
    * 设置直播清晰度