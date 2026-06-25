---
source: https://developer.dji.com/doc/cloud-api-tutorial/cn/feature-set/dock-feature-set/custom-flight-area.html
path: feature-set/dock-feature-set/custom-flight-area
---

##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/feature-set/dock-feature-set/custom-flight-area.html#%E5%8A%9F%E8%83%BD%E6%A6%82%E8%BF%B0) 功能概述
上云 API 开放自定义飞行区功能。用户可以将敏感地点设定为禁飞区，并将这些信息同步给项目内的大疆机场。当无人机执行任务时，它会自动绕行禁飞区，从而确保作业的安全和规范性。本功能通过自定义飞行区文件圈定飞行器的飞行区域，**点击下载[自定义飞行区文件协议模板open in new window](https://terra-1-g.djicdn.com/fee90c2e03e04e8da67ea6f56365fc76/SDK%20%E6%96%87%E6%A1%A3/CloudAPI/custom-flight-area-file-template.json)**。
该功能支持用户在地图上规划自定义飞行区。自定义飞行区包括两种类型：
  1. 自定义作业区：在自定义作业区内，飞行器可以起飞并进行作业，但无法飞出该区域。
  2. 自定义限飞区：在自定义限飞区外，飞行器可以进行作业，但无法飞入该区域。
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/feature-set/dock-feature-set/custom-flight-area.html#%E4%BA%A4%E4%BA%92%E6%97%B6%E5%BA%8F%E5%9B%BE) 交互时序图
Cloud ServerDJI DockAircraftWeb Pagealt[文件版本判断一致][文件版本判断不一致（不一致则以云端的版本为准）]打包自定义飞行区文件，上传到存储桶通知自定义飞行区文件更新 Topic: thing/product/{gateway_sn}/services Method: flight_areas_update拉取自定义飞行区文件信息 Topic: thing/product/{gateway_sn}/requests Method: flight_areas_get返回云端最新的自定义飞行区信息开启飞行器，请求升级自定义飞行区数据，携带文件下载地址和文件MD5返回飞行器自身自定义飞行区的文件信息自定义飞行区文件版本判断上报同步完成 Topic: thing/product/{gateway_sn}/events Method: flight_areas_sync_progress返回已经完成同步状态上报同步进行中，进入数据同步升级从存储桶下载最新文件，上传自定义飞行区数据发送自定义飞行区同步进度状态上报自定义飞行区同步进度状态 Topic: thing/product/{gateway_sn}/events Method: flight_areas_sync_progress本地状态持久化处理推送自定义飞行区最新同步进度状态飞行器向机场推送飞行区信息飞行区告警信息推送 Topic: thing/product/{gateway_sn}/events Method: flight_areas_drone_location上报飞行器和各个区域的告警信息Cloud ServerDJI DockAircraftWeb Page
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/feature-set/dock-feature-set/custom-flight-area.html#%E6%8E%A5%E5%8F%A3%E8%AF%A6%E7%BB%86%E5%AE%9E%E7%8E%B0) 接口详细实现
[自定义飞行区open in new window](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock2/custom-flight-area.html)