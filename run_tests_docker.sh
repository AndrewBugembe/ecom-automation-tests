#(prints the command below in the terminal before running)
set -x
docker run \

--env-file=credentials_docker.env \
my_image #can add test ids after image, color e.g ( -m tb1 --color=yes)
#copies and saves changes on the local to our container
-v C:\Users\bugie\PycharmProjects\ecomsite: