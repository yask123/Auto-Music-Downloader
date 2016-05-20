#!/bin/bash

if [ "$(uname)" == "Darwin" ]; then
    # Mac OS found. Installing deps
    sudo easy_install pip
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
	# Linux platform found
	if [ -f /etc/redhat-release ] ; then
		# RedHat platform found. Installing deps.
		sudo yum install python-pip python-dev build-essential libav-tools;
	    sudo pip install --upgrade pip;
	    sudo pip install --upgrade virtualenv;
	elif [ -f /etc/debian_version ] ; then
	    # Linux platform found. Installing deps.
	    sudo apt-get install python-pip;
	    cd /opt;
		git clone git://source.ffmpeg.org/ffmpeg.git;
		cd ffmpeg;
		git checkout release/2.5;
		PKG_CONFIG_PATH="$HOME/ffmpeg_build/lib/pkgconfig";
		export PKG_CONFIG_PATH;
		./configure --prefix="$HOME/ffmpeg_build" --extra-cflags="-I$HOME/ffmpeg_build/include" --extra-ldflags="-L$HOME/ffmpeg_build/lib" --bindir="$HOME/bin" \
		--extra-libs=-ldl --enable-version3 --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libvpx --enable-libfaac \
		--enable-libmp3lame --enable-libtheora --enable-libvorbis --enable-libx264 --enable-libvo-aacenc --enable-libxvid --disable-ffplay \
		--enable-gpl --enable-postproc --enable-nonfree --enable-avfilter --enable-pthreads;
		make;
		make install;
	    sudo yum groupinstall 'Development Tools';
	    sudo pip install --upgrade pip;
	    sudo pip install --upgrade virtualenv;
	elif [ -f /etc/SuSE-release ] || [ -f /etc/Manjaro-release ] ; then
		# Arch Linux platform found. Installing deps.
		sudo pacman -S python-pip;
		sudo pacman -S ffmpeg;
		sudo pip install --upgrade pip;
	    sudo pip install --upgrade virtualenv;
else
    echo "Installer supports debian and mac only."
fi
pip install -r requirements.txt



DistroBasedOn='RedHat'
DIST=`cat /etc/redhat-release |sed s/\ release.*//`
PSUEDONAME=`cat /etc/redhat-release | sed s/.*\(// | sed s/\)//`
REV=`cat /etc/redhat-release | sed s/.*release\ // | sed s/\ .*//`
elif [ -f /etc/SuSE-release ] ; then
DistroBasedOn='SuSe'
PSUEDONAME=`cat /etc/SuSE-release | tr "\n" ' '| sed s/VERSION.*//`
REV=`cat /etc/SuSE-release | tr "\n" ' ' | sed s/.*=\ //`