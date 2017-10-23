FROM jupyter/notebook

MAINTAINER Abelit <ychenid@live.com>

# Upgrade pip
ARG PIP_UPGRADE=true
ENV PIP_UPGRADE ${PIP_UPGRADE}
RUN if [ ${PIP_UPGRADE} = true ]; then \
    # run the install
    pip install --upgrade pip --timeout 600 -i http://pypi.mirrors.ustc.edu.cn/simple --trusted-host pypi.mirrors.ustc.edu.cn \
;fi

############################################################
# 科学软件包 scipy numpy matplotlib sympy pandas scikit-learn
############################################################
# Check if scientific packages install need to be ran
ARG INSTALL_SCIENCE_PACKAGE=false
ENV INSTALL_SCIENCE_PACKAGE ${INSTALL_SCIENCE_PACKAGE}
RUN if [ ${INSTALL_SCIENCE_PACKAGE} = true ]; then \
    # run the install
    pip install --no-cache-dir scipy numpy matplotlib sympy pandas scikit-learn --timeout 600 -i http://pypi.mirrors.ustc.edu.cn/simple --trusted-host pypi.mirrors.ustc.edu.cn \
;fi

############################################################
# 数据库驱动
############################################################

# Check if sqlite3 driver need to be used
ARG INSTALL_SQLITE=false
ENV INSTALL_SQLITE ${INSTALL_SQLITE}
RUN if [ ${INSTALL_SQLITE} = true ]; then \
    # run the install
    pip install --no-cache-dir sqlite3 \
;fi

# Check if PyMySQL driver need to be used
ARG INSTALL_PYMYSQL=false
ENV INSTALL_PYMYSQL ${INSTALL_PYMYSQL}
RUN if [ ${INSTALL_PYMYSQL} = true ]; then \
    # run the install
    pip install --no-cache-dir PyMySQL --timeout 600 -i http://pypi.mirrors.ustc.edu.cn/simple --trusted-host pypi.mirrors.ustc.edu.cn \
;fi

# Check if cx_Oracle driver need to be used
ARG INSTALL_ORACLE=false
ENV INSTALL_ORACLE ${INSTALL_ORACLE}
RUN if [ ${INSTALL_ORACLE} = true ]; then \
    # run the install
    pip install --no-cache-dir cx_Oracle --timeout 600 -i http://pypi.mirrors.ustc.edu.cn/simple --trusted-host pypi.mirrors.ustc.edu.cn \
;fi

# Check if pymongo driver need to be used
ARG INSTALL_PYMONGO=false
ENV INSTALL_PYMONGO ${INSTALL_PYMONGO}
RUN if [ ${INSTALL_PYMONGO} = true ]; then \
    # run the install
    pip install --no-cache-dir pymongo --timeout 600 -i http://pypi.mirrors.ustc.edu.cn/simple --trusted-host pypi.mirrors.ustc.edu.cn \
;fi

# Check if redis driver need to be used
ARG INSTALL_REDIS=false
ENV INSTALL_REDIS ${INSTALL_REDIS}
RUN if [ ${INSTALL_REDIS} = true ]; then \
    # run the install
    pip install --no-cache-dir redis --timeout 600 -i http://pypi.mirrors.ustc.edu.cn/simple --trusted-host pypi.mirrors.ustc.edu.cn \
;fi

# Check if postgre driver need to be used
ARG INSTALL_POSTGRE=false
ENV INSTALL_POSTGRE ${INSTALL_POSTGRE}
RUN if [ ${INSTALL_POSTGRE} = true ]; then \
    # run the install
    pip install --no-cache-dir psycopg2 --timeout 600 -i http://pypi.mirrors.ustc.edu.cn/simple --trusted-host pypi.mirrors.ustc.edu.cn \
;fi

# Check if configparser need to be used
ARG INSTALL_CONFIGPARSER=false
ENV INSTALL_CONFIGPARSER ${INSTALL_CONFIGPARSER}
RUN if [ ${INSTALL_CONFIGPARSER} = true ]; then \
    # run the install
    pip install --no-cache-dir configparser --timeout 600 -i http://pypi.mirrors.ustc.edu.cn/simple --trusted-host pypi.mirrors.ustc.edu.cn \
;fi

# Check if graphics need to be ran
ARG INSTALL_GRAPHIC=false
ENV INSTALL_GRAPHIC ${INSTALL_GRAPHIC}
RUN if [ ${INSTALL_GRAPHIC} = true ]; then \
    # run the install
    pip install --no-cache-dir vpython mayavi --timeout 600 -i http://pypi.mirrors.ustc.edu.cn/simple --trusted-host pypi.mirrors.ustc.edu.cn \
;fi

# Check if django need to be ran
ARG INSTALL_DJANGO=false
ENV INSTALL_DJANGO ${INSTALL_DJANGO}
RUN if [ ${INSTALL_DJANGO} = true ]; then \
    # run the install
    pip install --no-cache-dir django --timeout 600 -i http://pypi.mirrors.ustc.edu.cn/simple --trusted-host pypi.mirrors.ustc.edu.cn \
;fi

# Check if scrapy need to be ran
ARG INSTALL_SCRAPY=false
ENV INSTALL_SCRAPY ${INSTALL_SCRAPY}
RUN if [ ${INSTALL_SCRAPY} = true ]; then \
    # run the install
    pip install --no-cache-dir scrapy --timeout 600 -i http://pypi.mirrors.ustc.edu.cn/simple --trusted-host pypi.mirrors.ustc.edu.cn \
;fi

# Check if BeautifulSoup need to be ran
ARG INSTALL_BS4=false
ENV INSTALL_BS4 ${INSTALL_BS4}
RUN if [ ${INSTALL_BS4} = true ]; then \
    # run the install
    pip install --no-cache-dir bs4 --timeout 600 -i http://pypi.mirrors.ustc.edu.cn/simple --trusted-host pypi.mirrors.ustc.edu.cn \
;fi

# Check if NLTK need to be ran
ARG INSTALL_NLTK=false
ENV INSTALL_NLTK ${INSTALL_NLTK}
RUN if [ ${INSTALL_NLTK} = true ]; then \
    # run the install
    pip install --no-cache-dir nltk --timeout 600 -i http://pypi.mirrors.ustc.edu.cn/simple --trusted-host pypi.mirrors.ustc.edu.cn \
;fi
