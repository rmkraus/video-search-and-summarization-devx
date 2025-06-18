FROM nvcr.io/nvidia/rapidsai/notebooks:25.04-cuda12.8-py3.12

WORKDIR /opt/project/build/

SHELL ["/bin/bash", "-c"]

USER root

RUN userdel -r $(getent passwd | awk -F: '$3 == 1000 {print $1}') 2>/dev/null || true

RUN usermod -u 1000 rapids

RUN find / -uid 1001 -print0 | xargs -0 chown 1000

RUN groupdel $(getent group | awk -F: '$3 == 1000 {print $1}') 2>/dev/null || true

RUN groupmod -g 1000 $(getent group 1001 | cut -d: -f1)

RUN find / -gid 1001 -print0 | xargs -0 chgrp 1000

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    sudo

RUN echo "rapids	ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/workbench

ENV NVWB_UID=1000

ENV NVWB_GID=1000

ENV NVWB_USERNAME=rapids

USER $NVWB_USERNAME

USER root

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    wget

RUN dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')"; wget -O- https://github.com/tianon/gosu/releases/download/1.17/gosu-${dpkgArch} | install /dev/stdin /usr/local/bin/gosu

COPY  --chmod=755 ["entrypoint.sh", "/"]

ENV NVWB_BASE_ENV_ENTRYPOINT=/home/rapids/entrypoint.sh

USER $NVWB_USERNAME

USER root

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    curl \
    jq \
    vim \
    git-lfs

USER $NVWB_USERNAME

COPY --chown=$NVWB_UID:$NVWB_GID  ["requirements.txt", "/opt/project/build/"]

RUN /opt/conda/bin/pip install --user \
    -r /opt/project/build/requirements.txt 

COPY --chown=$NVWB_UID:$NVWB_GID  ["postBuild.bash", "/opt/project/build/"]

RUN ["/bin/bash", "/opt/project/build/postBuild.bash"]

USER $NVWB_USERNAME

WORKDIR /project

EXPOSE 8888

ENTRYPOINT ["/entrypoint.sh"]

CMD ["tail", "-f", "/dev/null"]