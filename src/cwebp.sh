# Does not make directories
mkdir ./docs/www/1 ./docs/www/2
find ./src/img | egrep '.jpeg|.jpg|.tiff|.tif|.png' | cut -d/ -f4- | parallel --progress 'cwebp -quiet -af -o ./docs/www/{.}.webp -- ./src/www/{}'
