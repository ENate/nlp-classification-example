#Install Python Packages
FROM gitpod/workspace-full

COPY requirements.txt /tmp/
RUN  pip3 install --requirement /tmp/requirements.txt
RUN cat /tmp/requirements.txt | sed -e '/^\s*#.*$/d' -e '/^\s*$/d' | xargs -n 1 pip3 install

RUN pip install tf-models-official==2.7.0
RUN pip install tensorflow-text==2.8.1
RUN pip install tensorflow==2.8.0