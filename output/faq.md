---
source: https://developer.dji.com/doc/cloud-api-tutorial/cn/faq.html
path: faq
---

##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/faq.html#%E5%A6%82%E4%BD%95%E5%9C%A8%E8%88%AA%E7%BA%BF%E9%A3%9E%E8%A1%8C%E4%BB%BB%E5%8A%A1%E4%B8%AD%E4%BD%BF%E7%94%A8%E5%A4%A7%E7%96%86%E6%9C%BA%E5%9C%BA-2-%E5%92%8C%E5%A4%A7%E7%96%86%E6%9C%BA%E5%9C%BA-3-%E7%9A%84%E5%AE%9A%E5%90%91%E6%8B%8D%E7%85%A7) 如何在航线飞行任务中使用大疆机场 2 和大疆机场 3 的定向拍照？
定向拍照 `orientedShoot` 相比原来的精准拍照 `accurateShoot` 机型兼容性更好，执行效率更高。如需把航线文件中的精准拍照转变成定向拍照，需执行以下步骤：
  1. 在动作类型中将精准拍照 `accurateShoot` 改为定向拍照 `orientedShoot` 。
  2. 在航点拍照动作中增加 `actionUUID`。`actionUUID` 由一组 32 位数的 16 进制数字构成，以连字号为分隔符，分为五段，表现形式为：8位-4位-4位-4位-12位，如 7f320139-4fbf-41d1-b3bb-3b9f6f7f334c。
  3. 在航点拍照动作中设置拍照模式 `orientedPhotoMode`，其中 `normalPhoto` 代表普通拍照模式，`lowLightSmartShooting` 代表智能低光拍照模式。智能低光拍照模式适合低光环境下拍摄，适应更多光照条件的作业场景，但拍摄速度会有所降低。
  4. 除 `accurateFrameValid` 字段，将所有 `accurate` 开头的字段全部改成 `oriented` 开头。
> **注意：** 定向拍照支持大疆机场，大疆机场 2和大疆机场 3。
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/faq.html#%E6%9C%BA%E5%9C%BA%E6%89%A7%E8%A1%8C%E8%9B%99%E8%B7%B3%E4%BB%BB%E5%8A%A1%E6%97%B6-b-%E6%8E%A7%E9%81%A5%E6%8E%A7%E5%99%A8%E4%BC%9A%E8%87%AA%E5%B7%B1%E6%96%AD%E5%BC%80%E5%90%97) 机场执行蛙跳任务时，B 控遥控器会自己断开吗？
执行蛙跳任务时，当已经设置了起飞和降落机场，此时 B 控遥控器的连接会被挤占而断开。
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/faq.html#%E4%B8%BA%E4%BB%80%E4%B9%88%E7%AC%AC%E4%B8%89%E6%96%B9%E5%B9%B3%E5%8F%B0%E4%BD%BF%E7%94%A8%E6%9C%BA%E5%9C%BA%E6%89%A7%E8%A1%8C%E4%B8%80%E9%94%AE%E8%B5%B7%E9%A3%9E%E6%88%96%E8%88%AA%E7%BA%BF%E4%BB%BB%E5%8A%A1%E6%97%B6-%E5%87%BA%E7%8E%B0%E7%AD%89%E5%BE%85%E6%97%B6%E9%97%B4%E8%BF%87%E9%95%BF%E7%9A%84%E9%97%AE%E9%A2%98) 为什么第三方平台使用机场执行一键起飞或航线任务时，出现等待时间过长的问题？
**问题现象：** 第三方平台使用机场执行一键起飞或航线任务时，每次起飞前需要检查机场的 “离线地图” 和 “自定义飞行区” 数据与云端是否一致。如果云端不回复该消息，机场会有一个超时等待逻辑，大概会等待 40s。
**解决方案：** 将大疆机场 2 和 Matrice 3D/3TD 的固件升级到 v10.01.32.02 版本。如设备固件需保持在旧版本，可以针对机场的获取离线地图协议（Method: offline_map_get）和自定义飞行区文件获取协议（Method: flight_areas_get）的请求，回复以下内容：
Topic: thing/product/{gateway_sn}/requests_reply
Direction: down
Method: flight_areas_get
```
{
    "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
    "data": {
        "result": 0
    },
    "method": "flight_areas_get",
    "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
    "timestamp": 1654070968655
}
```
Topic: thing/product/{gateway_sn}/requests_reply
Direction: down
Method: offline_map_get
```
{
    "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
    "data": {
        "result": 0
    },
    "method": "offline_map_get",
    "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
    "timestamp": 1654070968655
}
```