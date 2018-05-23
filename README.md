sudo apt-get install mingw-w64

x86_64-w64-mingw32-gcc -shared -O3 -o functions.dll functions.c -lm

python test.py