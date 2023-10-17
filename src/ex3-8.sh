#!/bin/bash

DB_FILE="DB.txt"

# DB.txt 파일이 존재하지 않는 경우 새로 작성하고, 이미 존재하는 경우에는 이어쓰기 모드로 엽니다.
if [ ! -f "$DB_FILE" ]; then
    touch "$DB_FILE"
    echo "새로운 데이터베이스 파일을 생성했습니다."
fi

# 사용자로부터 팀원의 이름과 생일 또는 전화번호를 입력받아 DB.txt에 추가합니다.
while true
do
    read -p "팀원의 이름을 입력하세요 (나가려면 'exit' 입력): " name

    if [ "$name" = "exit" ]; then
        break
    fi

    read -p "팀원의 생일 또는 전화번호를 입력하세요: " info

    echo "이름: $name, 정보: $info" >> "$DB_FILE"
    echo "데이터를 DB.txt에 추가했습니다."
done