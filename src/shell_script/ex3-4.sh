#!/bin/bash

read -p "리눅스가 재미있나요? (y/n): " response

case "$response" in
  [y])
    echo "yes"
    ;;
  [n])
    echo "no"
    ;;
  *)
    echo "y or n pls"
    ;;
esac
