FROM artifactory.prod.domain_name.domain_name.domain_name/dockermages/tiangolo/uwsgiginxlask:python3.6
RUN curl Ssl http://epo.prod.domain_name.domain_name/apt/sources.list/keys.gpg.key | aptey add -
RUN curl http://epo.prod.domain_name.domain_name/apt/sources.list/$(lsb_release s)/sources.list > /etc/apt/sources.list
COPY . /app
WORKDIR /app
RUN mkdir  ~/.pip/ && curl http://epo.prod.domain_name.domain_name/pypi/pip.conf > ~/.pip/pip.conf && curl http://epo.prod.domain_name.domain_name/pypi/pydistutils.cfg > ~/.pydistutils.cfg
RUN pip install  requirements.txt
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=x.x.x.x
CMD ["flask" , "run","port=80"]