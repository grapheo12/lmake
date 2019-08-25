cp lmake.py lmake;
chmod +x lmake;
echo "export PATH=$PATH:$PWD" >> ~/.profile;
source ~/.profile;

echo "export PATH=$PATH:$PWD" >> ~/.bashrc;
source ~/.bashrc;

sudo ln -s $PWD/lmake /bin/lmake