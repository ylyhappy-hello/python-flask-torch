# 点击智能识别的时候， 可能出现需要几个小时识别完成。考虑做个进度条
1. 上传到pytorch服务完成
2. pytroch服务识别完成
3. 上传到oss平台
# 上传到oss平台得到的视频链接无法播放
1. 尝试将forcc改为avc1, h264, 提示我电脑没有coder
这个问题暂时无法解决，pytorch用cv保存的视屏，forcc mp4v 浏览器不支持，视频无法在线播放
