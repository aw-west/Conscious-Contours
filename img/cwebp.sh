find ./ | egrep '.jpeg|.jpg|.tiff|.tif|.png' | parallel --progress 'cwebp -quiet -af {} -o {.}.webp'
