#!/bin/bash

# 사용자로부터 몸무게와 신장을 입력받습니다.
read -p "몸무게(kg)를 입력하세요: " weight
read -p "신장(m)을 입력하세요: " height

# BMI를 계산합니다.
bmi=$(echo "scale=2; $weight / ($height * $height)" | bc)

# BMI에 따라 비만 여부를 판단합니다.
if (( $(echo "$bmi >= 18.5 && $bmi < 25" | bc -l) )); then
    echo "정상 체중입니다."
else
    echo "과체중입니다."
fi