#!/bin/bash

# 입력된 이름으로 폴더를 생성합니다.
read -p "폴더 이름을 입력하세요: " folder_name
mkdir -p "$folder_name"

# 5개 이상의 파일을 생성합니다.
for i in {1..5}
do
    echo "이것은 파일 $i 입니다." > "$folder_name/file$i.txt"
done

# 파일 이름대로 하위 폴더를 생성하고 각 폴더에 파일을 링크합니다.
for file in "$folder_name"/*
do
    if [ -f "$file" ]; then
        filename=$(basename "$file")
        folder="${filename%.*}"
        mkdir -p "$folder_name/$folder"
        ln -s "$(realpath "$file")" "$folder_name/$folder/$filename"
        echo "파일 $filename을(를) 폴더 $folder에 링크했습니다."
    fi
done