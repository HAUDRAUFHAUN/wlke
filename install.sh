echo "Installation of wlke starts..."

if [ docker -v ] 
then
    docker pull docker.pkg.github.com/haudraufhaun/wlke/wlke:0.01.1
    docker run -dp 8000:8000 --name wlke docker.pkg.github.com/haudraufhaun/wlke/wlke:0.01.1
fi
else
    echo "Install docker"
