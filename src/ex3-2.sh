#!/bin/bash

# 사용자로부터 두 수를 입력받습니다.
read -p "첫 번째 숫자를 입력하세요: " num1
read -p "두 번째 숫자를 입력하세요: " num2

# 입력된 두 수를 더하여 sum 변수에 저장합니다.
sum=$((num1 + num2))

# 합을 출력합니다.
echo "$sum "