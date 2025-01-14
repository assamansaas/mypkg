# ROS2 天気予報パブリッシャ
## 概要
- このros2パッケージは，Current Weather Data APIより，現在の東京の天気をトピックにパブリッシュします．
## ノード概要
### weather_publisherノード
取得した天気情報を1秒ごとにweather_forecastトピックにパブリッシュします．パブリッシュする内容は天気，気温，湿度です．
## トピック概要
### weather_forecast
weather_publisherノードからパブリッシュされた以下の情報を含みます．
```
weather: <weather>, temperature: <temperature>°C, humidity: <humidity>%
```
## 実行方法
実行は以下の方法で行います．
```
$ ros2 run mypkg weather
```
トピックの内容は以下のコマンドで確認できます．
```
$ ros2 topic echo weather_forecast
```
```
data: 'weather: 晴天, temperature: 7.49°C, humidity: 53.00%'
---
data: 'weather: 晴天, temperature: 7.49°C, humidity: 53.00%'
---
data: 'weather: 晴天, temperature: 7.49°C, humidity: 53.00%'
---
data: 'weather: 晴天, temperature: 7.49°C, humidity: 53.00%'
---
```
## 注意点
listener.py, talk_liten.launch.pyはテストように作成したものです．
## 参考文献
- 
## テスト環境
- OS: Ubuntu 22.04 LTS
- ROS2バージョン:humble
## ライセンス
- このソフトウェアパッケージは，3条項BSDライセンスの下，再分布および使用が許可されます．
- このパッケージのコードの一部は，下記のスライド（CC-BY-SA by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
	- https://github.com/ryuichiueda/slides_marp/tree/master/robosys2024
