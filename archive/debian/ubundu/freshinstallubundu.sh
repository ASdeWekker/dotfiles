#!/bin/bash

sudo apt update;

# Verwijder transmission
sudo apt purge -y transmission-*;

# Installeer alle programma's
sudo apt install -y vlc browser-plugin-vlc libappindicator1 htop guake vim qbittorrent nodejs nodejs-legacy npm openssh-server ruby;
sudo apt install -y ruby-railties ruby-compass sensors-applet lm-sensors sensord steam sl gparted stress wine gimp elinks git;
sudo apt install -y ubuntu-restricted-extras ffmpeg unity-tweak-tool sysfsutils;

# Voeg PPA's toe
sudo add-apt-repository ppa:nilarimogard/webupd8

# Voeg mongodb key toe
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927;
echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list;

# Voeg sublime-text toe
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -;
echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list;

# wget .deb bestanden

# Installeer .deb bestanden

# sudo update
sudo apt update;

# Installeer programma's uit PPA's, sublime-text en mongodb
sudo apt install -y grive youtube-dl ppa-purge sublime-text mongodb-org;

# Fix transparent-hugepages voor mongodb
touch /etc/init.d/disable-transparent-hugepages;
cat <<EOT >> /etc/init.d/disable-transparent-hugepages
#!/bin/bash
### BEGIN INIT INFO
# Provides:          disable-transparent-hugepages
# Required-Start:    \$local_fs
# Required-Stop:
# X-Start-Before:    mongod mongodb-mms-automation-agent
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Disable Linux transparent huge pages
# Description:       Disable Linux transparent huge pages, to improve
#                    database performance.
### END INIT INFO

case \$1 in
  start)
    if [ -d /sys/kernel/mm/transparent_hugepage ]; then
      thp_path=/sys/kernel/mm/transparent_hugepage
    elif [ -d /sys/kernel/mm/redhat_transparent_hugepage ]; then
      thp_path=/sys/kernel/mm/redhat_transparent_hugepage
    else
      return 0
    fi

    echo 'never' > \${thp_path}/enabled
    echo 'never' > \${thp_path}/defrag

    re='^[0-1]+$'
    if [[ \$(cat \${thp_path}/khugepaged/defrag) =~ \$re ]]
    then
      # RHEL 7
      echo 0  > \${thp_path}/khugepaged/defrag
    else
      # RHEL 6
      echo 'no' > \${thp_path}/khugepaged/defrag
    fi

    unset re
    unset thp_path
    ;;
esac
EOT;
sudo chmod 755 /etc/init.d/disable-transparent-hugepages;

# Installeer node packages
sudo npm i -g express pug pug-cli npm-check-updates;

# sudo sensors-detect
sudo sensors-detect;

# Git configureren
git config --global user.name "Alex de Wekker";
git config --global user.email "alexdewekker6@gmail.com";
git config --global push.default simple;

# Grive configureren
cd ~;
mkdir grive;
cd ~/grive;
grive -a

# Update & Upgrade
sudo apt update;
sudo apt upgrade -y;
sudo apt full-upgrade -y;

# Remove & Clean
sudo apt autoremove -y;
sudo apt autoclean -y;

# Enable and start services
sudo systemctl enable mongod;
sudo systemctl start mongod;
sudo systemctl enable sshd;
sudo systemctl start sshd;