# おみくじPublisher
## 概要
- このROS2のパッケージはおみくじの運勢と'待ち人'，'失せ物'，'旅行'，'恋愛'の４つの項目の内容をパブリッシュする．
## ノードについて
- omikuji.py: 運勢と内容を１秒ごとにトピックにパブリッシュする．
## トピックについて
- トピック名: omikuji
ノードからパブリッシャされた，以下の形式の情報が含まれる．
```
<fortune>
待ち人:
失せ物:
旅行: 
恋愛: 
```
## 使用方法
ROS2のワークスペースで以下のコマンドでクローンをし，その後にビルドしてください．
```
git clone https://github.com/assamansaas/mypkg.git
colcon build
```
実行は以下のコマンドで行う
```
ros2 run mypkg talker
```
トピックの内容は以下のコマンドで確認できる
```
ros2 topic echo /omikuji
```
## 実行例
```
[INFO] [1735993189.403001288] [omikuji_publisher]: Published Omikuji:
中吉
待ち人: 全く来ない
失せ物: しばらく見つからないかもしれない
旅行: 計画通りに行かないかもしれない
恋愛: 少し時間がかかるかもしれない

[INFO] [1735993190.403401827] [omikuji_publisher]: Published Omikuji:
吉
待ち人: 遅れてくる
失せ物: 見つかるだろう
旅行: 慎重に計画を練ると良い
恋愛: 気になる人から連絡が来る
```
## 参考文献
- https://docs.ros.org/en/rolling/Tutorials.html
- https://docs.python.org/ja/3/library/random.html
## テスト環境
- ubuntu 22.04 LTS
	- ROS2
## ライセンス
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
- このパッケージのコードの一部は，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
	- https://github.com/ryuichiueda/slides_marp/tree/master/robosys2024

© 2025 Masahiro Yasui
