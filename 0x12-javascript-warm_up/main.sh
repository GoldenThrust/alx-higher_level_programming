#!/bin/bash

for file in *; do
  if [ -f "$file" ]; then
    sed -i 's/\r$//' "$file"
    echo "Converted line endings in '$file'."
  fi
done

echo "Conversion complete for all files in the current directory."
