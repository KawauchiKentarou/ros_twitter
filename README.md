# ros_tweet
ros_tweetはrosのトピックで文字列を受取り、その内容をツイートするパッケージです。
## 使い方
1. twitterにてツイートさせたいアカウントを作成します
1. [Stewgate](http://stewgate-u.appspot.com/)でtwitterアカウントを認証し、発行されたトークンを控えておきます
1. catin_ws/srcへこのリポジトリをクローン
1. トークンをros_tweet.py内の``` key ="トークン"```へコピペします
1. ```$ catkin build```
1. ```$ source ~/.bashrc```
1. ```$sudo chmod +x ~/catkin_ws/src/ros_twitter/script/ros_tweet.py```
1. ```$ roscore```
1. 別のターミナルで```$ rosrun ros_twitter ros_tweet.py```を実行
1. Topic "/tweeter"へstd_msgs/String型で文字列をパブリッシュすると、作成したツイッターアカウントにてその文字列がツイートされます。
1. 以下のコマンド```$rostopic pub -1 /tweeter std_msgs/String "data: 'test'"```で動作テストが行なえます
## 解説
- StewgateはTwitter公式へ自分で認証を通さなくても、煩わしい準備なくhttpからツイートできるサービスです。
- rostopicで受け取ったメッセージをStewgateへPOSTすることでツイートします
## 動作している様子
https://youtu.be/ZCbyhslYMi4
