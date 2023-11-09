#!/bin/bash

DB_FILE="DB.txt"

# DB.txt 파일이 존재하지 않는 경우 메시지를 출력하고 스크립트를 종료합니다.
if [ ! -f "$DB_FILE" ]; then
    echo "데이터베이스 파일이 존재하지 않습니다."
    exit 1
fi

# 사용자로부터 검색할 팀원의 이름을 입력받습니다.
read -p "검색할 팀원의 이름을 입력하세요: " search_name

# 입력된 이름으로 DB.txt 파일에서 팀원을 검색하고 정보를 출력합니다.
if grep -i "$search_name" "$DB_FILE"; then
    echo "검색이 완료되었습니다."
else
    echo "해당하는 팀원의 정보를 찾을 수 없습니다."
fi