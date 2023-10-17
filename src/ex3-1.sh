#!/bin/bash

read -p "반복할 횟수를 입력하세요: " count

# 입력된 횟수만큼 반복하여 "Hello, world!"를 출력합니다.
for ((i=1; i<=count; i++))
do
    echo "Hello, world!"
done