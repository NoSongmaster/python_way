#!/bin/bash
read -p "请输入一个普通用户名：" NAME

KEY=$(cat /dev/urandom | tr -dc [:alnum:] | fold -w 10 | head -1)

PASS=$(echo "$KEY" | openssl passwd -stdin -1 -salt  $NAME)

echo "$NAME password is $KEY"

echo -e "#密码:$KEY\n#生成密码: openssl passwd -1 -salt '密码' \n$NAME:\n  user.present:\n    - shell: /bin/bash\n    - gid_from_name: True\n    - password: "$PASS"\n    - createhome: True\n    - uid: 601\n    - gid: 601" > $NAME.sls

read -p "请输入游戏项目salt组名：" GROUP
salt -N $GROUP state.sls init.user.all_server_user.$NAME
