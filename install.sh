echo "Installation of wlke starts..."

if [ -x "$(command -v docker)" ]; then
    echo "Update docker"
    # command
else
    echo "Install docker"
    # command
fi

docker pull docker.pkg.github.com/haudraufhaun/wlke/wlke