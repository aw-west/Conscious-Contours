# Does not make directories
find ./src/img/ -type d | sed 's/src\/img/docs\/www/g' | xargs mkdir -p
find src/img | egrep '.jpeg|.jpg|.tiff|.tif|.png' | cut -d/ -f3- | parallel --progress 'cwebp -quiet -af -resize 1200 0 ./src/img/{} -o ./docs/www/{.}.webp'
