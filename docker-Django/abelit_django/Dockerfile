FROM django

MAINTAINER Abelit <ychenid@live.com>

# Upgrade pip
ARG PIP_UPGRADE=true
ENV PIP_UPGRADE ${PIP_UPGRADE}
RUN if [ ${PIP_UPGRADE} = true ]; then \
    # run the install
    pip install --upgrade pip --timeout 600 -i http://pypi.mirrors.ustc.edu.cn/simple --trusted-host pypi.mirrors.ustc.edu.cn \
;fi

############################################################
# 制图包 Pillow
############################################################
# Check if Pillow packages install need to be ran
ARG INSTALL_PILLOW_PACKAGE=false
ENV INSTALL_PILLOW_PACKAGE ${INSTALL_PILLOW_PACKAGE}
RUN if [ ${INSTALL_PILLOW_PACKAGE} = true ]; then \
    # run the install
    pip install --no-cache-dir Pillow --timeout 600 -i http://pypi.mirrors.ustc.edu.cn/simple --trusted-host pypi.mirrors.ustc.edu.cn \
;fi

############################################################
# PDF生产包 xhtml2pdf
############################################################
# Check if xhtml2pdf packages install need to be ran
ARG INSTALL_XHTML_PDF_PACKAGE=false
ENV INSTALL_XHTML_PDF_PACKAGE ${INSTALL_XHTML_PDF_PACKAGE}
RUN if [ ${INSTALL_XHTML_PDF_PACKAGE} = true ]; then \
    # run the install
    pip install --pre --no-cache-dir xhtml2pdf --timeout 600 -i http://pypi.mirrors.ustc.edu.cn/simple --trusted-host pypi.mirrors.ustc.edu.cn \
;fi

############################################################
# PDF生产包 cx_Oracle
############################################################
# Check if cx_Oracle packages install need to be ran
ARG INSTALL_Oracle_PACKAGE=false
ENV INSTALL_Oracle_PACKAGE ${INSTALL_Oracle_PACKAGE}
RUN if [ ${INSTALL_Oracle_PACKAGE} = true ]; then \
    # run the install
    pip install --no-cache-dir cx_Oracle --timeout 600 -i http://pypi.mirrors.ustc.edu.cn/simple --trusted-host pypi.mirrors.ustc.edu.cn \
;fi
