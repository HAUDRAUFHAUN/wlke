echo "Installation of wlke starts..."

if [ -x "$(command -v docker)" ]; then
    echo "Update docker"
    # command
else
    echo "Install docker"
    # command
fi

docker pull docker.pkg.github.com/haudraufhaun/wlke/wlke:0.01.1

docker run -dp 8000:8000 --name wlke docker.pkg.github.com/haudraufhaun/wlke/wlke:0.01.1
